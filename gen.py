#!/usr/bin/env python3
"""Rebuild the 32x-error-code tables from host/system_test/error_codes.

The published snapshot in 32x-error-code was driven by an old sheet export
plus one th_registry.yaml. The source of truth is now four registries:

- th_registry.yaml          (1X, being drained)
- MLT/mlt_th_registry.yaml  (chip / module)
- L10/l10_th_registry.yaml  (L10 server)
- common_th_registry.yaml   (cross-station)

Codes are emitted once per owning catalog. A 1X record is included only when
its identity is not already in MLT, L10, or common. L11 stays the spreadsheet
draft: system_test has no L11 registry.

Also writes error_code_update_comparison.csv against the previous joined
tables in 32x-error-code/data.
"""

import csv
import html
import os
import re
import shutil
import subprocess

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SW = os.path.abspath(os.path.join(HERE, "..", "..", "Etched_SW", "sw"))
# Pinned relative to this folder's sibling layout: Error_Code/ and Etched_SW/.
# Fall back to the snapshots already in this repo when that layout is absent.
SW_CODES = os.path.join(SW, "host", "system_test", "error_codes")
if not os.path.isdir(SW_CODES):
    SW_CODES = HERE
OLD_CANDIDATES = [
    os.path.abspath(os.path.join(HERE, "..", "32x-error-code")),
    os.path.abspath(os.path.join(HERE, "..", "Error_Code", "32x-error-code")),
]
OLD = next((path for path in OLD_CANDIDATES if os.path.isdir(path)), HERE)

REGISTRY_FILES = {
    "1x": os.path.join(SW_CODES, "th_registry.yaml"),
    "mlt": os.path.join(SW_CODES, "MLT", "mlt_th_registry.yaml"),
    "l10": os.path.join(SW_CODES, "L10", "l10_th_registry.yaml"),
    "common": os.path.join(SW_CODES, "common_th_registry.yaml"),
}

STAGE = {
    "mlt": "MLT / 1X Module Test",
    "l10": "L10 Test",
    "common": "Common",
    "l11": "L11 Test",
    "1x": "MLT / 1X Module Test",
}

CATEGORY = {
    0: "CATEGORY_NONE",
    1: "CATEGORY_NETWORK",
    2: "CATEGORY_STORAGE",
    3: "CATEGORY_MEMORY",
    4: "CATEGORY_AUTH",
    5: "CATEGORY_CONFIG",
    6: "CATEGORY_HARDWARE",
    7: "CATEGORY_SOFTWARE",
    8: "CATEGORY_API",
    9: "CATEGORY_RESOURCE",
    10: "CATEGORY_SECURITY",
    11: "CATEGORY_DATA",
    12: "CATEGORY_INTERNAL",
}
SEVERITY = {
    0: "ERROR_NONE",
    1: "ERROR_MONITOR",
    2: "ERROR_ISOLATE",
    3: "ERROR_UNKNOWN",
    4: "ERROR_TRIAGE",
    5: "ERROR_CONFIG",
    6: "ERROR_RESET",
}
QUICK_ACTION = {
    0: "QA_NO_ACT",
    1: "QA_COLD_REBOOT",
    2: "QA_WARM_REBOOT",
    3: "QA_SOFT_POWER_OFF",
    4: "QA_HARD_SHUTDOWN",
    5: "QA_DISABLE_COMPONENT",
    6: "QA_RETRY",
    7: "QA_HOT_REMOVE",
    8: "QA_HOT_SWITCH",
    9: "QA_ESCALATE",
}

SUFFIX = re.compile(r"^(TH-[A-Z0-9]+-\d+)(?:-S(\d)Q(\d))?$")
SPEC_AUTHOR = "Ulysses Kao"
DOC_REV_NEW = "0.4"

JOINED_COLS = [
    "Error Code ID",
    "Packed",
    "Version",
    "Doc Rev",
    "Original Author",
    "Author Basis",
    "DRI 2",
    "Name",
    "Message",
    "Severity",
    "Severity Name",
    "Quick Action",
    "Quick Action Name",
    "Quick Action (sheet)",
    "Recover / Troubleshooting Procedure",
    "Error Type",
    "Category",
    "Category Name",
    "Component",
    "Test Case",
    "Source",
    "Possible Root Cause",
    "Bugs",
    "Owner",
    "Since",
    "Disposition",
    "Retryable",
    "In th_registry.yaml",
    "Merged Duplicate",
    "Doc URL",
]

DIFF_FIELDS = [
    "full_id",
    "name",
    "message",
    "severity",
    "quick_action",
    "category",
    "component",
    "test_cases",
    "disposition",
    "retryable",
    "owner",
    "since",
    "doc_url",
    "version",
    "packed",
    "procedure",
    "registry_status",
]


def norm(value):
    return " ".join(str(value or "").split())


def parse_id(code):
    code = (code or "").strip()
    match = SUFFIX.match(code)
    if not match:
        return code, None, None
    severity = int(match.group(2)) if match.group(2) else None
    quick = int(match.group(3)) if match.group(3) else None
    return match.group(1), severity, quick


def packed_of(base, category, severity, quick_action):
    sequence = int(base.rsplit("-", 1)[1])
    return (
        (0x1 << 28)
        | (int(category) << 24)
        | (int(severity) << 20)
        | (int(quick_action) << 16)
        | sequence
    )


