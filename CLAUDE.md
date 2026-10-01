# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A single-page HTML rendering of the Etched test-harness error-code table, published on
GitHub Pages (private to the org). Everything shipped — `index.html`, both `.xlsx`
workbooks, and every CSV under `data/` — is **generated output**. The only hand-edited
files are `gen.py` and the two snapshots it reads.

Read `README.md` first; it carries the provenance, the fidelity caveats on
`etched_error_code.xlsx`, and the roadmap. Don't duplicate that here.

## Commands

```sh
pip install pyyaml openpyxl   # the only dependencies
python gen.py                 # regenerates index.html, both workbooks, data/**.csv
```

`gen.py` must run from the repo root with `sheet.md` and `th_registry.yaml` beside it;
it resolves every path relative to its own location and writes in place. There is no
build system, no test suite, and no linter. The generator is the whole toolchain.

Every `open()` in `gen.py` pins `encoding='utf-8'`, and the `index.html` write pins
`newline='
'`. Both are load-bearing on Windows and must stay: without the encoding the
script dies decoding `sheet.md` under cp1252, and without the newline it emits CRLF and
every regeneration shows up as a whole-file diff. Keep them on any `open()` you add.

Refresh the source-of-truth snapshot before regenerating when the registry has moved:

```sh
gh api repos/etched-ai/sw/contents/host/system_test/error_codes/th_registry.yaml \
  --jq .content | base64 -d > th_registry.yaml
```

Verification is by `git diff` — the CSVs under `data/` exist precisely so a regeneration
diffs line by line instead of as an opaque binary blob. After any change to `gen.py`,
re-run it and read the diff; unexpected churn in the CSVs is the signal that something
broke. `index.html` and every CSV reproduce byte-for-byte from unchanged snapshots, so a
clean regeneration should leave them untouched. The trailing stdout lines (per-stage
counts, DRI entries, revision count) are the built-in sanity check — currently
`MLT/1X 82  L10 213  L11 61  total 356  in-registry 132`.

**The two `.xlsx` files are the exception: they always show as modified.** openpyxl stamps
a fresh build timestamp into `docProps/core.xml` on every save, so the binaries differ even
when every sheet is identical. Don't read that as a real change, and don't chase it —
`unzip` both and `diff -r` the extracted trees if you need to know whether the data moved.
Consider reverting them (`git checkout -- '*.xlsx'`) when a change didn't touch workbook
content, to keep the commit honest.

Committing to `master` republishes the Pages site.

## Architecture

`gen.py` is a **top-to-bottom script, not a module**: module-level statements do the
work, so importing it runs the entire pipeline and writes files. It has no `main()` and
no `if __name__ == '__main__'` guard. Read it in source order — the stages are
sequential and each depends on globals the previous one defined.

The pipeline is a join between two snapshots:

- **`sheet.md`** — a Drive markdown export of the `_Etched Error Code` spreadsheet.
  Parsed by `blocks()` into blank-line-separated grids, then `table()`. Blocks are
  addressed **positionally** (`BL[0]` is revision history, `BL[1]` MLT/1X, and so on)
  and named by `SOURCE_TABS`, because the markdown export carries no tab names. A
  re-export that adds, removes or reorders a grid silently shifts every downstream
  index — that is the most likely way this breaks.
- **`th_registry.yaml`** — the snapshot of the source of truth from `etched-ai/sw`,
  keyed by `error_code`.

`enrich()` is where the join happens, and it establishes the precedence rule the whole
page depends on: **the sheet's value wins where present, the registry fills the gaps.**
Codes carry an optional `-S<x>Q<y>` suffix encoding severity and quick action; only the
`TH-<BLOCK>-<NNNN>` prefix is the identity used for the registry lookup (`base_and_flags`).
A row whose base code is absent from the registry is kept and flagged `sheet only` rather
than dropped.

`collect()` de-duplicates codes repeated within one stage block, keeping the row with more
detail and recording the discard in `COLLISIONS` — which surfaces as the "Source data
notes" section rather than vanishing. Preserve that property when touching it.

Three output writers consume the joined records:

| Writer | Output | Contract |
| --- | --- | --- |
| `write_source_xlsx` / `write_source_csvs` | `etched_error_code.xlsx`, `data/source/` | **Verbatim mirror.** Same tabs, columns, rows, blanks. Never add, reorder or restyle here |
| `write_xlsx` / `write_csvs` | `etched_error_code_annotated.xlsx`, `data/` | Joined view, driven by `CODE_COLS`; `code_sheet()` drops columns empty for a given stage |
| the `html_out` f-string | `index.html` | Single self-contained file, `CSS` inlined, no assets, no JS |

Adding a field to the annotated workbook and CSVs means one entry in `CODE_COLS`; adding
it to the page means a cell in `code_table()` as well — the two are deliberately separate
and neither derives from the other.

## Rules that come from the domain, not the code

- **Identity segments are immutable.** Never renumber, never reuse a code. A change of
  meaning requires allocating a new code, not bumping a version. `version:` in the
  registry is per-code; the sheet's `Version` column is the document revision. These are
  different things and the page shows both (`Ver` vs `Doc Rev`).
- **Never hand-edit `index.html`, the workbooks, or the CSVs.** The stated direction in
  `#error-code-define` is that the registry stays the source of truth and documentation
  is generated from it. Fix `gen.py` or a snapshot, then regenerate.
- Bump `REPO_VERSION` in `gen.py` when publishing, and tag the commit to match.
- Enum legends (`CATEGORY`, `SEVERITY`, `QUICK_ACTION`) are transcribed from inline
  comments in `th_registry.yaml`. They are not parsed from it — if the registry gains a
  value, these dicts need the matching edit or the page renders a blank badge.
- `ETCH-\d+` strings in the Bugs column auto-link to Jira, and test-case names link to the
  DRI tab's PR when one is listed. Neither is configurable; both live in `bugs_html` /
  `cases_html`.
