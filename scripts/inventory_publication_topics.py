#!/usr/bin/env python3
"""Inventory publication topic tags for offline review.

This script reads publication front matter from ``content/publication/*/index.md``
and writes review-only metadata to ``metadata/publication_topics_inventory.json``
and ``metadata/publication_topics_inventory.md``. It does not modify website
content.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


DEFAULT_CONTENT_DIR = Path("content/publication")
DEFAULT_OUTPUT_DIR = Path("metadata")

TOPIC_RULES: dict[str, list[str]] = {
    "autonomous driving": [
        r"\bautonomous (vehicle|driving|car|cars|vehicles|navigation)\b",
        r"\bdriving\b",
        r"\btraffic\b",
        r"\bwaymo\b",
        r"\blidar\b",
        r"\broads?\b",
    ],
    "autonomous exploration": [
        r"\bexploration\b",
        r"\bexplore\b",
        r"\binformation[- ]?seeking\b",
        r"\bintrinsic control\b",
    ],
    "benchmarks": [
        r"\bbenchmark\b",
        r"\bchallenge\b",
        r"\bdataset\b",
        r"\bleaderboard\b",
    ],
    "compression": [
        r"\bcompression\b",
        r"\bcompress\b",
        r"\bprun(?:e|ing)\b",
        r"\bnetwork to network\b",
    ],
    "computer vision": [
        r"\bcomputer vision\b",
        r"\bvisual\b",
        r"\bvision\b",
        r"\bimage\b",
        r"\bvideo\b",
        r"\blidar\b",
        r"\bpoint ?cloud\b",
        r"\bradiance field\b",
        r"\b3d scene\b",
    ],
    "first-person video": [
        r"\bfirst[- ]person\b",
        r"\begocentric\b",
        r"\bactivity forecasting\b",
    ],
    "forecasting": [
        r"\bforecast(?:ing|s)?\b",
        r"\bpredict(?:ion|ive|ing)?\b",
        r"\bfuture\b",
        r"\btrajectory\b",
        r"\bworld model\b",
        r"\bsimulation\b",
    ],
    "generative models": [
        r"\bgenerative\b",
        r"\bgenerate\b",
        r"\bdiffusion\b",
        r"\bflow matching\b",
        r"\bautoregressive\b",
        r"\badversarial\b",
        r"\bgan\b",
        r"\bvariational\b",
        r"\bprobabilistic\b",
        r"\bworld model\b",
    ],
    "imitation learning": [
        r"\bimitation learning\b",
        r"\bimitation\b",
        r"\bimitative\b",
        r"\bdemonstrations?\b",
        r"\blearning from.*demonstrations?\b",
        r"\bbehavioral priors?\b",
    ],
    "intrinsic control": [
        r"\bintrinsic control\b",
        r"\bintrinsic motivation\b",
        r"\binformation capture\b",
        r"\bsurprise\b",
    ],
    "machine learning": [
        r"\bmachine learning\b",
        r"\blearning\b",
        r"\bneural\b",
        r"\bdeep\b",
        r"\bmodel\b",
    ],
    "manipulation": [
        r"\bmanipulation\b",
        r"\bmanipulat(?:e|ing|or)\b",
        r"\bgrasp(?:ing)?\b",
    ],
    "model-based control": [
        r"\bmodel predictive control\b",
        r"\bmpc\b",
        r"\bplanning\b",
        r"\bplanner\b",
        r"\bcontrol\b",
        r"\bpolicy\b",
    ],
    "offroad navigation": [
        r"\boff[- ]?road\b",
        r"\bunstructured outdoor\b",
        r"\bopen[- ]world navigation\b",
    ],
    "reinforcement learning": [
        r"\breinforcement learning\b",
        r"\bpolicy gradient\b",
        r"\brl\b",
        r"\bq[- ]?learning\b",
        r"\breward\b",
    ],
    "reward learning": [
        r"\breward\b",
        r"\binverse reinforcement learning\b",
        r"\bpreference[- ]based\b",
        r"\bpreferences?\b",
        r"\bcost function\b",
    ],
    "robotics": [
        r"\brobot(?:s|ic|ics)?\b",
        r"\bnavigation\b",
        r"\bmanipulation\b",
        r"\bcontrol\b",
        r"\bembodied\b",
    ],
    "social navigation": [
        r"\bsocial navigation\b",
        r"\bsocial robot\b",
        r"\bcrowd\b",
        r"\bhuman[- ]aware\b",
    ],
}

NON_TOPICAL_TAGS = {"paper award"}
AUTO_REVIEW_TOPICS = {
    "autonomous driving",
    "autonomous exploration",
    "first-person video",
    "generative models",
    "intrinsic control",
    "manipulation",
    "offroad navigation",
    "social navigation",
}

def split_front_matter(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path} does not start with YAML front matter")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError(f"{path} has no closing front matter marker")
    return text[4:end]


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


def yaml_unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == "'" and value[-1] == "'":
        return value[1:-1].replace("''", "'").replace("\\\\", "\\")
    if len(value) >= 2 and value[0] == '"' and value[-1] == '"':
        return value[1:-1].replace('\\"', '"')
    return value


def parse_scalar(front_matter: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}\s*:\s*(.*)$", front_matter)
    if not match:
        return ""
    value = match.group(1).strip()
    if value in {"", "''", '""'}:
        return ""
    return yaml_unquote(value)


def parse_list(front_matter: str, key: str) -> list[str]:
    span = find_field_span(front_matter, key)
    if not span:
        return []
    block = front_matter[span[0] : span[1]]
    first_value = block.split(":", 1)[1].strip()
    if first_value == "[]":
        return []
    if first_value.startswith("[") and first_value.endswith("]"):
        try:
            return [str(item) for item in json.loads(first_value.replace("'", '"'))]
        except json.JSONDecodeError:
            items = re.findall(r"""["']([^"']+)["']""", first_value)
            return [item.strip() for item in items if item.strip()]

    values: list[str] = []
    for raw_line in block.splitlines()[1:]:
        line = raw_line.strip()
        if not line.startswith("- "):
            continue
        values.append(yaml_unquote(line[2:].strip()))
    return values


def parse_block_text(front_matter: str, key: str) -> str:
    span = find_field_span(front_matter, key)
    if not span:
        return ""
    block = front_matter[span[0] : span[1]]
    value = block.split(":", 1)[1].strip()
    if value in {"", "''", '""'}:
        return ""
    if value.startswith(">-") or value.startswith("|"):
        parts = [line.strip() for line in block.splitlines()[1:] if line.strip()]
        return " ".join(parts)
    return yaml_unquote(value)


def matching_rules(text: str) -> dict[str, list[str]]:
    matches: dict[str, list[str]] = {}
    for topic, patterns in TOPIC_RULES.items():
        topic_matches: list[str] = []
        for pattern in patterns:
            if re.search(pattern, text, flags=re.IGNORECASE):
                topic_matches.append(pattern)
        if topic_matches:
            matches[topic] = topic_matches
    return matches


def flag_publication(pub: dict[str, Any]) -> list[dict[str, Any]]:
    tags = set(pub["tags"])
    topical_tags = tags - NON_TOPICAL_TAGS
    flags: list[dict[str, Any]] = []

    missing = sorted(
        topic
        for topic, matches in pub["topic_evidence"].items()
        if topic in AUTO_REVIEW_TOPICS
        and topic not in topical_tags
        and len(matches) >= 2
        and not any(topic in flag.get("suggested_additions", []) for flag in flags)
    )
    if missing:
        flags.append(
            {
                "type": "heuristic_possible_missing_tags",
                "message": "Repeated abstract/title keyword evidence suggests these topic tags may be missing. Review manually before changing.",
                "suggested_additions": missing,
            }
        )

    if not pub["abstract"]:
        flags.append(
            {
                "type": "missing_abstract",
                "message": "No abstract was found in front matter; read the PDF or paper page before reviewing tags.",
            }
        )

    return flags


def read_publications(content_dir: Path) -> list[dict[str, Any]]:
    publications: list[dict[str, Any]] = []
    for index_path in sorted(content_dir.glob("*/index.md")):
        front_matter = split_front_matter(index_path)
        title = parse_scalar(front_matter, "title")
        abstract = parse_block_text(front_matter, "abstract")
        publication = parse_block_text(front_matter, "publication")
        publication_short = parse_scalar(front_matter, "publication_short")
        date = parse_scalar(front_matter, "date")
        tags = parse_list(front_matter, "tags")
        url_pdf = parse_scalar(front_matter, "url_pdf")

        evidence_text = " ".join([title, abstract, publication, publication_short])
        rule_matches = matching_rules(evidence_text)
        suggested_topics = sorted(rule_matches)

        pub = {
            "slug": index_path.parent.name,
            "path": str(index_path),
            "title": title,
            "date": date,
            "publication": publication,
            "publication_short": publication_short,
            "tags": tags,
            "abstract": abstract,
            "url_pdf": url_pdf,
            "local_pdfs": sorted(str(path.relative_to(index_path.parent)) for path in index_path.parent.glob("*.pdf")),
            "suggested_topics": suggested_topics,
            "topic_evidence": rule_matches,
        }
        pub["review_flags"] = flag_publication(pub)
        publications.append(pub)
    return publications


def write_markdown(path: Path, inventory: dict[str, Any]) -> None:
    lines = [
        "# Publication Topic Inventory",
        "",
        f"Generated: {inventory['generated_at']}",
        f"Publication count: {inventory['publication_count']}",
        "",
        "## Topics",
        "",
    ]
    for topic in inventory["topics"]:
        lines.append(f"- {topic['tag']}: {topic['count']}")

    lines.extend(["", "## Review Flags", ""])
    flagged = [pub for pub in inventory["publications"] if pub["review_flags"]]
    if not flagged:
        lines.append("No review flags.")
    for pub in flagged:
        lines.append(f"### {pub['title']}")
        lines.append("")
        lines.append(f"- Slug: `{pub['slug']}`")
        lines.append(f"- Current tags: {', '.join(pub['tags']) if pub['tags'] else '(none)'}")
        lines.append(f"- Suggested topics: {', '.join(pub['suggested_topics']) if pub['suggested_topics'] else '(none)'}")
        for flag in pub["review_flags"]:
            lines.append(f"- Flag: `{flag['type']}` - {flag['message']}")
            if flag.get("suggested_additions"):
                lines.append(f"  - Suggested additions: {', '.join(flag['suggested_additions'])}")
            if flag.get("current_tags_to_review"):
                lines.append(f"  - Current tags to review: {', '.join(flag['current_tags_to_review'])}")
            if flag.get("suggested_topics"):
                lines.append(f"  - Suggested topics: {', '.join(flag['suggested_topics'])}")
        lines.append("")

    lines.extend(["## Publications", ""])
    lines.append("The topic hints below are keyword-derived inventory metadata, not review flags.")
    lines.append("")
    for pub in inventory["publications"]:
        lines.append(f"### {pub['title']}")
        lines.append("")
        lines.append(f"- Slug: `{pub['slug']}`")
        lines.append(f"- Date: {pub['date']}")
        lines.append(f"- Current tags: {', '.join(pub['tags']) if pub['tags'] else '(none)'}")
        lines.append(f"- Keyword-derived topic hints: {', '.join(pub['suggested_topics']) if pub['suggested_topics'] else '(none)'}")
        lines.append("")

    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def build_inventory(content_dir: Path) -> dict[str, Any]:
    publications = read_publications(content_dir)
    counts = Counter(tag for pub in publications for tag in pub["tags"])
    by_topic: dict[str, list[str]] = defaultdict(list)
    for pub in publications:
        for tag in pub["tags"]:
            by_topic[tag].append(pub["slug"])

    return {
        "generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "content_dir": str(content_dir),
        "publication_count": len(publications),
        "topic_count": len(counts),
        "topics": [
            {"tag": tag, "count": count, "publications": sorted(by_topic[tag])}
            for tag, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        ],
        "publications": publications,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--content-dir", type=Path, default=DEFAULT_CONTENT_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    inventory = build_inventory(args.content_dir)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    json_path = args.output_dir / "publication_topics_inventory.json"
    md_path = args.output_dir / "publication_topics_inventory.md"
    json_path.write_text(json.dumps(inventory, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_markdown(md_path, inventory)

    flagged_count = sum(1 for pub in inventory["publications"] if pub["review_flags"])
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    print(f"Found {inventory['topic_count']} tags across {inventory['publication_count']} publications.")
    print(f"Flagged {flagged_count} publications for review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