def load_yaml(path):
    with open(path, encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def sw_sha():
    if SW_CODES == HERE:
        return "local"
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short=12", "HEAD"],
            cwd=SW,
            text=True,
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def copy_file(src, dst):
    if os.path.normcase(os.path.abspath(src)) == os.path.normcase(os.path.abspath(dst)):
        return
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy(src, dst)


def load_dri():
    path = os.path.join(OLD, "data", "dri_ownership.csv")
    dri = {}
    with open(path, newline="", encoding="utf-8-sig") as handle:
        for row in csv.DictReader(handle):
            name = (row.get("Test Case") or "").strip()
            if name:
                dri[name] = row
    return dri


def author_for(test_cases, dri):
    for test_case in test_cases:
        hit = dri.get(test_case) or dri.get(
            test_case if test_case.endswith("TestCase") else test_case + "TestCase"
        )
        if hit and (hit.get("DRI 1") or "").strip():
            return hit["DRI 1"].strip(), f"DRI 1 of {test_case}"
    return SPEC_AUTHOR, "spec author (no DRI listed)"


def procedure_of(entry):
    parts = []
    for action in entry.get("repair_actions") or []:
        if isinstance(action, dict):
            text = action.get("action") or ""
        else:
            text = str(action)
        text = norm(text)
        if text:
            parts.append(text)
    return " ".join(parts)


def causes_of(entry):
    return " | ".join(norm(item) for item in (entry.get("probable_causes") or []) if norm(item))


def from_entry(entry, catalog, stage):
    base = entry["error_code"].strip()
    severity = int(entry["severity"])
    quick = int(entry["quick_action"])
    category = int(entry["category"])
    cases = [str(item).strip() for item in (entry.get("test_cases") or []) if str(item).strip()]
    return {
        "catalog": catalog,
        "stage": stage,
        "base": base,
        "full_id": f"{base}-S{severity}Q{quick}",
        "name": entry.get("name") or "",
        "message": norm(entry.get("description") or ""),
        "severity": severity,
        "quick_action": quick,
        "category": category,
        "component": entry.get("component") or "",
        "test_cases": cases,
        "disposition": entry.get("disposition") or "",
        "retryable": bool(entry.get("retryable")),
        "owner": entry.get("owner") or "",
        "since": entry.get("since") or "",
        "doc_url": entry.get("doc_url") or "",
        "version": entry.get("version", 1),
        "packed": packed_of(base, category, severity, quick),
        "procedure": procedure_of(entry),
        "probable_causes": causes_of(entry),
        "retired": bool(entry.get("retired")),
        "in_registry": True,
    }


def load_new():
    catalogs = {name: load_yaml(path) for name, path in REGISTRY_FILES.items()}
    owned = set()
    for name in ("mlt", "l10", "common"):
        owned.update(entry["error_code"] for entry in catalogs[name])
    rows = []
    for catalog in ("mlt", "l10", "common"):
        for entry in catalogs[catalog]:
            rows.append(from_entry(entry, catalog, STAGE[catalog]))
    for entry in catalogs["1x"]:
        if entry["error_code"] not in owned:
            rows.append(from_entry(entry, "1x", STAGE["1x"]))
    return rows


def load_old_codes():
    rows = []
    for filename, stage in (
        ("mlt_1x.csv", STAGE["mlt"]),
        ("l10.csv", STAGE["l10"]),
        ("l11.csv", STAGE["l11"]),
    ):
        path = os.path.join(OLD, "data", filename)
        with open(path, newline="", encoding="utf-8-sig") as handle:
            for raw in csv.DictReader(handle):
                full = (raw.get("Error Code ID") or "").strip()
                if not full:
                    continue
                base, severity, quick = parse_id(full)
                if severity is None and (raw.get("Severity") or "").strip().isdigit():
                    severity = int(raw["Severity"])
                if quick is None and (raw.get("Quick Action") or "").strip().isdigit():
                    quick = int(raw["Quick Action"])
                packed = (raw.get("Packed") or "").strip()
                cases = [
                    part.strip()
                    for part in (raw.get("Test Case") or "").split(",")
                    if part.strip()
                ]
                rows.append(
                    {
                        "stage": stage,
                        "base": base,
                        "full_id": full,
                        "name": raw.get("Name") or "",
                        "message": norm(raw.get("Message") or ""),
                        "severity": severity,
                        "quick_action": quick,
                        "category": int(raw["Category"])
                        if (raw.get("Category") or "").strip().isdigit()
                        else None,
                        "component": raw.get("Component") or "",
                        "test_cases": cases,
                        "disposition": raw.get("Disposition") or "",
                        "retryable": (raw.get("Retryable") or "").strip(),
                        "owner": raw.get("Owner") or "",
                        "since": raw.get("Since") or "",
                        "doc_url": raw.get("Doc URL") or "",
                        "version": raw.get("Version") or "",
                        "packed": int(packed) if packed.isdigit() else None,
                        "procedure": norm(
                            raw.get("Recover / Troubleshooting Procedure") or ""
                        ),
                        "in_registry": (raw.get("In th_registry.yaml") or "").strip().lower()
                        == "yes",
                        "doc_rev": raw.get("Doc Rev") or "",
                        "author": raw.get("Original Author") or "",
                        "author_basis": raw.get("Author Basis") or "",
                        "bugs": raw.get("Bugs") or "",
                        "error_type": raw.get("Error Type") or "",
                        "root_cause": raw.get("Possible Root Cause") or "",
                        "quick_action_txt": raw.get("Quick Action (sheet)") or "",
                        "dri2": raw.get("DRI 2") or "",
                        "source": raw.get("Source") or "",
                    }
                )
    return rows


def index_by_stage(rows):
    out = {}
    for row in rows:
        out[(row["stage"], row["base"])] = row
    return out


def stages_for(rows):
    found = {}
    for row in rows:
        found.setdefault(row["base"], {})[row["stage"]] = row
    return found


def same_text(left, right):
    return norm(left) == norm(right)


def cases_key(cases):
    return tuple(sorted(cases))


def field_changes(old, new):
    changes = []

    def add(field, old_value, new_value):
        if norm(old_value) == norm(new_value):
            return
        changes.append((field, "" if old_value is None else old_value, new_value))

    add("full_id", old["full_id"], new["full_id"])
    add("name", old["name"], new["name"])
    add("message", old["message"], new["message"])
    add("severity", old["severity"], new["severity"])
    add("quick_action", old["quick_action"], new["quick_action"])
    add("category", old["category"], new["category"])
    add("component", old["component"], new["component"])
    if cases_key(old["test_cases"]) != cases_key(new["test_cases"]):
        add(
            "test_cases",
            ", ".join(old["test_cases"]),
            ", ".join(new["test_cases"]),
        )
    add("disposition", old["disposition"], new["disposition"])
    old_retry = norm(old["retryable"]).lower()
    new_retry = "true" if new["retryable"] else "false"
    if old_retry in ("", "none") and new_retry:
        add("retryable", old["retryable"], new_retry)
    elif old_retry and old_retry != new_retry:
        add("retryable", old["retryable"], new_retry)
    add("owner", old["owner"], new["owner"])
    add("since", old["since"], new["since"])
    add("doc_url", old["doc_url"], new["doc_url"])
    add("version", old["version"], new["version"])
    if old["packed"] is not None and old["packed"] != new["packed"]:
        add("packed", old["packed"], new["packed"])
    if old["procedure"] and not same_text(old["procedure"], new["procedure"]):
        add("procedure", old["procedure"], new["procedure"])
    if not old["in_registry"]:
        add("registry_status", "sheet only", "in registry")
    if new["retired"]:
        add("retired", "", "true")
    return changes


def summary_text(row):
    cases = ", ".join(row["test_cases"])
    return (
        f"{row.get('name') or row['full_id']} | {row['full_id']} | "
        f"{row['message']} | cases: {cases} | {row.get('component', '')}"
    )


def build_diff(old_rows, new_rows):
    old_ix = index_by_stage(old_rows)
    new_ix = index_by_stage(new_rows)
    old_stages = stages_for(old_rows)
    new_stages = stages_for(new_rows)
    diffs = []
    handled = set()

    def emit(change, catalog, stage, base, name, full_old, full_new, field, old_value, new_value):
        diffs.append(
            {
                "change_type": change,
                "catalog": catalog,
                "stage": stage,
                "error_code": base,
                "name": name,
                "full_id_old": full_old,
                "full_id_new": full_new,
                "field": field,
                "old_value": old_value,
                "new_value": new_value,
            }
        )

    def emit_fields(old, new, change="updated"):
        for field, old_value, new_value in field_changes(old, new):
            kind = "retired" if field == "retired" else change
            emit(
                kind,
                new["catalog"],
                new["stage"],
                new["base"],
                new["name"],
                old["full_id"],
                new["full_id"],
                field,
                old_value,
                new_value,
            )

    bases = set(old_stages) | set(new_stages)
    for base in sorted(bases):
        if base.startswith("EC-"):
            continue
        old_map = old_stages.get(base, {})
        new_map = new_stages.get(base, {})
        old_set = set(old_map)
        new_set = set(new_map)
        if len(old_set) == 1 and len(new_set) == 1 and old_set != new_set:
            old = next(iter(old_map.values()))
            new = next(iter(new_map.values()))
            emit(
                "moved",
                new["catalog"],
                new["stage"],
                base,
                new["name"],
                old["full_id"],
                new["full_id"],
                "stage",
                old["stage"],
                new["stage"],
            )
            emit_fields(old, new)
            handled.add((old["stage"], base))
            handled.add((new["stage"], base))
            continue
        for stage in sorted(new_set - old_set):
            new = new_map[stage]
            if not old_map:
                kind = "retired" if new["retired"] else "added"
                emit(
                    kind,
                    new["catalog"],
                    stage,
                    base,
                    new["name"],
                    "",
                    new["full_id"],
                    "code",
                    "",
                    summary_text(new),
                )
            else:
                emit(
                    "added",
                    new["catalog"],
                    stage,
                    base,
                    new["name"],
                    "",
                    new["full_id"],
                    "stage",
                    "previously in " + ", ".join(sorted(old_set)),
                    stage,
                )
            handled.add((stage, base))
        for stage in sorted(old_set - new_set):
            old = old_map[stage]
            still = ", ".join(sorted(new_set))
            emit(
                "removed",
                "",
                stage,
                base,
                old.get("name") or "",
                old["full_id"],
                "",
                "code" if not still else "stage",
                summary_text(old) if not still else stage,
                "" if not still else "still listed in " + still,
            )
            handled.add((stage, base))

    for key, new in sorted(new_ix.items()):
        if key in handled or key not in old_ix:
            continue
        emit_fields(old_ix[key], new)

    return diffs


def dri2_of(test_cases, dri):
    for test_case in test_cases:
        hit = dri.get(test_case) or dri.get(
            test_case if test_case.endswith("TestCase") else test_case + "TestCase"
        )
        if hit and (hit.get("DRI 2") or "").strip():
            return hit["DRI 2"].strip()
    return ""


def error_type_of(row):
    name = CATEGORY.get(row["category"], "")
    return name.removeprefix("CATEGORY_").replace("_", " ").title()


def annotate(new_rows, old_rows, dri):
    old_ix = index_by_stage(old_rows)
    for row in new_rows:
        old = old_ix.get((row["stage"], row["base"]))
        if old is None:
            # A moved code keeps the author / bugs from its previous stage.
            old = next(
                (item for item in old_rows if item["base"] == row["base"]),
                None,
            )
        author, basis = author_for(row["test_cases"], dri)
        row["author"] = author
        row["author_basis"] = basis
        row["doc_rev"] = old["doc_rev"] if old and old.get("doc_rev") else DOC_REV_NEW
        row["bugs"] = old.get("bugs", "") if old else ""
        row["dri2"] = (old.get("dri2") if old else "") or dri2_of(row["test_cases"], dri)
        row["error_type"] = (old.get("error_type") if old else "") or error_type_of(row)
        row["source"] = (old.get("source") if old else "") or row["stage"]
        row["root_cause"] = (old.get("root_cause") if old else "") or row["probable_causes"]
        row["quick_action_txt"] = (
            (old.get("quick_action_txt") if old else "")
            or QUICK_ACTION.get(row["quick_action"], "").removeprefix("QA_")
        )


def joined_row(row):
    category_name = CATEGORY.get(row["category"], "")
    return [
        row["full_id"],
        row["packed"],
        row["version"],
        row["doc_rev"],
        row["author"],
        row["author_basis"],
        row.get("dri2") or "",
        row["name"],
        row["message"],
        row["severity"],
        SEVERITY.get(row["severity"], ""),
        row["quick_action"],
        QUICK_ACTION.get(row["quick_action"], ""),
        row.get("quick_action_txt") or "",
        row["procedure"],
        row.get("error_type") or "",
        row["category"],
        category_name,
        row["component"],
        ", ".join(row["test_cases"]),
        row.get("source") or row["stage"],
        row.get("root_cause") or "",
        row["bugs"],
        row["owner"],
        row["since"],
        row["disposition"],
        row["retryable"],
        "yes" if row["in_registry"] else "no",
        "yes" if row.get("dup") else "",
        row["doc_url"],
    ]


def drop_empty_columns(header, body):
    keep = [
        index
        for index, _name in enumerate(header)
        if any(str(row[index] if index < len(row) else "").strip() for row in body)
    ]
    if not keep:
        return header, body
    return (
        [header[index] for index in keep],
        [[row[index] if index < len(row) else "" for index in keep] for row in body],
    )


def write_csv(path, header, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)


def write_tables(new_rows):
    groups = {
        "mlt_1x": [row for row in new_rows if row["catalog"] in ("mlt", "1x")],
        "l10": [row for row in new_rows if row["catalog"] == "l10"],
        "common": [row for row in new_rows if row["catalog"] == "common"],
    }
    for name, rows in groups.items():
        rows.sort(key=lambda row: row["full_id"])
        header, body = drop_empty_columns(JOINED_COLS, [joined_row(row) for row in rows])
        write_csv(os.path.join(HERE, "data", name + ".csv"), header, body)
    copy_file(
        os.path.join(OLD, "data", "l11.csv"),
        os.path.join(HERE, "data", "l11.csv"),
    )
    for name in ("mlt_1x.csv", "l10.csv", "l11.csv", "suite_run_log.csv", "revision_history.csv"):
        src = os.path.join(OLD, "data", "source", name)
        if os.path.isfile(src):
            copy_file(src, os.path.join(HERE, "data", "source", name))


def write_static():
    for name in (
        "dri_ownership.csv",
        "field_definitions.csv",
        "error_id_encoding.csv",
        "source_data_notes.csv",
    ):
        copy_file(os.path.join(OLD, "data", name), os.path.join(HERE, "data", name))
    for name in ("dri_ownership.csv", "field_definitions.csv"):
        src = os.path.join(OLD, "data", "source", name)
        if os.path.exists(src):
            copy_file(src, os.path.join(HERE, "data", "source", name))
    revisions = []
    with open(os.path.join(OLD, "data", "revision_history.csv"), newline="", encoding="utf-8-sig") as handle:
        revisions = list(csv.DictReader(handle))
    sha = sw_sha()
    if sha == "local":
        # These snapshots were taken from etched-ai/sw at this commit.
        sha = "65cf3520a606"
    if SW_CODES == HERE:
        marker = "Refresh from host/system_test/error_codes at sw@"
        for row in reversed(revisions):
            comment = row.get("Comment") or ""
            if comment.startswith(marker) and not comment.endswith("@local"):
                sha = comment[len(marker):]
                break
    refresh = f"Refresh from host/system_test/error_codes at sw@{sha}"
    already = any((row.get("Comment") or "") == refresh for row in revisions)
    if not already:
        revisions.append(
            {
                "Version": DOC_REV_NEW,
                "Comment": refresh,
                "Author": "supercomputing-sw",
            }
        )
    write_csv(
        os.path.join(HERE, "data", "revision_history.csv"),
        ["Version", "Comment", "Author"],
        [[row["Version"], row["Comment"], row["Author"]] for row in revisions],
    )
    legends = (
        [["category", key, value] for key, value in sorted(CATEGORY.items())]
        + [["severity", key, value] for key, value in sorted(SEVERITY.items())]
        + [["quick_action", key, value] for key, value in sorted(QUICK_ACTION.items())]
    )
    write_csv(
        os.path.join(HERE, "data", "enum_legends.csv"),
        ["Field", "Value", "Name"],
        legends,
    )
    return revisions, sha


def copy_registries():
    copy_file(REGISTRY_FILES["1x"], os.path.join(HERE, "th_registry.yaml"))
    copy_file(REGISTRY_FILES["common"], os.path.join(HERE, "common_th_registry.yaml"))
    os.makedirs(os.path.join(HERE, "MLT"), exist_ok=True)
    os.makedirs(os.path.join(HERE, "L10"), exist_ok=True)
    copy_file(REGISTRY_FILES["mlt"], os.path.join(HERE, "MLT", "mlt_th_registry.yaml"))
    copy_file(REGISTRY_FILES["l10"], os.path.join(HERE, "L10", "l10_th_registry.yaml"))
    open(os.path.join(HERE, ".nojekyll"), "w", encoding="utf-8").close()


def write_comparison(diffs, old_rows, new_rows):
    l11 = [row for row in old_rows if row["stage"] == STAGE["l11"]]
    updated_codes = {
        (row["stage"], row["error_code"])
        for row in diffs
        if row["change_type"] in ("updated", "retired", "moved")
    }
    matched = set()
    old_ix = index_by_stage([row for row in old_rows if row["stage"] != STAGE["l11"]])
    new_ix = index_by_stage(new_rows)
    for key in old_ix.keys() & new_ix.keys():
        if not field_changes(old_ix[key], new_ix[key]):
            matched.add(key)
    # Moves are not in the intersection under the new stage.
    summaries = [
        ("summary", "", "", "", "", "", "", "old_published_codes_excluding_l11", "", str(len(old_rows) - len(l11))),
        ("summary", "", "", "", "", "", "", "new_registry_codes", "", str(len(new_rows))),
        ("summary", "", "", "", "", "", "", "added", "", str(sum(1 for row in diffs if row["change_type"] == "added" and row["field"] == "code"))),
        ("summary", "", "", "", "", "", "", "added_to_extra_stage", "", str(sum(1 for row in diffs if row["change_type"] == "added" and row["field"] == "stage"))),
        ("summary", "", "", "", "", "", "", "removed", "", str(sum(1 for row in diffs if row["change_type"] == "removed"))),
        ("summary", "", "", "", "", "", "", "moved", "", str(sum(1 for row in diffs if row["change_type"] == "moved"))),
        ("summary", "", "", "", "", "", "", "retired_markers", "", str(sum(1 for row in diffs if row["change_type"] == "retired"))),
        ("summary", "", "", "", "", "", "", "updated_field_rows", "", str(sum(1 for row in diffs if row["change_type"] == "updated"))),
        ("summary", "", "", "", "", "", "", "codes_with_field_changes", "", str(len(updated_codes))),
        ("summary", "", "", "", "", "", "", "unchanged_codes", "", str(len(matched))),
        ("summary", "", "", "", "", "", "", "l11_carried_forward_not_in_registry", "", str(len(l11))),
    ]
    header = [
        "change_type",
        "catalog",
        "stage",
        "error_code",
        "name",
        "full_id_old",
        "full_id_new",
        "field",
        "old_value",
        "new_value",
    ]
    order = {"summary": 0, "added": 1, "removed": 2, "moved": 3, "retired": 4, "updated": 5}
    body = []
    for row in summaries:
        body.append(list(row))
    detail = sorted(
        diffs,
        key=lambda row: (
            order.get(row["change_type"], 9),
            row["stage"],
            row["error_code"],
            DIFF_FIELDS.index(row["field"]) if row["field"] in DIFF_FIELDS else 99,
        ),
    )
    for row in detail:
        body.append(
            [
                row["change_type"],
                row["catalog"],
                row["stage"],
                row["error_code"],
                row["name"],
                row["full_id_old"],
                row["full_id_new"],
                row["field"],
                row["old_value"],
                row["new_value"],
            ]
        )
    path = os.path.join(HERE, "error_code_update_comparison.csv")
    write_csv(path, header, body)
    return path, summaries


def esc(value):
    return html.escape(str("" if value is None else value))


NONE = "\u2014"
REPO_VERSION = "0.1"
REPO_URL = "https://github.com/Quan-Etched/ErrorCode_Prod_Test"
PAGES_URL = "https://quan-etched.github.io/ErrorCode_Prod_Test/"
SHEET_URL = (
    "https://docs.google.com/spreadsheets/d/"
    "1zKcxEXyYFLAQkI0AnVtZnSQ7Z-sxGqzGBpc9-0qhrqk/edit?gid=1353335746"
)
REGISTRY_URL = (
    "https://github.com/etched-ai/sw/blob/master/host/system_test/"
    "error_codes/th_registry.yaml"
)
SLACK_URL = "https://etchedai.slack.com/archives/C0B299EA7UK"
SLACK_URL_2 = "https://etchedai.slack.com/archives/C0BMBRF327R"


def page_css():
    text = open(os.path.join(OLD, "index.html"), encoding="utf-8").read()
    start = text.index("<style>") + len("<style>")
    end = text.index("</style>")
    return text[start:end]


def read_dicts(path):
    if not os.path.isfile(path):
        return []
    with open(path, newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def file_size(path):
    if not os.path.isfile(path):
        return NONE
    size = os.path.getsize(path)
    if size < 1024 * 1024:
        return f"{size / 1024:.0f} KB"
    return f"{size / 1048576:.1f} MB"


def dri_index():
    found = {}
    for row in read_dicts(os.path.join(HERE, "data", "dri_ownership.csv")):
        name = (row.get("Test Case") or "").strip()
        if name:
            found[name] = {
                "dri1": (row.get("DRI 1") or "").strip(),
                "dri2": (row.get("DRI 2") or "").strip(),
                "status": (row.get("Status") or "").strip(),
                "pr": (row.get("PR") or "").strip(),
            }
    return found


def blank():
    return f'<span class="none">{NONE}</span>'


def cases_html(cases, dri):
    if not cases:
        return blank()
    out = []
    for case in cases:
        hit = dri.get(case) or dri.get(case + "TestCase")
        if hit and hit["pr"]:
            pr = hit["pr"].split(",")[0].strip().rstrip("/")
            out.append(f'<a href="{esc(pr)}"><code>{esc(case)}</code></a>')
        else:
            out.append(f"<code>{esc(case)}</code>")
    return "<br>".join(out)


def bugs_html(bugs):
    if not str(bugs or "").strip():
        return blank()
    parts = []
    for bug in re.split(r",(?=\s*ETCH-)", str(bugs)):
        bug = bug.strip()
        match = re.match(r"(ETCH-\d+)(.*)", bug)
        if match:
            parts.append(
                f'<a href="https://etched.atlassian.net/browse/{match.group(1)}">'
                f"{match.group(1)}</a>{esc(match.group(2))}"
            )
        else:
            parts.append(esc(bug))
    return "<br>".join(parts)


def sev_badge(severity):
    if severity is None or severity == "":
        return blank()
    severity = int(severity)
    label = SEVERITY.get(severity, "").removeprefix("ERROR_")
    return (
        f'<span class="badge sev sev{severity}" title="{esc(SEVERITY.get(severity, ""))}">'
        f"S{severity} {esc(label)}</span>"
    )


def qa_badge(quick, text):
    if quick is None or quick == "":
        return f'<span class="badge qa">{esc(text or NONE)}</span>'
    quick = int(quick)
    label = QUICK_ACTION.get(quick, "").removeprefix("QA_")
    return (
        f'<span class="badge qa qa{quick}" title="{esc(QUICK_ACTION.get(quick, ""))}">'
        f"Q{quick} {esc(label)}</span>"
    )


def code_key(record):
    return re.sub(r"\d+", lambda match: match.group().zfill(6), record["code"])


def page_record(row):
    return {
        "code": row["full_id"],
        "stage": row["stage"],
        "packed": row["packed"],
        "version": row["version"],
        "doc_rev": row["doc_rev"],
        "author": row["author"],
        "author_basis": row["author_basis"],
        "name": row["name"],
        "message": row["message"],
        "severity": row["severity"],
        "qa": row["quick_action"],
        "quick_action_txt": row.get("quick_action_txt") or "",
        "procedure": row["procedure"],
        "error_type": row.get("error_type") or "",
        "component": row["component"],
        "test_cases": row["test_cases"],
        "source": row.get("source") or row["stage"],
        "root_cause": row.get("root_cause") or "",
        "bugs": row.get("bugs") or "",
        "owner": row["owner"],
        "since": row["since"],
        "doc_url": row["doc_url"],
        "in_registry": True,
        "retired": row.get("retired"),
    }


def l11_records():
    records = []
    for raw in read_dicts(os.path.join(HERE, "data", "l11.csv")):
        code = (raw.get("Error Code ID") or "").strip()
        if not code:
            continue
        severity = (raw.get("Severity") or "").strip()
        quick = (raw.get("Quick Action") or "").strip()
        records.append(
            {
                "code": code,
                "stage": "L11 Test",
                "packed": raw.get("Packed") or "",
                "version": raw.get("Version") or 1,
                "doc_rev": raw.get("Doc Rev") or "",
                "author": raw.get("Original Author") or "",
                "author_basis": raw.get("Author Basis") or "",
                "name": raw.get("Name") or "",
                "message": raw.get("Message") or "",
                "severity": int(severity) if severity.isdigit() else None,
                "qa": int(quick) if quick.isdigit() else None,
                "quick_action_txt": raw.get("Quick Action (sheet)") or "",
                "procedure": raw.get("Recover / Troubleshooting Procedure") or "",
                "error_type": raw.get("Error Type") or "",
                "component": raw.get("Component") or "",
                "test_cases": [
                    part.strip()
                    for part in (raw.get("Test Case") or "").split(",")
                    if part.strip()
                ],
                "source": raw.get("Source") or "",
                "root_cause": raw.get("Possible Root Cause") or "",
                "bugs": raw.get("Bugs") or "",
                "owner": raw.get("Owner") or "",
                "since": raw.get("Since") or "",
                "doc_url": raw.get("Doc URL") or "",
                "in_registry": (raw.get("In th_registry.yaml") or "").strip().lower() == "yes",
                "retired": False,
            }
        )
    records.sort(key=code_key)
    return records


def kv_table(pairs, headers):
    head = "".join(f"<th>{esc(header)}</th>" for header in headers)
    body = "\n".join(
        "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>" for row in pairs
    )
    return (
        '<div class="scroll"><table>\n<thead><tr>'
        + head
        + "</tr></thead>\n<tbody>\n"
        + body
        + "\n</tbody></table></div>"
    )


def code_table(records, dri, show_packed=False, show_root=False):
    headers = ["Error Code ID"]
    if show_packed:
        headers.append("Packed")
    headers += [
        "Ver",
        "Doc Rev",
        "Original Author",
        "Name",
        "Message",
        "Severity",
        "Quick Action",
        "Recover / Troubleshooting Procedure",
        "Error Type",
        "Component",
        "Test Case",
        "Source",
    ]
    if show_root:
        headers.append("Possible Root Cause")
    headers += ["Bugs", "Owner", "Since"]
    rows = []
    for record in records:
        anchor = (
            re.sub(r"[^A-Za-z0-9]+", "-", record["stage"]).strip("-").lower()
            + "--"
            + record["code"]
        )
        mark = ""
        if record.get("retired"):
            mark += ' <span class="badge nyr">retired</span>'
        elif not record["in_registry"]:
            mark += (
                ' <span class="badge nyr" title="not yet in th_registry.yaml">'
                "sheet only</span>"
            )
        if record["doc_url"]:
            link = f'<a href="{esc(record["doc_url"])}"><code>{esc(record["code"])}</code></a>'
        else:
            link = f'<code>{esc(record["code"])}</code>'
        cells = [f'<td class="id" id="{esc(anchor)}">{link}{mark}</td>']
        if show_packed:
            cells.append(f'<td class="num"><code>{esc(record["packed"]) or NONE}</code></td>')
        version_title = (
            "version: in th_registry.yaml"
            if record["in_registry"]
            else "not in th_registry.yaml yet; first revision by definition"
        )
        cells.append(
            f'<td class="num"><span class="badge ver" title="{esc(version_title)}">'
            f'v{esc(record["version"])}</span></td>'
        )
        cells.append(f'<td class="num">{esc(record["doc_rev"])}</td>')
        cells.append(
            f'<td class="who" title="{esc(record["author_basis"])}">{esc(record["author"])}</td>'
        )
        cells.append(f'<td><code class="nm">{esc(record["name"]) or NONE}</code></td>')
        cells.append(f'<td class="msg">{esc(record["message"])}</td>')
        cells.append(f'<td>{sev_badge(record["severity"])}</td>')
        cells.append(f'<td>{qa_badge(record["qa"], record["quick_action_txt"])}</td>')
        procedure = esc(record["procedure"]) or f'<span class="none">{NONE}</span>'
        cells.append(f'<td class="msg">{procedure}</td>')
        cells.append(f'<td>{esc(record["error_type"])}</td>')
        cells.append(f'<td><code>{esc(record["component"])}</code></td>')
        cells.append(f'<td>{cases_html(record["test_cases"], dri)}</td>')
        cells.append(f'<td>{esc(record["source"])}</td>')
        if show_root:
            cause = esc(record["root_cause"]) or f'<span class="none">{NONE}</span>'
            cells.append(f'<td class="msg">{cause}</td>')
        cells.append(f'<td>{bugs_html(record["bugs"])}</td>')
        cells.append(f'<td>{esc(record["owner"]) or blank()}</td>')
        cells.append(f'<td class="num">{esc(record["since"]) or blank()}</td>')
        rows.append("<tr>" + "".join(cells) + "</tr>")
    head = "".join(f"<th>{esc(header)}</th>" for header in headers)
    return (
        '<div class="scroll"><table class="codes">\n<thead><tr>'
        + head
        + "</tr></thead>\n<tbody>\n"
        + "\n".join(rows)
        + "\n</tbody></table></div>"
    )


def section(title, anchor, body, intro=""):
    intro_html = f'<p class="sub">{intro}</p>' if intro else ""
    return f'<h2 id="{anchor}">{esc(title)}</h2>{intro_html}{body}'


def write_html(new_rows, revisions, sha, summary_pairs):
    del summary_pairs
    dri = dri_index()
    mlt = sorted(
        [page_record(row) for row in new_rows if row["catalog"] in ("mlt", "1x")],
        key=code_key,
    )
    l10 = sorted(
        [page_record(row) for row in new_rows if row["catalog"] == "l10"],
        key=code_key,
    )
    common = sorted(
        [page_record(row) for row in new_rows if row["catalog"] == "common"],
        key=code_key,
    )
    l11 = l11_records()
    total = len(mlt) + len(l10) + len(common) + len(l11)
    in_reg = len(mlt) + len(l10) + len(common)

    def stat(count, label):
        return (
            f'<div class="stat"><div class="n">{count}</div>'
            f'<div class="l">{esc(label)}</div></div>'
        )

    rev_rows = [
        [f"<strong>{esc(row['Version'])}</strong>", esc(row["Comment"]), esc(row["Author"])]
        for row in sorted(revisions, key=lambda row: [int(part) for part in row["Version"].split(".")])
    ]
    doc_rev = revisions[-1]["Version"] if revisions else ""
    versions = sorted({row["version"] for row in new_rows})
    if versions == [1]:
        version_note = "every code at <code>version: 1</code>"
    else:
        shown = ", ".join(f"<code>version: {esc(item)}</code>" for item in versions)
        version_note = "registry versions " + shown

    field_rows = [
        [f"<code>{esc(row['Field'])}</code>", esc(row["Describe"])]
        for row in read_dicts(os.path.join(HERE, "data", "field_definitions.csv"))
        if (row.get("Field") or "") not in ("", "Char #", "Describe", "Define")
    ]
    bit_rows = [
        [
            f"<code>{esc(row.get('Char #') or '')}</code>",
            f"<strong>{esc(row.get('Describe') or '')}</strong>",
            esc(row.get("Define") or "").replace("\n", "<br>"),
        ]
        for row in read_dicts(os.path.join(HERE, "data", "error_id_encoding.csv"))
    ]
    dri_rows = []
    for name, item in sorted(dri.items()):
        links = ""
        for url in [part.strip().rstrip("/") for part in item["pr"].split(",") if part.strip()]:
            number = url.rstrip("/").split("/")[-1]
            links += f'<a href="{esc(url)}">#{esc(number)}</a> '
        dri_rows.append(
            [
                f"<code>{esc(name)}</code>",
                esc(item["dri1"]),
                esc(item["dri2"]),
                esc(item["status"]) or blank(),
                links or blank(),
            ]
        )
    notes = read_dicts(os.path.join(HERE, "data", "source_data_notes.csv"))
    if notes:
        collision_html = (
            "<p>These Error Code IDs each appear twice in one stage block of the sheet "
            "(an older short-form row plus a later expanded row). Identity segments are "
            "immutable, so the repeat is the same code: the row with more detail is kept "
            "and the other is listed here for reconciliation in the sheet.</p>"
            + kv_table(
                [
                    [
                        f"<code>{esc(row.get('Error Code ID') or '')}</code>",
                        esc(row.get("Stage") or ""),
                        f"<code>{esc(row.get('Quick action kept') or '')}</code>",
                        f"<code>{esc(row.get('Quick action dropped') or '')}</code>",
                        esc(row.get("Dropped row message") or "") or blank(),
                        (
                            f"<code>{esc(row.get('Dropped row test cases') or '')}</code>"
                            if (row.get("Dropped row test cases") or "").strip()
                            else blank()
                        ),
                    ]
                    for row in notes
                ],
                [
                    "Error Code ID",
                    "Stage",
                    "Quick action kept",
                    "Quick action dropped",
                    "Dropped row message",
                    "Dropped row test cases",
                ],
            )
        )
    else:
        collision_html = "<p>No duplicate Error Code IDs within a stage block.</p>"

    legend = lambda pairs: [
        [f"<code>{esc(key)}</code>", f"<code>{esc(value)}</code>"] for key, value in pairs
    ]
    download = kv_table(
        [
            [
                '<a href="etched_error_code.xlsx"><strong>etched_error_code.xlsx</strong></a>',
                "The source workbook &mdash; a mirror of the original spreadsheet. Same tabs "
                "in the same order, same columns, same rows, nothing added or reordered. "
                "This is the file to edit and commit.",
                file_size(os.path.join(HERE, "etched_error_code.xlsx")),
            ],
            [
                '<a href="etched_error_code_annotated.xlsx">etched_error_code_annotated.xlsx</a>',
                "The joined view: version, original author, severity and quick-action names, "
                "owner, <code>since</code>, and registry status, with the code tables refreshed "
                "from the current registries.",
                file_size(os.path.join(HERE, "etched_error_code_annotated.xlsx")),
            ],
            [
                "<code>data/source/</code><br>"
                '<a href="data/source/revision_history.csv">revision_history.csv</a><br>'
                '<a href="data/source/mlt_1x.csv">mlt_1x.csv</a><br>'
                '<a href="data/source/l10.csv">l10.csv</a><br>'
                '<a href="data/source/l11.csv">l11.csv</a><br>'
                '<a href="data/source/field_definitions.csv">field_definitions.csv</a><br>'
                '<a href="data/source/dri_ownership.csv">dri_ownership.csv</a><br>'
                '<a href="data/source/suite_run_log.csv">suite_run_log.csv</a>',
                "Each source tab as CSV, verbatim &mdash; the diffable form of the workbook above.",
                "7 files",
            ],
            [
                "<code>data/</code><br>"
                '<a href="data/revision_history.csv">revision_history.csv</a><br>'
                '<a href="data/mlt_1x.csv">mlt_1x.csv</a><br>'
                '<a href="data/l10.csv">l10.csv</a><br>'
                '<a href="data/common.csv">common.csv</a><br>'
                '<a href="data/l11.csv">l11.csv</a><br>'
                '<a href="data/field_definitions.csv">field_definitions.csv</a><br>'
                '<a href="data/error_id_encoding.csv">error_id_encoding.csv</a><br>'
                '<a href="data/dri_ownership.csv">dri_ownership.csv</a><br>'
                '<a href="data/source_data_notes.csv">source_data_notes.csv</a><br>'
                '<a href="data/enum_legends.csv">enum_legends.csv</a>',
                "Joined tabs as CSV. MLT / 1X, L10 and Common are refreshed from the registries. "
                "L11 is the previous spreadsheet draft.",
                "10 files",
            ],
            [
                '<a href="sheet.md">sheet.md</a>',
                "Verbatim export of the Google Sheet the earlier tables were built from.",
                file_size(os.path.join(HERE, "sheet.md")),
            ],
            [
                '<a href="th_registry.yaml">th_registry.yaml</a><br>'
                '<a href="MLT/mlt_th_registry.yaml">MLT/mlt_th_registry.yaml</a><br>'
                '<a href="L10/l10_th_registry.yaml">L10/l10_th_registry.yaml</a><br>'
                '<a href="common_th_registry.yaml">common_th_registry.yaml</a>',
                f"Snapshots of <code>host/system_test/error_codes</code> at <code>sw@{esc(sha)}</code>.",
                "4 files",
            ],
        ],
        ["File", "What it is", "Size"],
    )
    meta = (
        '<div class="meta"><dl>'
        f"<dt>Version</dt><dd><strong>v{REPO_VERSION}</strong> of this page and repo "
        f"&middot; document revision <strong>{esc(doc_rev)}</strong> &middot; {version_note}</dd>"
        f'<dt>Repository</dt><dd><a href="{REPO_URL}">{REPO_URL.replace("https://", "")}</a></dd>'
        f'<dt>Published at</dt><dd><a href="{PAGES_URL}">'
        f'{PAGES_URL.replace("https://", "").rstrip("/")}</a></dd>'
        f'<dt>Source of truth</dt><dd><a href="{REGISTRY_URL}"><code>etched-ai/sw</code> '
        "&rarr; <code>host/system_test/error_codes</code></a> "
        f'<span class="sub">sw@{esc(sha)}</span></dd>'
        f'<dt>Slack</dt><dd><a href="{SLACK_URL}">#error-code-define</a> &middot; '
        f'<a href="{SLACK_URL_2}">#tiger-error-code</a></dd>'
        "<dt>Owner</dt><dd><code>supercomputing-sw</code></dd>"
        "</dl></div>"
    )
    page = (
        "<title>32x Error Code Registry</title>\n<style>"
        + page_css()
        + "</style>\n<div class=\"wrap\">\n"
        + f"""<h1>32x Error Code Registry</h1>
<p class="sub">Consolidated Etched test-harness error codes &mdash; MLT&nbsp;/&nbsp;1X, L10, Common and L11 &mdash;
with revision history and original author per code. Field names and enum values follow
<code>th_registry.yaml</code> (TH Error Code Specification v0.3 &sect;7, &sect;11.1), the source of truth.</p>

{meta}

<div class="stats">
{stat(total, "error codes")}
{stat(len(mlt), "MLT / 1X")}
{stat(len(l10), "L10")}
{stat(len(common), "Common")}
{stat(len(l11), "L11")}
{stat(in_reg, "in the registries")}
{stat(len(dri), "test cases with DRI")}
</div>

<div class="note">
<strong>Identity segments are immutable.</strong> Per <code>th_registry.yaml</code>: never renumber,
never reuse a code &mdash; a change of meaning requires a new code. The <code>-S<em>x</em>Q<em>y</em></code>
suffix carries severity and quick action; the stable identity is the <code>TH-&lt;BLOCK&gt;-&lt;NNNN&gt;</code> prefix.
</div>

{section("Download the source workbook", "download", download,
         "Code tables below are refreshed from the registry snapshots. "
         "The spreadsheet export and its verbatim CSVs are unchanged.")}

{section("Revision history", "revisions",
         kv_table(rev_rows, ["Version", "Comment", "Author"]),
         "From the source spreadsheet, oldest revision first.")}

{section("Error code fields", "fields",
         kv_table(field_rows, ["Field", "Description"]))}

{section("Error ID encoding (L11 EC-* space)", "encoding",
         kv_table(bit_rows, ["Char #", "Describe", "Define"]),
         "Character layout of the 12-hex-digit <code>EC-</code> identifier used by the L11 block.")}

{section("Enum legends", "legends",
         '<div class="legends"><div><h3>Category</h3>'
         + kv_table(legend(sorted(CATEGORY.items())), ["Value", "Name"])
         + "</div><div><h3>Severity</h3>"
         + kv_table(legend(sorted(SEVERITY.items())), ["Value", "Name"])
         + "</div><div><h3>Quick action</h3>"
         + kv_table(legend(sorted(QUICK_ACTION.items())), ["Value", "Name"])
         + "</div></div>",
         "Values as used by <code>category</code>, <code>severity</code> and "
         "<code>quick_action</code> in the registries.")}

{section("MLT / 1X Module Test codes", "mlt", code_table(mlt, dri),
         f"Refreshed from <code>MLT/mlt_th_registry.yaml</code> and 1X-only leftovers. {len(mlt)} codes.")}

{section("L10 Test codes", "l10", code_table(l10, dri, show_packed=True),
         f"Refreshed from <code>L10/l10_th_registry.yaml</code>, with the packed 32-bit integer form. {len(l10)} codes.")}

{section("Common codes", "common", code_table(common, dri, show_packed=True),
         f"Cross-station codes from <code>common_th_registry.yaml</code>. {len(common)} codes.")}

{section("L11 Test codes", "l11", code_table(l11, dri, show_root=True),
         f"{len(l11)} codes.")}

{section("Test case DRI ownership", "dri",
         kv_table(dri_rows, ["Test case", "DRI 1", "DRI 2", "Status", "PR"]),
         "DRI 1 of a code&rsquo;s primary test case is what the <em>Original Author</em> column "
         "above resolves to; codes with no DRI listed fall back to the spec author "
         f"({esc(SPEC_AUTHOR)}). Hover an author cell to see which basis was used.")}

{section("Source data notes", "notes", collision_html,
         "Points where the spreadsheet needed a judgment call to normalize.")}

<h2 id="sources">Sources &amp; provenance</h2>
<ul>
<li>Source of truth &mdash; <a href="{REGISTRY_URL}"><code>etched-ai/sw &rarr; host/system_test/error_codes</code></a> ({in_reg} codes at <code>sw@{esc(sha)}</code>; snapshots committed alongside this page).</li>
<li>Spreadsheet &mdash; <a href="{SHEET_URL}">_Etched Error Code</a> (L11 and the verbatim export, revision 0.3).</li>
<li>Discussion &mdash; Slack <a href="{SLACK_URL}">#error-code-define</a>; <a href="{SLACK_URL_2}">#tiger-error-code</a>.</li>
<li>Spec docs &mdash; <a href="https://docs.google.com/document/d/19p0DrsD3fMRnOJajcB390yxke-aAjlfLj-Dbwmoktiw/edit">Error code format definition</a>, <a href="https://docs.google.com/document/d/1rj0vtUVVIzQ_QMn-OBfLXeXAmq5mkb8G7hubHn5DQNI/edit">error-event revision</a>.</li>
</ul>

<div class="note">
Aidan Holm, 2026-08-12 in #error-code-define: &ldquo;The source of truth is going to move to the
in-repo error code directory; from there we&rsquo;re eventually going to want some automated
documentation generated from that.&rdquo; This page is generated by <code>gen.py</code> from that
registry plus the spreadsheet &mdash; regenerate rather than hand-edit.
</div>

<footer>
v{REPO_VERSION} &middot; generated by <code>gen.py</code> from the error-code registries at <code>sw@{esc(sha)}</code>.
Owner of the code space: <code>supercomputing-sw</code>. Codes marked
<span class="badge nyr">sheet only</span> exist in the spreadsheet but are not yet in a registry.
</footer>
</div>
"""
    )
    with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8", newline="\n") as handle:
        handle.write(page)


def write_sheet(new_rows):
    src = os.path.join(OLD, "sheet.md")
    if os.path.isfile(src):
        copy_file(src, os.path.join(HERE, "sheet.md"))
        return
    lines = [
        "# Error codes refreshed from system_test/error_codes",
        "",
        "L11 remains the previous spreadsheet draft (no L11 registry).",
        "",
    ]
    for title, catalog in (
        ("MLT / 1X Module Test", ("mlt", "1x")),
        ("L10 Test", ("l10",)),
        ("Common", ("common",)),
    ):
        rows = [row for row in new_rows if row["catalog"] in catalog]
        rows.sort(key=lambda row: row["full_id"])
        lines.append(f"## {title}")
        lines.append("")
        lines.append("| Error Code ID | Name | Message | Component | Test Case |")
        lines.append("| --- | --- | --- | --- | --- |")
        for row in rows:
            message = row["message"].replace("|", "\\|")
            lines.append(
                f"| {row['full_id']} | {row['name']} | {message} | {row['component']} | "
                f"{', '.join(row['test_cases'])} |"
            )
        lines.append("")
    with open(os.path.join(HERE, "sheet.md"), "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines))


def write_xlsx(new_rows, diff_path):
    try:
        from openpyxl import Workbook
        from openpyxl.styles import Alignment, Font, PatternFill
        from openpyxl.utils import get_column_letter
    except ImportError:
        print("openpyxl not installed; workbooks skipped")
        return False

    def add_sheet(workbook, name, header, rows):
        sheet = workbook.create_sheet(name[:31])
        sheet.append(header)
        for row in rows:
            sheet.append(["" if cell is None else cell for cell in row])
        fill = PatternFill("solid", fgColor="3C4450")
        font = Font(bold=True, color="FFFFFF")
        for cell in sheet[1]:
            cell.fill = fill
            cell.font = font
            cell.alignment = Alignment(vertical="center", wrap_text=True)
        sheet.freeze_panes = "A2"
        if rows:
            sheet.auto_filter.ref = f"A1:{get_column_letter(len(header))}{len(rows) + 1}"
        for index, title in enumerate(header, start=1):
            width = min(max(len(str(title)), 12), 48)
            sheet.column_dimensions[get_column_letter(index)].width = width
        return sheet

    groups = (
        ("MLT 1X", [row for row in new_rows if row["catalog"] in ("mlt", "1x")]),
        ("L10", [row for row in new_rows if row["catalog"] == "l10"]),
        ("Common", [row for row in new_rows if row["catalog"] == "common"]),
    )
    plain = Workbook()
    plain.remove(plain.active)
    joined = Workbook()
    joined.remove(joined.active)
    for name, rows in groups:
        rows = sorted(rows, key=lambda row: row["full_id"])
        body = [joined_row(row) for row in rows]
        add_sheet(plain, name, JOINED_COLS, body)
        add_sheet(joined, name, JOINED_COLS, body)
    with open(diff_path, newline="", encoding="utf-8-sig") as handle:
        diff_rows = list(csv.reader(handle))
    if diff_rows:
        add_sheet(joined, "Comparison", diff_rows[0], diff_rows[1:])
    plain_src = os.path.join(OLD, "etched_error_code.xlsx")
    if os.path.isfile(plain_src):
        copy_file(plain_src, os.path.join(HERE, "etched_error_code.xlsx"))
    else:
        plain.save(os.path.join(HERE, "etched_error_code.xlsx"))
    joined.save(os.path.join(HERE, "etched_error_code_annotated.xlsx"))
    return True


def write_readme(sha, new_rows, summary_pairs):
    counts = {row[7]: row[9] for row in summary_pairs}
    text = f"""# 32x-error-code refresh

Local refresh of the files in `32x-error-code`, generated from
`etched-ai/sw` `host/system_test/error_codes` at `{sha}`.

| Catalog | File | Codes |
| --- | --- | --- |
| MLT / 1X | `MLT/mlt_th_registry.yaml` plus 1X-only leftovers in `th_registry.yaml` | {sum(1 for row in new_rows if row['catalog'] in ('mlt', '1x'))} |
| L10 | `L10/l10_th_registry.yaml` | {sum(1 for row in new_rows if row['catalog'] == 'l10')} |
| Common | `common_th_registry.yaml` | {sum(1 for row in new_rows if row['catalog'] == 'common')} |
| L11 | previous spreadsheet draft | {counts.get('l11_carried_forward_not_in_registry', '')} (not in system_test) |

`error_code_update_comparison.csv` is the field-level diff against
`32x-error-code/data/{{mlt_1x,l10,l11}}.csv`.

- `added` / `removed` — identity appeared or disappeared
- `moved` — same identity, different station table
- `updated` — a field changed (`field`, `old_value`, `new_value`)
- `retired` — registry marks `retired: true`
- `summary` — counts at the top of the file

L11 rows are carried forward unchanged. Identity segments stay immutable.
Regenerate with `python gen.py` from this directory.
"""
    with open(os.path.join(HERE, "README.md"), "w", encoding="utf-8") as handle:
        handle.write(text)


def main():
    dri = load_dri()
    old_rows = load_old_codes()
    new_rows = load_new()
    annotate(new_rows, old_rows, dri)
    diffs = build_diff(old_rows, new_rows)
    os.makedirs(os.path.join(HERE, "data", "source"), exist_ok=True)
    copy_registries()
    write_tables(new_rows)
    revisions, sha = write_static()
    diff_path, summaries = write_comparison(diffs, old_rows, new_rows)
    write_sheet(new_rows)
    wrote_xlsx = write_xlsx(new_rows, diff_path)
    write_html(new_rows, revisions, sha, summaries)
    write_readme(sha, new_rows, summaries)
    print(f"sha {sha}")
    print(f"new codes {len(new_rows)}  diff rows {len(diffs)}  xlsx {wrote_xlsx}")
    print(f"comparison {diff_path}")
    for row in summaries:
        print(f"  {row[7]}: {row[9]}")


if __name__ == "__main__":
    main()
