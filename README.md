# khdouble.github.io

Personal academic site for Hyun Hak Kim, migrated from the old Google Sites page
(`sites.google.com/site/khdouble2`). Built with [Quarto](https://quarto.org).

## How to update

Content lives in `data/*.yml`. `build.py` turns it into `research.qmd` and
`projects.qmd`; Quarto runs `build.py` automatically as a pre-render step.

```bash
quarto preview        # local preview at http://localhost:4200
quarto render         # writes docs/ , which is what GitHub Pages serves
```

**Adding a publication** — append a block to the right section of
`data/publications.yml` and re-render:

```yaml
  - title: "Title of the paper"
    authors: ["Co Author"]        # co-authors only; omit if sole-authored
    venue: "Journal Name"
    detail: "12(3):45-67"         # or "submitted" / "Forthcoming (2026)"
    lang: ko                      # only when the paper is in Korean
    url: "https://doi.org/..."    # or "files/wp/local-file.pdf"
    extras:
      - {label: "Appendix", href: "files/wp/....pdf"}
```

**Adding a project** — append a block to `data/projects.yml`. `start` (YYYY-MM)
drives the ordering; `period` is what gets shown.

Do **not** hand-edit `research.qmd` or `projects.qmd` — they are regenerated on
every render and your changes would be lost.

## Layout

| Path | What it is |
|:--|:--|
| `index.qmd`, `links.qmd` | hand-written pages |
| `research.qmd`, `projects.qmd` | **generated** by `build.py` |
| `data/publications.yml` | 53 entries: journal, chapter, report, WP, WIP, translations |
| `data/projects.yml` | 29 commissioned research projects |
| `files/` | CV and working-paper PDFs served directly from the repo |
| `styles.scss`, `_quarto.yml` | theme and site config |
| `docs/` | render output — this is the GitHub Pages source |

## Deployment

GitHub Pages is served from the `main` branch, `/docs` folder. `.nojekyll` keeps
Jekyll from swallowing Quarto's `site_libs/` directory. Commit `docs/` along with
the source whenever content changes.

## Notes on migrated content

- Published journal articles link to the publisher/DOI page only; PDFs in `files/`
  are working papers, preprints, appendices and reports.
- Several links on the old site were already dead and were repaired or dropped
  during migration — see `MIGRATION.md`.
