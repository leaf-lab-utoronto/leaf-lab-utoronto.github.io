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

# Run publication topic inventory script
python scripts/inventory_publication_topics.py

# Fetch/update publication abstracts
python scripts/update_publication_abstracts.py
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

**Publication pipeline:** Edit `publications.bib` → push to main → GitHub Actions workflow (`.github/workflows/import-publications.yml`) runs the `academic` importer and opens an automated PR. Abstracts can be enriched with `scripts/update_publication_abstracts.py` (hits arXiv, OpenAlex, OpenReview APIs).

**Deployment:** `.github/workflows/publish.yaml` builds with Hugo extended and deploys to GitHub Pages. `netlify.toml` is also configured but GitHub Pages is the active deployment target.

## Key Conventions

- Publication front matter uses MLA citation style (`params.yaml: cite_style: mla`).
- Author slugs must match exactly between `content/authors/<slug>/` and the `authors:` field in publication/event front matter.
- Static assets (fonts, PDFs, logos) live in `static/`; processed assets (SCSS, JS) live in `assets/`.
- The `public/` and `resources/` directories are gitignored build artifacts.
- `content/scratch/` holds draft/unpublished content.
- `metadata/` holds generated JSON/Markdown reports from the inventory script — don't hand-edit these.
