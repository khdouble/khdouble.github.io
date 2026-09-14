# Migration notes — Google Sites → GitHub Pages

Source: `https://sites.google.com/site/khdouble2/` (Home / RESEARCH / CONSULTING / LINKS)
Target: `https://khdouble.github.io/` (Home / Research / Projects / Links)

Content carried over in full: **53** research entries, **29** commissioned projects,
**13** external links (15 on the old site, two of which were dead and dropped).

## Links that were already broken on the old site

These were verified as genuinely dead, not merely slow or bot-blocked.

| Old link | Status | What was done |
|:--|:--|:--|
| `goog_1207722160` | Google Sites authoring bug — the BOK bulletin title was split across two anchors, one pointing at a non-URL | Merged into one entry, now served locally |
| `bok.or.kr/down.search?…1462328171098.pdf` (apartment bulletin) | 404 | `files/wp/apartment-price-diffusion-korea-bok-bulletin.pdf` |
| `imer.bok.or.kr/…bok_13-26.pdf` (Black Box WP version) | host retired | `files/wp/black-box-korean-economy-bok-wp-2013-26.pdf` |
| `eri.bok.or.kr/…bok_14-29_F.pdf` (Hysteresis WP) | host retired | `files/wp/hysteresis-korean-labor-market-bok-wp-2014-29.pdf` |
| `tp.or.kr/…down.do` (TCFD report) | HTTP 400 | `files/wp/tcfd-pension-fund-response-korea.pdf` |
| `165.132.79.212/kje/…` (한국경제학보) | worked, but a bare IP address | `files/wp/search-index-macro-forecasting-kje.pdf` |
| `imer.bok.or.kr/imer_eng/…` (Links page) | host retired | `https://www.bok.or.kr/imer/main/main.do` |
| `bok.or.kr/eng/engMain.action` (Links page) | 404 | `https://www.bok.or.kr/eng/main/main.do` |
| `research.stlouisfed.org/fred2/` | redirect | `https://fred.stlouisfed.org/` |
| `econ.rutgers.edu` | redirect | `https://economics.rutgers.edu/` |
| `cyhome.cyworld.com/…` | service shut down | dropped |
| `netec.mcc.ac.uk/jokec.html` (JokEc) | host gone | dropped |
| `pkarchive.org` | no response | `https://paulkrugman.substack.com/` |
| `docs.google.com/viewer?…` (legacy CV attachment) | stale Google Sites viewer | `files/cv-hyunhak-kim.pdf` |
| Home footer "Teaching" link | pointed at the Consulting page | removed (no Teaching page in this version) |

## Google Drive attachments

All 21 Drive links on the old site were checked anonymously (i.e. as a visitor sees them):

- **12 were public** and are now served from `files/`.
- **8 return a hard 404** — the files are deleted from Drive, so these links are
  broken on the live Google Sites page today. Five were recovered from local
  archives; three could not be:

  | Supplement | Recovered |
  |:--|:--|
  | Black Box — Appendices | ✅ `files/wp/black-box-korean-economy-appendices.pdf` |
  | Consumer Credit SOM — Appendix | ✅ `files/wp/consumer-credit-panel-som-appendix.pdf` |
  | Systemic Risk — Appendix | ✅ `files/wp/systemic-risk-consumer-credit-network-appendix.pdf` |
  | Combining Point & Density — R codes | ❌ not found |
  | Black Box — MATLAB codes | ❌ not found |
  | House Price Diffusion — Gauss codes | ❌ not found |
  | Monetary Policy Disaggregate — MATLAB code | ❌ not found |
  | Consumer Credit SOM — R codes | ❌ not found |

- **1 requires sign-in** (HTTP 401), so it was never publicly readable:
  "Financial Development and Income and Wealth Inequalities". It is listed
  without a link until a public copy is available.

## Rutgers code archives (Norman Swanson's page)

`econweb.rutgers.edu/nswanson/...` now redirects to the department root, so five
links died with it: three MATLAB `.zip` archives, the Factor-MIDAS Online Appendix,
and the Mining Big Data WP version. They are dropped from the site.

Local replacements exist for two of the three code archives but were **not** added:

- `Kim_Swanson_JoE2014.zip` (8.2 MB) — 96% of it is a bundled third-party
  MATLAB econometrics toolbox, which raises redistribution questions.
- `MiningBigData.ziP` (49.7 MB) — the author's own code, but large enough to
  weigh on the repository and GitHub Pages bandwidth.

Decide case by case whether to publish these, trim them to first-party code, or
host them elsewhere.

## Open items

- `github.com/khdouble/mpb-statement-forecasting`, linked as **[CODE]** from
  "Do Central Bank Statements Forecast Policy?", returns **404 to anonymous
  visitors** — the repository appears to be private. Make it public or drop the link.
- Publication years are not stored in `data/publications.yml`; entries keep the
  volume/issue detail exactly as the old site listed it.
