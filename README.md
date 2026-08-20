# 32x-error-code

GitHub version of the Etched error-code table (`_Etched Error Code` spreadsheet),
rendered as a single HTML page and published on GitHub Pages:

**<https://fantastic-telegram-38n6vyw.pages.github.io/>**

The site is a *private* Pages site — visible to Etched org members with read access
to this repo, not to the public. The obfuscated hostname is how GitHub serves
private Pages; it does not change when the site rebuilds.

The page carries a **Download the source workbook** section at the top:
[`etched_error_code.xlsx`](etched_error_code.xlsx) is the editable copy of the
whole sheet, one worksheet per source tab.

Every error code is listed with its **version** and **original author**, organized
with the field names and enum values of the source of truth:
[`etched-ai/sw` → `host/system_test/error_codes/th_registry.yaml`](https://github.com/etched-ai/sw/blob/master/host/system_test/error_codes/th_registry.yaml)
(TH Error Code Specification v0.3 §7, §11.1).

Revision history is ordered oldest first (0.1 → 0.3), and codes are sorted
ascending within each stage.

## Contents

| File | What it is |
| --- | --- |
| `index.html` | Published page: download links, revision history, field definitions, `EC-` bitfield encoding, enum legends, the MLT/1X, L10 and L11 code tables, DRI ownership, source notes |
| `etched_error_code.xlsx` | The maintainable workbook — 9 sheets, one per source tab, with autofilters and frozen headers. Downloadable from the page |
| `data/*.csv` | The same 9 tabs as CSV, one file per tab, so git diffs a revision line by line instead of as a binary blob |
| `gen.py` | Generator — rebuilds `index.html`, the workbook and the CSVs from the two snapshots below |
| `th_registry.yaml` | Snapshot of the source of truth from `etched-ai/sw@master` |
| `sheet.md` | Snapshot of the `_Etched Error Code` spreadsheet export the tables were built from |
| `.nojekyll` | Serves `data/` and every file verbatim on Pages, no Jekyll processing |

### A note on the workbook

`etched_error_code.xlsx` is **regenerated from the sheet export**, not a copy of the
Drive binary — Drive's binary export is not reachable from this tooling
(`?format=xlsx` returns 401 without an interactive session). Content matches
`sheet.md` plus everything joined in from `th_registry.yaml`; cell formatting and
formulas from the original Google Sheet are not carried over. To capture the true
original instead, download it manually from the sheet
(File → Download → Microsoft Excel) and commit it over this file.

## Regenerating

```sh
# refresh the source-of-truth snapshot
gh api repos/etched-ai/sw/contents/host/system_test/error_codes/th_registry.yaml \
  --jq .content | base64 -d > th_registry.yaml
# re-export the sheet over sheet.md, then
python3 gen.py          # needs pyyaml + openpyxl
```

`gen.py` writes `index.html`, `etched_error_code.xlsx` and `data/*.csv` next to
itself; run it from the repo root with `sheet.md` and `th_registry.yaml` beside it.
Committing to `master` republishes the Pages site.

## How the two columns are derived

- **Version** — `version:` of the code in `th_registry.yaml` (all currently `1`;
  identity segments are immutable, so a change of meaning means a new code, not
  a version bump). **Doc Rev** is the spreadsheet revision that introduced the
  stage block.
- **Original Author** — DRI 1 of the code's primary test case, from the DRI tab
  of the sheet. Codes with no DRI listed fall back to the spec author
  (Ulysses Kao, who drafted revisions 0.1–0.3). Hover an author cell in
  `index.html` to see which basis was used.

## Coverage

356 codes: 82 MLT / 1X Module Test, 213 L10 Test, 61 L11 Test (draft).
132 of those rows resolve to a code in `th_registry.yaml`; the rest are marked
`sheet only` — present in the spreadsheet, not yet landed in the registry.
L11 is still in progress (per `#error-code-define`, 2026-08-19).

## Sources

- Source of truth — [`th_registry.yaml`](https://github.com/etched-ai/sw/blob/master/host/system_test/error_codes/th_registry.yaml)
- Spreadsheet — [_Etched Error Code](https://docs.google.com/spreadsheets/d/1zKcxEXyYFLAQkI0AnVtZnSQ7Z-sxGqzGBpc9-0qhrqk/edit?gid=1353335746)
- Discussion — Slack [#error-code-define](https://etchedai.slack.com/archives/C0B299EA7UK), [#tiger-error-code](https://etchedai.slack.com/archives/C0BMBRF327R)
- Spec docs — [Error code format definition](https://docs.google.com/document/d/19p0DrsD3fMRnOJajcB390yxke-aAjlfLj-Dbwmoktiw/edit), [error-event revision](https://docs.google.com/document/d/1rj0vtUVVIzQ_QMn-OBfLXeXAmq5mkb8G7hubHn5DQNI/edit)

The intent stated in `#error-code-define` is that the registry stays the source
of truth and documentation is generated from it — so regenerate this page rather
than hand-editing `index.html`.

## Roadmap — auth, in-place editing, versioning

The current model is: edit a snapshot, commit, regenerate, Pages republishes.
That already gives per-change authorship and history through git. The intended
next step is letting people change codes without a git checkout:

1. **Auth** — the Pages site is already gated to org members with repo read
   access. Write access needs a real identity, so an editor would sit behind
   GitHub OAuth (or the org SSO) rather than on the static site.
2. **Editing** — a form over the CSVs in `data/`, since they diff cleanly. Each
   save becomes a commit (or a PR) attributed to the signed-in user; the
   generator then rebuilds the page and workbook.
3. **Versioning** — the sheet's `Version` column is the document revision; each
   code's `version:` in `th_registry.yaml` is its own. Identity segments are
   immutable, so an edit that changes a code's *meaning* must allocate a new
   code rather than bump anything. That rule is what an editor has to enforce,
   and it is why the registry stays the source of truth: the site should end up
   generated from it, per the direction set in `#error-code-define`.

A static Pages site cannot write to the repo on its own — step 2 needs either a
GitHub App backend or a Pages-hosted editor calling the GitHub API with the
signed-in user's token.
