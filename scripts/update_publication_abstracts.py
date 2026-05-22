#!/usr/bin/env python3
"""Find and fill publication abstracts.

The script is intentionally dependency-light: it uses the arXiv Atom API when a
paper has an arXiv identifier, searches arXiv by exact-ish title as a fallback,
and only then tries to extract an abstract from the linked PDF with `pdftotext`.

By default this is a dry run. Pass --write to update publication front matter.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import os
import re
import shutil
import ssl
import subprocess
import sys
import tempfile
import textwrap
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


ARXIV_API = "http://export.arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"


def split_front_matter(path: Path) -> tuple[str, str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path} does not start with YAML front matter")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError(f"{path} has no closing front matter marker")
    return text[:4], text[4:end], text[end:]


def find_field_span(front_matter: str, key: str) -> tuple[int, int] | None:
    match = re.search(rf"(?m)^{re.escape(key)}\s*:", front_matter)
    if not match:
        return None

    next_match = re.search(
        r"(?m)^(?:[A-Za-z_][A-Za-z0-9_-]*\s*:|# )",
        front_matter[match.end() :],
    )
    if not next_match:
        return match.start(), len(front_matter)
    return match.start(), match.end() + next_match.start()


def get_scalar(front_matter: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}\s*:\s*(.*)$", front_matter)
    if not match:
        return ""
    value = match.group(1).strip()
    if value in {"''", '""'}:
        return ""
    return value.strip("'\"")


def abstract_is_empty(front_matter: str) -> bool:
    span = find_field_span(front_matter, "abstract")
    if not span:
        return True
    block = front_matter[span[0] : span[1]]
    value = block.split(":", 1)[1].strip()
    return value in {"", "''", '""'}


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace("'", "''")
    return f"'{escaped}'"


def yaml_unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == "'" and value[-1] == "'":
        return value[1:-1].replace("''", "'").replace("\\\\", "\\")
    if len(value) >= 2 and value[0] == '"' and value[-1] == '"':
        return value[1:-1]
    return value


def yaml_block(key: str, value: str) -> str:
    wrapped = "\n".join(textwrap.wrap(value.strip(), width=88))
    if not wrapped:
        return f"{key}: ''\n"
    indented = "\n".join(f"  {line}" if line else "" for line in wrapped.splitlines())
    return f"{key}: >-\n{indented}\n"


def format_versions(versions: list[dict[str, str]]) -> str:
    if not versions:
        return ""

    lines = ["paper_versions:"]
    for version in versions:
        lines.append(f"- retrieved_at: {yaml_quote(version['retrieved_at'])}")
        for key in ("source", "version", "url", "pdf_url", "updated", "title"):
            value = version.get(key)
            if value:
                lines.append(f"  {key}: {yaml_quote(value)}")
    return "\n".join(lines) + "\n"


def parse_versions(front_matter: str) -> list[dict[str, str]]:
    span = find_field_span(front_matter, "paper_versions")
    if not span:
        return []

    block = front_matter[span[0] : span[1]]
    versions: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for raw_line in block.splitlines()[1:]:
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("- "):
            if current:
                versions.append(current)
            current = {}
            line = line[2:].strip()
        if ":" not in line or current is None:
            continue
        key, value = line.split(":", 1)
        current[key.strip()] = yaml_unquote(value.strip())
    if current:
        versions.append(current)
    return versions


def merge_versions(existing: list[dict[str, str]], incoming: list[dict[str, str]]) -> list[dict[str, str]]:
    seen = {
        (
            version.get("retrieved_at", ""),
            version.get("source", ""),
            version.get("version", ""),
            version.get("url", ""),
            version.get("pdf_url", ""),
        )
        for version in existing
    }
    merged = list(existing)
    for version in incoming:
        key = (
            version.get("retrieved_at", ""),
            version.get("source", ""),
            version.get("version", ""),
            version.get("url", ""),
            version.get("pdf_url", ""),
        )
        if key not in seen:
            merged.append(version)
            seen.add(key)
    return merged


def replace_field(front_matter: str, key: str, replacement: str) -> str:
    span = find_field_span(front_matter, key)
    if not span:
        return front_matter.rstrip() + "\n" + replacement
    start, end = span
    return front_matter[:start] + replacement + front_matter[end:].lstrip("\n")


def update_front_matter(
    front_matter: str, abstract: str | None, versions: list[dict[str, str]], force: bool
) -> str:
    updated = front_matter
    if abstract and (force or abstract_is_empty(front_matter)):
        updated = replace_field(updated, "abstract", yaml_block("abstract", abstract))
    if versions:
        updated = replace_field(updated, "paper_versions", format_versions(merge_versions(parse_versions(front_matter), versions)))
    return updated


def normalize_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()


def similar_title(left: str, right: str) -> bool:
    left_norm = normalize_title(left)
    right_norm = normalize_title(right)
    return left_norm == right_norm or left_norm in right_norm or right_norm in left_norm


def arxiv_id_from_text(text: str) -> str | None:
    patterns = [
        r"arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5})(?:v\d+)?",
        r"arXiv[:.]\s*([0-9]{4}\.[0-9]{4,5})(?:v\d+)?",
        r"10\.48550/arXiv\.([0-9]{4}\.[0-9]{4,5})(?:v\d+)?",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            return match.group(1)
    return None


def fetch_url(url: str, timeout: int) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "leaf-lab-abstract-updater/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.read()
    except urllib.error.URLError as exc:
        if isinstance(exc.reason, ssl.SSLCertVerificationError):
            context = ssl._create_unverified_context()
            with urllib.request.urlopen(request, timeout=timeout, context=context) as response:
                return response.read()
        raise


def parse_arxiv_entry(entry: ET.Element, retrieved_at: str) -> tuple[str, dict[str, str]]:
    title = " ".join((entry.findtext(f"{ATOM}title") or "").split())
    summary = " ".join((entry.findtext(f"{ATOM}summary") or "").split())
    entry_id = entry.findtext(f"{ATOM}id") or ""
    updated = entry.findtext(f"{ATOM}updated") or ""

    pdf_url = ""
    for link in entry.findall(f"{ATOM}link"):
        if link.attrib.get("title") == "pdf" or link.attrib.get("type") == "application/pdf":
            pdf_url = link.attrib.get("href", "")
            break

    version = ""
    version_node = entry.find(f"{ARXIV}version")
    if version_node is not None:
        version = version_node.attrib.get("version", "")

    version_record = {
        "retrieved_at": retrieved_at,
        "source": "arxiv",
        "version": version,
        "url": entry_id,
        "pdf_url": pdf_url,
        "updated": updated,
        "title": title,
    }
    return html.unescape(summary), version_record


def arxiv_query(params: dict[str, str], timeout: int) -> list[ET.Element]:
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    data = fetch_url(url, timeout)
    root = ET.fromstring(data)
    return root.findall(f"{ATOM}entry")


def arxiv_by_id(arxiv_id: str, retrieved_at: str, timeout: int) -> tuple[str, dict[str, str]] | None:
    entries = arxiv_query({"id_list": arxiv_id, "max_results": "1"}, timeout)
    if not entries:
        return None
    return parse_arxiv_entry(entries[0], retrieved_at)


def arxiv_by_title(title: str, retrieved_at: str, timeout: int) -> tuple[str, dict[str, str]] | None:
    query = f'ti:"{title}"'
    entries = arxiv_query(
        {"search_query": query, "sortBy": "lastUpdatedDate", "sortOrder": "descending", "max_results": "5"},
        timeout,
    )
    for entry in entries:
        entry_title = " ".join((entry.findtext(f"{ATOM}title") or "").split())
        if similar_title(title, entry_title):
            return parse_arxiv_entry(entry, retrieved_at)
    return None


def extract_pdf_url(front_matter: str) -> str:
    return get_scalar(front_matter, "url_pdf")


def resolve_pdf(path: Path, url: str, timeout: int) -> Path | None:
    if not url:
        return None
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme in {"http", "https"}:
        if not parsed.path.lower().endswith(".pdf") and "arxiv.org/pdf/" not in url:
            return None
        data = fetch_url(url, timeout)
        handle = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        handle.write(data)
        handle.close()
        return Path(handle.name)

    local = (path.parent / url).resolve()
    if local.exists() and local.suffix.lower() == ".pdf":
        return local
    return None


def pdf_text(pdf_path: Path) -> str:
    if not shutil.which("pdftotext"):
        raise RuntimeError("pdftotext is not installed")
    result = subprocess.run(
        ["pdftotext", "-f", "1", "-l", "2", str(pdf_path), "-"],
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout


def extract_abstract_from_text(text: str) -> str | None:
    cleaned = re.sub(r"[ \t]+", " ", text.replace("\r", "\n"))
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    match = re.search(r"(?is)(?:^|\n)\s*abstract\s*[:.\-]?\s*(.+)", cleaned)
    if not match:
        return None

    rest = match.group(1)
    stop = re.search(
        r"(?is)\n\s*(?:1\s*\.?\s*)?(?:introduction|keywords|index terms|background|related work)\b",
        rest,
    )
    if stop:
        rest = rest[: stop.start()]

    abstract = " ".join(rest.split())
    abstract = re.sub(r"^(?:abstract\s*)[:.\-]?\s*", "", abstract, flags=re.IGNORECASE)
    if len(abstract) < 80 or len(abstract) > 3500:
        return None
    if abstract.count(".") == 0:
        return None
    return abstract


def find_abstract(path: Path, front_matter: str, retrieved_at: str, timeout: int) -> tuple[str | None, list[dict[str, str]], str]:
    title = get_scalar(front_matter, "title")
    searchable = "\n".join(
        [
            title,
            get_scalar(front_matter, "publication"),
            get_scalar(front_matter, "url_pdf"),
            get_scalar(front_matter, "url_doi"),
            get_scalar(front_matter, "url_project"),
        ]
    )

    versions: list[dict[str, str]] = []
    arxiv_id = arxiv_id_from_text(searchable)
    if arxiv_id:
        result = arxiv_by_id(arxiv_id, retrieved_at, timeout)
        if result:
            abstract, version = result
            versions.append(version)
            return abstract, versions, "arxiv-id"

    if title:
        result = arxiv_by_title(title, retrieved_at, timeout)
        if result:
            abstract, version = result
            versions.append(version)
            return abstract, versions, "arxiv-title"

    pdf_url = extract_pdf_url(front_matter)
    pdf_path = None
    try:
        pdf_path = resolve_pdf(path, pdf_url, timeout)
        if pdf_path:
            abstract = extract_abstract_from_text(pdf_text(pdf_path))
            versions.append(
                {
                    "retrieved_at": retrieved_at,
                    "source": "pdf",
                    "url": pdf_url,
                    "title": title,
                }
            )
            return abstract, versions, "pdf" if abstract else "pdf-no-abstract"
    finally:
        if pdf_path and str(pdf_path).startswith(tempfile.gettempdir()):
            try:
                pdf_path.unlink()
            except OSError:
                pass

    return None, versions, "not-found"


def iter_publications(content_dir: Path, slug: str | None) -> list[Path]:
    if slug:
        return [content_dir / slug / "index.md"]
    return sorted(content_dir.glob("*/index.md"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--content-dir", default="content/publication", type=Path)
    parser.add_argument("--slug", help="Only update one publication slug")
    parser.add_argument("--write", action="store_true", help="Write changes instead of reporting a dry run")
    parser.add_argument("--force", action="store_true", help="Replace existing non-empty abstracts")
    parser.add_argument("--timeout", type=int, default=20)
    parser.add_argument("--limit", type=int, help="Process at most this many publications")
    args = parser.parse_args()

    retrieved_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    paths = iter_publications(args.content_dir, args.slug)
    if args.limit:
        paths = paths[: args.limit]

    changed = 0
    for path in paths:
        if not path.exists():
            print(f"missing: {path}", file=sys.stderr)
            continue
        try:
            prefix, front_matter, suffix = split_front_matter(path)
            if not args.force and not abstract_is_empty(front_matter):
                print(f"skip existing abstract: {path.parent.name}")
                continue

            abstract, versions, method = find_abstract(path, front_matter, retrieved_at, args.timeout)
            if not abstract:
                print(f"no reliable abstract ({method}): {path.parent.name}")
                continue

            new_front_matter = update_front_matter(front_matter, abstract, versions, args.force)
            if new_front_matter == front_matter:
                print(f"unchanged: {path.parent.name}")
                continue

            changed += 1
            print(f"{'update' if args.write else 'would update'} ({method}): {path.parent.name}")
            if args.write:
                path.write_text(prefix + new_front_matter.rstrip() + suffix, encoding="utf-8")
        except (ET.ParseError, OSError, RuntimeError, subprocess.CalledProcessError, urllib.error.URLError, ValueError) as exc:
            print(f"error: {path.parent.name}: {exc}", file=sys.stderr)

    mode = "updated" if args.write else "would update"
    print(f"{mode} {changed} publication(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
