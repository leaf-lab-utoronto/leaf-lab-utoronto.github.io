# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the LEAF Laboratory academic research group website, built with Hugo (v0.125.7 extended) and the [Hugo Blox Builder](https://hugoblox.com/) (formerly Wowchemy). It deploys to GitHub Pages via GitHub Actions.

## Common Commands

```bash
# Serve locally with live reload
hugo server

# Build for production
hugo --gc --minify

# Import publications from BibTeX (requires academic CLI tool)
academic import publications.bib content/publication/ --compact

# Run publication topic inventory script (read-only, writes to metadata/)
python scripts/inventory_publication_topics.py

# Dry-run abstract fetcher — shows what would change, does not write files
python scripts/update_publication_abstracts.py

# Actually write fetched abstracts to content/publication/*/index.md
python scripts/update_publication_abstracts.py --write

# Update a single publication by slug
python scripts/update_publication_abstracts.py --write --slug rhinehart2021contingencies
```

## Scripts

### `scripts/inventory_publication_topics.py`

**Read-only.** Reads `content/publication/*/index.md` front matter and writes two report files:
- `metadata/publication_topics_inventory.json`
- `metadata/publication_topics_inventory.md`

Does not touch any content files. Useful for auditing tag coverage. It applies keyword heuristics (defined in `TOPIC_RULES` at the top of the script) to title + abstract + publication venue text and flags publications that appear to be missing topic tags. Flags only fire for the subset of topics listed in `AUTO_REVIEW_TOPICS` and require at least two keyword matches to reduce noise.

### `scripts/update_publication_abstracts.py`

**Writes to `content/publication/*/index.md`** when run with `--write`; dry-run by default.

Fills in the `abstract:` field in publication front matter by querying external APIs in priority order:
1. **OpenAlex** (by DOI if present, then by title)
2. **OpenReview** (if an OpenReview URL is in the front matter)
3. **arXiv** (by arXiv ID extracted from any front-matter URL, then by title search)
4. **Source page / Figshare** (scrapes `url_doi` or `url_project` for `<meta>` abstract tags)
5. **PDF** (downloads `url_pdf` and runs `pdftotext` — requires `pdftotext` installed)

Also records a `paper_versions:` block in front matter with provenance metadata (source, URL, retrieval timestamp). Skips publications that already have an abstract unless `--force` is passed. Useful flags:
- `--slug <slug>` — process only one publication
- `--limit N` — cap at N publications
- `--force` — overwrite existing abstracts
- `--reflow-existing` — rewrap existing abstract text without network lookup

## Result Videos

Publications can display an inline result video via the `result_media` front matter block:

```yaml
result_media:
  src: result-candidates/my-paper-snippet.mp4
  type: video
  alt: Brief description of what the video shows
```

The video file lives in `content/publication/<slug>/result-candidates/` alongside the `index.md`. Use `result-candidates/` as a staging area — the file that gets wired up in `result_media.src` is the one that ships.

**Encoding convention** (match the autoworld-snippet.mp4 reference):
- Container: MP4
- Video codec: H.264 (`libx264`), `yuv420p` pixel format
- CRF: 23, preset: slow
- Audio: stripped (`-an`)
- Faststart: enabled (`-movflags +faststart`) so the video plays before fully downloaded
- Length: ~30–60 seconds; target file size ~5–15 MB

**ffmpeg one-liner to cut and encode a clip:**
```bash
ffmpeg -ss HH:MM:SS -to HH:MM:SS -i input.mp4 \
  -c:v libx264 -crf 23 -preset slow -pix_fmt yuv420p -an -movflags +faststart \
  content/publication/<slug>/result-candidates/<slug>-snippet.mp4 -y
```

**Note:** If ffmpeg fails with a missing `libx265.215.dylib` error, the x265 brew package may have updated ahead of ffmpeg. Fix with:
```bash
ln -s /usr/local/Cellar/x265/4.1/lib/libx265.215.dylib /usr/local/opt/x265/lib/libx265.215.dylib
```

## Architecture

**Config:** Split across `config/_default/` in YAML files — `hugo.yaml` (core settings), `params.yaml` (site params, theme/font selection), `menus.yaml` (nav), `module.yaml` (Hugo Blox dependencies), `languages.yaml`.

**Theme:** No `themes/` directory. The base theme comes from Hugo Blox modules (`blox-bootstrap/v5`, `blox-plugin-netlify`, `blox-plugin-decap-cms`) fetched as Go modules (`go.mod`). Custom theming is entirely data-driven:
- `data/themes/theme_leaf_lab_v2.toml` — brand colors (primary: `#1E3765` U of T blue)
- `data/fonts/font_leaf_lab.toml` — Trade Gothic font throughout
- `assets/scss/template.scss` — main custom styles (navbar, people grid, publication thumbnails, homepage sections)
- `assets/scss/custom.scss` — mobile/responsive overrides

**Layouts:** `layouts/` contains targeted overrides of Hugo Blox templates. Key overrides:
- `layouts/partials/blocks/people.html` — team grid display
- `layouts/partials/blocks/collection.html` — publication/event listings
- `layouts/publication/single.html` — individual publication pages
- `layouts/partials/components/footers/minimal.html` — footer with U of T logos and land acknowledgement

**Content types:**
- `content/publication/*/index.md` — each publication is a directory with `index.md` (YAML front matter), `cite.bib`, `featured.jpg/png`, optional PDFs. BibTeX import via the `academic` CLI tool populates these.
- `content/authors/*/` — lab member profiles with `_index.md` and `avatar.jpg`
- `content/event/*/` — news/announcements

**Publication pipeline:** Edit `publications.bib` → run `academic import publications.bib content/publication/ --compact` locally → commit the generated `content/publication/<slug>/` directories. The GitHub Actions workflow (`.github/workflows/import-publications.yml`) is set to manual-only (`workflow_dispatch`) and does not run on push. Abstracts can be enriched with `scripts/update_publication_abstracts.py --write` (hits arXiv, OpenAlex, OpenReview APIs).

**Deployment:** `.github/workflows/publish.yaml` builds with Hugo extended and deploys to GitHub Pages. `netlify.toml` is also configured but GitHub Pages is the active deployment target.

## Key Conventions

- Publication front matter uses MLA citation style (`params.yaml: cite_style: mla`).
- Author slugs must match exactly between `content/authors/<slug>/` and the `authors:` field in publication/event front matter.
- Static assets (fonts, PDFs, logos) live in `static/`; processed assets (SCSS, JS) live in `assets/`.
- The `public/` and `resources/` directories are gitignored build artifacts.
- `content/scratch/` holds draft/unpublished content.
- `metadata/` holds generated JSON/Markdown reports from the inventory script — don't hand-edit these.
