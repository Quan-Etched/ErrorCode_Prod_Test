# 32x-error-code refresh

Local refresh of the files in `32x-error-code`, generated from
`etched-ai/sw` `host/system_test/error_codes` at `65cf3520a606`.

| Catalog | File | Codes |
| --- | --- | --- |
| MLT / 1X | `MLT/mlt_th_registry.yaml` plus 1X-only leftovers in `th_registry.yaml` | 78 |
| L10 | `L10/l10_th_registry.yaml` | 228 |
| Common | `common_th_registry.yaml` | 19 |
| L11 | previous spreadsheet draft | 61 (not in system_test) |

`error_code_update_comparison.csv` is the field-level diff against
`32x-error-code/data/{mlt_1x,l10,l11}.csv`.

- `added` / `removed` — identity appeared or disappeared
- `moved` — same identity, different station table
- `updated` — a field changed (`field`, `old_value`, `new_value`)
- `retired` — registry marks `retired: true`
- `summary` — counts at the top of the file

L11 rows are carried forward unchanged. Identity segments stay immutable.
Regenerate with `python gen.py` from this directory.
URL : https://quan-etched.github.io/ErrorCode_Prod_Test/
