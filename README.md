# 32x-error-code

GitHub version of the Etched error-code table (`_Etched Error Code` spreadsheet),
rendered as a single HTML page: **[`index.html`](index.html)**.

Every error code is listed with its **version** and **original author**, organized
with the field names and enum values of the source of truth:
[`etched-ai/sw` → `host/system_test/error_codes/th_registry.yaml`](https://github.com/etched-ai/sw/blob/master/host/system_test/error_codes/th_registry.yaml)
(TH Error Code Specification v0.3 §7, §11.1).

Revision history is ordered oldest first (0.1 → 0.3), and codes are sorted
ascending within each stage.

## Contents

| File | What it is |
| --- | --- |
| `index.html` | Generated page: revision history, field definitions, `EC-` bitfield encoding, enum legends, the MLT/1X, L10 and L11 code tables, DRI ownership, source notes |
| `gen.py` | Generator — rebuilds `index.html` from the two snapshots below |
| `th_registry.yaml` | Snapshot of the source of truth from `etched-ai/sw@master` |
| `sheet.md` | Snapshot of the `_Etched Error Code` spreadsheet export the tables were built from |

## Regenerating

```sh
# refresh the source-of-truth snapshot
gh api repos/etched-ai/sw/contents/host/system_test/error_codes/th_registry.yaml \
  --jq .content | base64 -d > th_registry.yaml
# re-export the sheet over sheet.md, then
python3 gen.py
```

`gen.py` writes `index.html` next to itself; run it from the repo root
with `sheet.md` and `th_registry.yaml` beside it.

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
