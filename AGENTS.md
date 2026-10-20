# Repository Guidelines

## Project Structure & Module Organization

This LEAF Lab website uses Hugo extended 0.125.7 and Hugo Blox modules declared in `go.mod`.

- `content/`: Markdown pages with YAML front matter; publications use `publication/<slug>/index.md`, profiles use `authors/<slug>/_index.md`, and announcements live in `event/`.
- `layouts/`: Hugo template overrides, including publication pages and people grids.
- `assets/scss/`: custom styling in `template.scss` and responsive overrides in `custom.scss`.
- `static/`: fonts, logos, and downloadable files; publication images and videos stay beside their page.
- `config/_default/`: site configuration; `data/themes/` and `data/fonts/`: branding.
- `scripts/`: Python publication utilities; `metadata/`: generated inventory reports.

## Build, Test, and Development Commands

Run commands from the repository root with Hugo extended and Go installed:

- `hugo server`: preview with live reload at `http://localhost:1313/`. Check for an existing server before starting another.
- `hugo --gc --minify`: build production output into `public/`.
- `academic import publications.bib content/publication/ --compact`: import BibTeX using `academic==0.10.0`; review generated changes before committing.
- `python3 scripts/inventory_publication_topics.py`: regenerate topic reports without changing content.
- `python3 scripts/update_publication_abstracts.py --slug <slug>`: preview abstract enrichment; add `--write` to apply changes.

## Coding Style & Naming Conventions

Follow `.editorconfig`: UTF-8, LF, two-space indentation, final newlines, and no trailing whitespace except in Markdown. Match existing four-space Python indentation. No dedicated formatter or linter is configured.

Use lowercase, hyphenated content slugs. Author references must exactly match profile directory names. Preserve the site's light typography and responsive News grid. Store publication videos under `result-candidates/` and reference them through `result_media`; use H.264 MP4 with faststart.

Archive order: year descending, preprints before accepted, then date descending. Dates use `arxiv_date` or the earlier `acceptance_date`/`venue_date`; record sources.

## Testing Guidelines

No automated test suite or coverage target is configured. Validate changes with a Hugo build and browser checks at desktop and mobile widths. Check affected navigation, publication filters, author links, images, and videos. Capture visual snapshots serially. GitHub Actions builds and deploys pushes to `main`; publication import is manual-only.

## Commit & Pull Request Guidelines

History favors short, descriptive subjects such as `Add Peer-reviewed filter to publications page`; no strict prefix convention exists. Keep commits focused. PRs should explain the change, link relevant issues, report validation, and include screenshots for visual updates.

## Generated Files & Working Changes

Do not commit `public/` or `resources/`, hand-edit `metadata/`, or revert unrelated working changes. Review publication imports carefully to preserve manually curated front matter and media.
