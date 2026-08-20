#!/usr/bin/env python3
"""Generate index.html for etched-ai/32x-error-code.

Sources
-------
1. Google Sheet "_Etched Error Code"
   https://docs.google.com/spreadsheets/d/1zKcxEXyYFLAQkI0AnVtZnSQ7Z-sxGqzGBpc9-0qhrqk
2. Slack #error-code-define (C0B299EA7UK)
3. Source of truth: etched-ai/sw host/system_test/error_codes/th_registry.yaml

Field naming and enum values follow th_registry.yaml (TH Error Code
Specification v0.3 GBP7, GBP11.1).
"""
import csv, html, os, re, sys, yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SHEET = os.path.join(HERE, 'sheet.md')
REGISTRY = os.path.join(HERE, 'th_registry.yaml')
OUT = os.path.join(HERE, 'index.html')
XLSX = os.path.join(HERE, 'etched_error_code.xlsx')            # verbatim mirror
ANNOTATED = os.path.join(HERE, 'etched_error_code_annotated.xlsx')  # joined view
XLSX_NAME = os.path.basename(XLSX)
ANNOTATED_NAME = os.path.basename(ANNOTATED)
DATA_DIR = os.path.join(HERE, 'data')
SRC_DIR = os.path.join(DATA_DIR, 'source')

# Best-effort tab names: the Drive markdown export carries no tab names, so the
# seven contiguous grids it emits are named after their content, in source
# order. Renaming a tab here is the only edit needed if the originals differ.
SOURCE_TABS = ['Revision History', 'MLT 1X', 'L10', 'L11',
               'Field Definitions', 'DRI Ownership', 'Suite Run Log']

# ------------------------------------------------------------------ identity
REPO_VERSION = '0.1'          # version of this repo / published page
REPO_URL = 'https://github.com/etched-ai/32x-error-code'
PAGES_URL = 'https://fantastic-telegram-38n6vyw.pages.github.io/'
SHEET_URL = ('https://docs.google.com/spreadsheets/d/'
             '1zKcxEXyYFLAQkI0AnVtZnSQ7Z-sxGqzGBpc9-0qhrqk/edit?gid=1353335746')
REGISTRY_URL = ('https://github.com/etched-ai/sw/blob/master/host/system_test/'
                'error_codes/th_registry.yaml')
SLACK_CHANNEL = '#error-code-define'
SLACK_URL = 'https://etchedai.slack.com/archives/C0B299EA7UK'
SLACK_CHANNEL_2 = '#tiger-error-code'
SLACK_URL_2 = 'https://etchedai.slack.com/archives/C0BMBRF327R'

# ---------------------------------------------------------------- enum legends
# Straight from th_registry.yaml inline comments.
CATEGORY = {0: 'CATEGORY_NONE', 1: 'CATEGORY_NETWORK', 3: 'CATEGORY_MEMORY',
            5: 'CATEGORY_CONFIG', 6: 'CATEGORY_HARDWARE', 7: 'CATEGORY_SOFTWARE',
            11: 'CATEGORY_DATA'}
SEVERITY = {2: 'ERROR_ISOLATE', 3: 'ERROR_UNKNOWN', 4: 'ERROR_TRIAGE',
            5: 'ERROR_CONFIG'}
QUICK_ACTION = {0: 'QA_NO_ACT', 1: 'QA_COLD_REBOOT', 2: 'QA_WARM_REBOOT',
                3: 'QA_SOFT_POWER_OFF', 4: 'QA_HARD_SHUTDOWN',
                5: 'QA_DISABLE_COMPONENT', 6: 'QA_RETRY', 7: 'QA_HOT_REMOVE',
                8: 'QA_HOT_SWITCH', 9: 'QA_ESCALATE'}

# --------------------------------------------------------------- sheet parsing
ESCAPED = re.compile(r'\\([_#~*`|<>\[\]().!\-])')

def unmd(cell):
    return ESCAPED.sub(r'\1', cell).strip()

def blocks(path):
    out, cur = [], []
    for line in open(path).read().split('\n'):
        if not line.strip():
            if cur:
                out.append(cur); cur = []
            continue
        if ':-:' in line:
            continue
        cur.append([unmd(c) for c in line.strip().strip('|').split('|')])
    if cur:
        out.append(cur)
    return out

def table(block):
    """First row with >=2 non-empty cells is the header; rest are records."""
    hdr_i = next(i for i, r in enumerate(block) if sum(bool(c) for c in r) >= 2)
    hdr = block[hdr_i]
    rows = []
    for r in block[hdr_i + 1:]:
        if not any(r):
            continue
        rows.append({hdr[i] if i < len(hdr) and hdr[i] else f'col{i}': (r[i] if i < len(r) else '')
                     for i in range(max(len(hdr), len(r)))})
    return hdr, rows

BL = blocks(SHEET)
revisions      = table(BL[0])[1]   # Version | Comment | Author
mlt_rows       = table(BL[1])[1]   # 1X Module Test / MLT
l10_rows       = table(BL[2])[1]   # L10 Test (has Packed + Name)
l11_rows       = table(BL[3])[1]   # L11 Test (EC-* numeric space)
field_defs     = table(BL[4])[1]   # Field | Describe  (+ Error ID bitfield rows)
dri_rows       = table(BL[5])[1]   # test case | DRI 1 | DRI 2 | comment | PR

# The Error-ID bitfield legend is appended to the field-definition block.
field_defs = [r for r in field_defs if r.get('Field') and r.get('Describe')]
bitfield = [r for r in table(BL[4])[1] if r.get('Field') in ('Char #', 'Describe', 'Define')
            and r.get('col2')]

# ------------------------------------------------------------ DRI / authorship
DRI = {}
for r in dri_rows:
    tc = r.get('col0', '').strip()
    if not tc or tc == 'DRI Members' or r.get('DRI 1', '') == '':
        continue
    DRI[tc] = {'dri1': r.get('DRI 1', '').strip(),
               'dri2': r.get('DRI 2', '').strip(),
               'status': r.get('comment', '').strip(),
               'pr': r.get('PR', '').strip()}

SPEC_AUTHOR = revisions[0]['Author'] if revisions else 'Ulysses Kao'

def split_cases(s):
    return [c.strip() for c in re.split(r'[,;]', s or '') if c.strip()]

def author_for(test_cases):
    """Original author = DRI 1 of the first test case that has one listed
    (DRI tab of the sheet); otherwise the spec author who drafted the code."""
    for tc in test_cases:
        if tc in DRI and DRI[tc]['dri1']:
            return DRI[tc]['dri1'], f'DRI 1 of {tc}'
        base = tc if tc.endswith('TestCase') else tc + 'TestCase'
        if base in DRI and DRI[base]['dri1']:
            return DRI[base]['dri1'], f'DRI 1 of {base}'
    return SPEC_AUTHOR, 'spec author (no DRI listed)'

# ------------------------------------------------------------------- registry
reg = {}
for e in yaml.safe_load(open(REGISTRY)):
    reg[e['error_code']] = e

SUFFIX = re.compile(r'^(TH-[A-Z0-9]+-\d+)(?:-S(\d)Q(\d))?$')

def base_and_flags(code):
    m = SUFFIX.match(code.strip())
    if not m:
        return code.strip(), None, None
    return m.group(1), (int(m.group(2)) if m.group(2) else None), \
           (int(m.group(3)) if m.group(3) else None)

def enrich(sheet_row, code_field, doc_rev, stage):
    code = sheet_row.get(code_field, '').strip()
    if not code:
        return None
    base, sev, qa = base_and_flags(code)
    e = reg.get(base, {})
    cases = split_cases(sheet_row.get('Test_Case', ''))
    if not cases and e.get('test_cases'):
        cases = list(e['test_cases'])
    author, basis = author_for(cases)
    if sev is None:
        sev = e.get('severity')
    if qa is None:
        qa = e.get('quick_action')
    desc = sheet_row.get('Message', '') or ' '.join((e.get('description') or '').split())
    return {
        'code': code, 'base': base, 'stage': stage,
        'name': sheet_row.get('Name', '') or e.get('name', ''),
        'packed': sheet_row.get('Packed', ''),
        'version': e.get('version', 1),
        'doc_rev': doc_rev,
        'author': author, 'author_basis': basis,
        'dri2': (DRI.get(cases[0], {}) or {}).get('dri2', '') if cases else '',
        'message': desc,
        'quick_action_txt': sheet_row.get('Quick_Action', ''),
        'procedure': sheet_row.get('Troubleshooting Procedure', '') or sheet_row.get('Recover_Step', ''),
        'source': sheet_row.get('Source', ''),
        'error_type': sheet_row.get('Error_Type', '') or CATEGORY.get(e.get('category'), ''),
        'category': e.get('category'), 'severity': sev, 'qa': qa,
        'component': sheet_row.get('Component', '') or e.get('component', ''),
        'test_cases': cases,
        'root_cause': sheet_row.get('Possible Root cause', ''),
        'bugs': sheet_row.get('Bugs', ''),
        'owner': e.get('owner', ''), 'since': e.get('since', ''),
        'doc_url': e.get('doc_url', ''),
        'disposition': e.get('disposition', ''),
        'retryable': e.get('retryable'),
        'in_registry': base in reg,
        'probable_causes': e.get('probable_causes') or [],
    }

COLLISIONS = []

def collect(rows, code_field, doc_rev, stage):
    """Collect a stage's codes, de-duplicating repeated Error Code IDs.

    The sheet lists a handful of codes twice inside one stage block (an older
    short-form row plus a later expanded row). Identity segments are immutable,
    so a repeat is the same code: keep the row carrying the most detail and
    record the collision so it is reported rather than silently dropped.
    """
    seen = {}
    for r in rows:
        rec = enrich(r, code_field, doc_rev, stage)
        if not rec:
            continue
        prev = seen.get(rec['code'])
        if prev is None:
            seen[rec['code']] = rec
            continue
        detail = lambda x: len(x['message']) + len(x['procedure']) + len(x['test_cases'])
        keep, drop = (rec, prev) if detail(rec) > detail(prev) else (prev, rec)
        seen[rec['code']] = keep
        keep['dup'] = True
        COLLISIONS.append({'stage': stage, 'code': rec['code'],
                           'kept': keep['quick_action_txt'] or '(blank)',
                           'dropped': drop['quick_action_txt'] or '(blank)',
                           'dropped_msg': drop['message'],
                           'dropped_cases': ', '.join(drop['test_cases'])})
    out = list(seen.values())
    out.sort(key=lambda x: (re.sub(r'\d+', lambda m: m.group().zfill(6), x['code'])))
    return out

# doc_rev = the sheet revision that introduced each stage's block (revision tab)
mlt = collect(mlt_rows, 'Error Code ID', '0.2', 'MLT / 1X Module Test')
l10 = collect(l10_rows, 'Error Code ID', '0.3', 'L10 Test')
l11 = collect(l11_rows, 'Error Code ID', '0.3', 'L11 Test')

# ------------------------------------------------------------------- rendering
def esc(x):
    return html.escape(str(x if x is not None else ''))

def cases_html(cases):
    if not cases:
        return '<span class="none">—</span>'
    out = []
    for c in cases:
        d = DRI.get(c) or DRI.get(c + 'TestCase')
        if d and d['pr']:
            pr = d['pr'].split(',')[0].strip().rstrip('/')
            out.append(f'<a href="{esc(pr)}"><code>{esc(c)}</code></a>')
        else:
            out.append(f'<code>{esc(c)}</code>')
    return '<br>'.join(out)

def bugs_html(bugs):
    if not bugs.strip():
        return '<span class="none">—</span>'
    parts = []
    for b in re.split(r',(?=\s*ETCH-)', bugs):
        b = b.strip()
        m = re.match(r'(ETCH-\d+)(.*)', b)
        if m:
            parts.append(f'<a href="https://etched.atlassian.net/browse/{m.group(1)}">'
                         f'{m.group(1)}</a>{esc(m.group(2))}')
        else:
            parts.append(esc(b))
    return '<br>'.join(parts)

def sev_badge(sev):
    if sev is None:
        return '<span class="none">—</span>'
    return f'<span class="badge sev sev{sev}" title="{esc(SEVERITY.get(sev, ""))}">S{sev} {esc(SEVERITY.get(sev, "").replace("ERROR_", ""))}</span>'

def qa_badge(qa, txt):
    if qa is None:
        return f'<span class="badge qa">{esc(txt or "—")}</span>'
    return (f'<span class="badge qa qa{qa}" title="{esc(QUICK_ACTION.get(qa, ""))}">'
            f'Q{qa} {esc(QUICK_ACTION.get(qa, "").replace("QA_", ""))}</span>')

def code_table(recs, show_packed=False, show_root=False):
    th = ['Error Code ID']
    if show_packed:
        th.append('Packed')
    th += ['Ver', 'Doc Rev', 'Original Author', 'Name', 'Message', 'Severity',
           'Quick Action', 'Recover / Troubleshooting Procedure', 'Error Type',
           'Component', 'Test Case', 'Source']
    if show_root:
        th.append('Possible Root Cause')
    th += ['Bugs', 'Owner', 'Since']
    rows = []
    for r in recs:
        tds = []
        anchor = re.sub(r'[^A-Za-z0-9]+', '-', r['stage']).strip('-').lower() + '--' + r['code']
        reg_mark = '' if r['in_registry'] else ' <span class="badge nyr" title="not yet in th_registry.yaml">sheet only</span>'
        if r.get('dup'):
            reg_mark += (' <span class="badge nyr" title="listed more than once in this '
                         'sheet block; merged, see Source data notes">merged</span>')
        link = (f'<a href="{esc(r["doc_url"])}"><code>{esc(r["code"])}</code></a>'
                if r['doc_url'] else f'<code>{esc(r["code"])}</code>')
        tds.append(f'<td class="id" id="{esc(anchor)}">{link}{reg_mark}</td>')
        if show_packed:
            tds.append(f'<td class="num"><code>{esc(r["packed"]) or "—"}</code></td>')
        vt = ('version: in th_registry.yaml' if r['in_registry']
              else 'not in th_registry.yaml yet; first revision by definition')
        tds.append(f'<td class="num"><span class="badge ver" title="{esc(vt)}">'
                   f'v{esc(r["version"])}</span></td>')
        tds.append(f'<td class="num">{esc(r["doc_rev"])}</td>')
        tds.append(f'<td class="who" title="{esc(r["author_basis"])}">{esc(r["author"])}</td>')
        tds.append(f'<td><code class="nm">{esc(r["name"]) or "—"}</code></td>')
        tds.append(f'<td class="msg">{esc(r["message"])}</td>')
        tds.append(f'<td>{sev_badge(r["severity"])}</td>')
        tds.append(f'<td>{qa_badge(r["qa"], r["quick_action_txt"])}</td>')
        tds.append(f'<td class="msg">{esc(r["procedure"]) or "<span class=none>—</span>"}</td>')
        tds.append(f'<td>{esc(r["error_type"])}</td>')
        tds.append(f'<td><code>{esc(r["component"])}</code></td>')
        tds.append(f'<td>{cases_html(r["test_cases"])}</td>')
        tds.append(f'<td>{esc(r["source"])}</td>')
        if show_root:
            tds.append(f'<td class="msg">{esc(r["root_cause"]) or "<span class=none>—</span>"}</td>')
        tds.append(f'<td>{bugs_html(r["bugs"])}</td>')
        tds.append(f'<td>{esc(r["owner"]) or "<span class=none>—</span>"}</td>')
        tds.append(f'<td class="num">{esc(r["since"]) or "<span class=none>—</span>"}</td>')
        rows.append('<tr>' + ''.join(tds) + '</tr>')
    head = ''.join(f'<th>{esc(h)}</th>' for h in th)
    return ('<div class="scroll"><table class="codes">\n<thead><tr>' + head +
            '</tr></thead>\n<tbody>\n' + '\n'.join(rows) + '\n</tbody></table></div>')

def kv_table(pairs, headers):
    head = ''.join(f'<th>{esc(h)}</th>' for h in headers)
    body = '\n'.join('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>' for row in pairs)
    return ('<div class="scroll"><table>\n<thead><tr>' + head +
            '</tr></thead>\n<tbody>\n' + body + '\n</tbody></table></div>')

# revision history — first version first (ascending)
rev_rows = [[f'<strong>{esc(r["Version"])}</strong>', esc(r['Comment']), esc(r['Author'])]
            for r in sorted(revisions, key=lambda r: [int(p) for p in r['Version'].split('.')])]

field_rows = [[f'<code>{esc(r["Field"])}</code>', esc(r['Describe'])] for r in field_defs]

bit_hdr = next((r for r in bitfield if r['Field'] == 'Char #'), None)
bit_desc = next((r for r in bitfield if r['Field'] == 'Describe'), None)
bit_def = next((r for r in bitfield if r['Field'] == 'Define'), None)
bit_rows = []
if bit_hdr and bit_desc and bit_def:
    keys = [k for k in bit_hdr if k != 'Field']
    for k in keys:
        if not bit_hdr.get(k):
            continue
        bit_rows.append([f'<code>{esc(bit_hdr[k])}</code>',
                         f'<strong>{esc(bit_desc.get(k, ""))}</strong>',
                         esc(bit_def.get(k, '')).replace('  ', '<br>')])

dri_table_rows = []
for tc, d in sorted(DRI.items()):
    pr = ''
    for u in [x.strip().rstrip('/') for x in d['pr'].split(',') if x.strip()]:
        n = u.rstrip('/').split('/')[-1]
        pr += f'<a href="{esc(u)}">#{esc(n)}</a> '
    dri_table_rows.append([f'<code>{esc(tc)}</code>', esc(d['dri1']), esc(d['dri2']),
                           esc(d['status']) or '<span class="none">—</span>',
                           pr or '<span class="none">—</span>'])

cat_rows = [[f'<code>{k}</code>', f'<code>{esc(v)}</code>'] for k, v in sorted(CATEGORY.items())]
sev_rows = [[f'<code>{k}</code>', f'<code>{esc(v)}</code>'] for k, v in sorted(SEVERITY.items())]
qa_rows = [[f'<code>{k}</code>', f'<code>{esc(v)}</code>'] for k, v in sorted(QUICK_ACTION.items())]

if COLLISIONS:
    collision_html = kv_table(
        [[f'<code>{esc(c["code"])}</code>', esc(c['stage']),
          f'<code>{esc(c["kept"])}</code>', f'<code>{esc(c["dropped"])}</code>',
          esc(c['dropped_msg']) or '<span class="none">—</span>',
          f'<code>{esc(c["dropped_cases"])}</code>' if c['dropped_cases'] else '<span class="none">—</span>']
         for c in sorted(COLLISIONS, key=lambda c: c['code'])],
        ['Error Code ID', 'Stage', 'Quick action kept', 'Quick action dropped',
         'Dropped row message', 'Dropped row test cases'])
    collision_html = (
        '<p>These Error Code IDs each appear twice in one stage block of the sheet '
        '(an older short-form row plus a later expanded row). Identity segments are '
        'immutable, so the repeat is the same code: the row with more detail is kept '
        'and the other is listed here for reconciliation in the sheet.</p>' + collision_html)
else:
    collision_html = '<p>No duplicate Error Code IDs within a stage block.</p>'


# ------------------------------------------------------------------- exports
# The maintainable copy of the sheet: one worksheet per source tab, plus a CSV
# of each so git can diff revisions. Regenerated from sheet.md + the registry,
# NOT a copy of the Drive binary (Drive binary export is not reachable here).
CODE_COLS = [
    ('Error Code ID', lambda r: r['code']),
    ('Packed', lambda r: r['packed']),
    ('Version', lambda r: r['version']),
    ('Doc Rev', lambda r: r['doc_rev']),
    ('Original Author', lambda r: r['author']),
    ('Author Basis', lambda r: r['author_basis']),
    ('DRI 2', lambda r: r['dri2']),
    ('Name', lambda r: r['name']),
    ('Message', lambda r: r['message']),
    ('Severity', lambda r: r['severity']),
    ('Severity Name', lambda r: SEVERITY.get(r['severity'], '')),
    ('Quick Action', lambda r: r['qa']),
    ('Quick Action Name', lambda r: QUICK_ACTION.get(r['qa'], '')),
    ('Quick Action (sheet)', lambda r: r['quick_action_txt']),
    ('Recover / Troubleshooting Procedure', lambda r: r['procedure']),
    ('Error Type', lambda r: r['error_type']),
    ('Category', lambda r: r['category']),
    ('Category Name', lambda r: CATEGORY.get(r['category'], '')),
    ('Component', lambda r: r['component']),
    ('Test Case', lambda r: ', '.join(r['test_cases'])),
    ('Source', lambda r: r['source']),
    ('Possible Root Cause', lambda r: r['root_cause']),
    ('Bugs', lambda r: r['bugs']),
    ('Owner', lambda r: r['owner']),
    ('Since', lambda r: r['since']),
    ('Disposition', lambda r: r['disposition']),
    ('Retryable', lambda r: r['retryable']),
    ('In th_registry.yaml', lambda r: 'yes' if r['in_registry'] else 'no'),
    ('Merged Duplicate', lambda r: 'yes' if r.get('dup') else ''),
    ('Doc URL', lambda r: r['doc_url']),
]

def code_sheet(recs):
    """Drop columns that are empty for every row in this stage."""
    cols = [(h, f) for h, f in CODE_COLS
            if any(str(f(r) or '').strip() for r in recs)]
    return [h for h, _ in cols], [[f(r) for _, f in cols] for r in recs]

def plain(rows, keys):
    return [[r.get(k, '') for k in keys] for r in rows]

def workbook_tabs():
    tabs = []
    tabs.append(('Revision History', ['Version', 'Comment', 'Author'],
                 plain(sorted(revisions,
                              key=lambda r: [int(p) for p in r['Version'].split('.')]),
                       ['Version', 'Comment', 'Author'])))
    for name, recs in (('MLT 1X', mlt), ('L10', l10), ('L11', l11)):
        hdr, rows = code_sheet(recs)
        tabs.append((name, hdr, rows))
    tabs.append(('Field Definitions', ['Field', 'Describe'],
                 [[r['Field'], r['Describe']] for r in field_defs]))
    if bit_rows:
        tabs.append(('Error ID Encoding', ['Char #', 'Describe', 'Define'],
                     [[re.sub('<[^>]+>', '', c.replace('<br>', '\n')) for c in row]
                      for row in bit_rows]))
    tabs.append(('DRI Ownership', ['Test Case', 'DRI 1', 'DRI 2', 'Status', 'PR'],
                 [[tc, d['dri1'], d['dri2'], d['status'], d['pr']]
                  for tc, d in sorted(DRI.items())]))
    if COLLISIONS:
        tabs.append(('Source Data Notes',
                     ['Error Code ID', 'Stage', 'Quick action kept',
                      'Quick action dropped', 'Dropped row message',
                      'Dropped row test cases'],
                     [[c['code'], c['stage'], c['kept'], c['dropped'],
                       c['dropped_msg'], c['dropped_cases']]
                      for c in sorted(COLLISIONS, key=lambda c: c['code'])]))
    tabs.append(('Enum Legends', ['Field', 'Value', 'Name'],
                 [['category', k, v] for k, v in sorted(CATEGORY.items())] +
                 [['severity', k, v] for k, v in sorted(SEVERITY.items())] +
                 [['quick_action', k, v] for k, v in sorted(QUICK_ACTION.items())]))
    return tabs

TABS = workbook_tabs()

def slug(name):
    return re.sub(r'[^a-z0-9]+', '_', name.lower()).strip('_')

def write_csvs(tabs):
    os.makedirs(DATA_DIR, exist_ok=True)
    written = []
    for name, hdr, rows in tabs:
        path = os.path.join(DATA_DIR, slug(name) + '.csv')
        with open(path, 'w', newline='') as fh:
            w = csv.writer(fh)
            w.writerow(hdr)
            for r in rows:
                w.writerow(['' if c is None else c for c in r])
        written.append((os.path.basename(path), name, len(rows)))
    return written

NUMERIC = re.compile(r'[1-9]\d*$')

def cell(v):
    """Original cell value; integers back to numbers, everything else verbatim.

    Leading-zero and dotted strings stay text ('0.1', '00: Undefine') because
    that is what the sheet holds.
    """
    return int(v) if NUMERIC.fullmatch(v) else v

def source_grids():
    """The sheet as exported: one grid per tab, rows verbatim, blanks kept."""
    out = []
    for i, block in enumerate(BL):
        name = SOURCE_TABS[i] if i < len(SOURCE_TABS) else f'Sheet{i + 1}'
        width = max(len(r) for r in block)
        rows = [[cell(r[c]) if c < len(r) else '' for c in range(width)] for r in block]
        out.append((name, rows))
    return out

def write_source_xlsx(grids):
    """Mirror of the original workbook: same tabs, same columns, same rows.

    Nothing is added, dropped, reordered or restyled -- the point is that a
    download of this file is the sheet, not a view of it. Formatting, merges
    and formulas cannot survive the markdown export and are not reconstructed.
    """
    try:
        from openpyxl import Workbook
        from openpyxl.utils import get_column_letter
    except ImportError:
        return False
    wb = Workbook()
    wb.remove(wb.active)
    for name, rows in grids:
        ws = wb.create_sheet(name[:31])
        for r in rows:
            ws.append(r)
        width = max(len(r) for r in rows)
        for i in range(1, width + 1):
            longest = max(len(str(r[i - 1])) for r in rows if i <= len(r))
            ws.column_dimensions[get_column_letter(i)].width = min(max(longest + 2, 9), 60)
    wb.save(XLSX)
    return True

def write_source_csvs(grids):
    os.makedirs(SRC_DIR, exist_ok=True)
    written = []
    for name, rows in grids:
        path = os.path.join(SRC_DIR, slug(name) + '.csv')
        with open(path, 'w', newline='') as fh:
            csv.writer(fh).writerows(rows)
        written.append((os.path.basename(path), name, len(rows)))
    return written


def write_xlsx(tabs):
    """The joined view: sheet data plus everything resolved from the registry."""
    try:
        from openpyxl import Workbook
        from openpyxl.styles import Alignment, Font, PatternFill
        from openpyxl.utils import get_column_letter
    except ImportError:
        print('openpyxl not installed - skipping workbooks', file=sys.stderr)
        return False
    wb = Workbook()
    wb.remove(wb.active)
    head_font = Font(bold=True, color='FFFFFF')
    head_fill = PatternFill('solid', fgColor='3C4450')
    wrap = Alignment(vertical='top', wrap_text=True)
    top = Alignment(vertical='top')
    for name, hdr, rows in tabs:
        ws = wb.create_sheet(name[:31])
        ws.append(hdr)
        for r in rows:
            ws.append(['' if c is None else c for c in r])
        for c in ws[1]:
            c.font, c.fill = head_font, head_fill
            c.alignment = Alignment(vertical='center', wrap_text=True)
        ws.freeze_panes = 'A2'
        if rows:
            ws.auto_filter.ref = (f'A1:{get_column_letter(len(hdr))}{len(rows) + 1}')
        for i, h in enumerate(hdr, start=1):
            widest = max([len(str(h))] + [len(str(r[i - 1])) for r in rows if i <= len(r)])
            width = min(max(widest + 2, 10), 60)
            ws.column_dimensions[get_column_letter(i)].width = width
            for cell in ws[get_column_letter(i)][1:]:
                cell.alignment = wrap if width >= 40 else top
        ws.row_dimensions[1].height = 30
    wb.save(ANNOTATED)
    return True

GRIDS = source_grids()
src_ok = write_source_xlsx(GRIDS)
src_csvs = write_source_csvs(GRIDS)
csvs = write_csvs(TABS)
ok = write_xlsx(TABS)
print(f'wrote {XLSX_NAME} (verbatim mirror, {len(GRIDS)} tabs)' if src_ok else
      'openpyxl missing - no workbooks written')
for fn, name, n in src_csvs:
    print(f'  data/source/{fn:<26} {name} ({n} rows)')
if ok:
    print(f'wrote {ANNOTATED_NAME} (joined view, {len(TABS)} tabs)')
for fn, name, n in csvs:
    print(f'  data/{fn:<33} {name} ({n} rows)')


def human(path):
    n = os.path.getsize(path)
    return f'{n / 1024:.0f} KB' if n < 1024 * 1024 else f'{n / 1048576:.1f} MB'


download_rows = [
    [f'<a href="{XLSX_NAME}"><strong>{XLSX_NAME}</strong></a>' if src_ok else
     f'<code>{XLSX_NAME}</code>',
     'The source workbook &mdash; a mirror of the original spreadsheet. Same tabs in '
     'the same order, same columns, same rows, nothing added or reordered. '
     'This is the file to edit and commit.',
     human(XLSX) if src_ok else '&mdash;'],
    [f'<a href="{ANNOTATED_NAME}">{ANNOTATED_NAME}</a>' if ok else
     f'<code>{ANNOTATED_NAME}</code>',
     'The same data with everything this page joins in &mdash; version, original '
     'author, severity/quick-action names, owner, <code>since</code>, registry '
     'status &mdash; plus autofilters and frozen headers.',
     human(ANNOTATED) if ok else '&mdash;'],
    ['<code>data/source/</code><br>' + '<br>'.join(
         f'<a href="data/source/{fn}">{fn}</a>' for fn, _, _ in src_csvs),
     'Each source tab as CSV, verbatim &mdash; the diffable form of the workbook above.',
     f'{len(src_csvs)} files'],
    ['<code>data/</code><br>' + '<br>'.join(
         f'<a href="data/{fn}">{fn}</a>' for fn, _, _ in csvs),
     f'The {len(csvs)} joined tabs as CSV &mdash; so git diffs a revision line by line '
     'instead of as a binary blob.',
     f'{len(csvs)} files'],
    ['<a href="sheet.md">sheet.md</a>',
     'Verbatim export of the Google Sheet the tables were built from.',
     human(SHEET)],
    ['<a href="th_registry.yaml">th_registry.yaml</a>',
     'Snapshot of the source of truth from <code>etched-ai/sw@master</code>.',
     human(REGISTRY)],
]


def stat(n, label):
    return f'<div class="stat"><div class="n">{n}</div><div class="l">{esc(label)}</div></div>'

total = len(mlt) + len(l10) + len(l11)
in_reg = sum(1 for r in mlt + l10 + l11 if r['in_registry'])

CSS = """
:root{--bg:#fff;--fg:#16181d;--muted:#606877;--line:#e3e6ec;--head:#f6f7f9;
--accent:#8a4b1e;--card:#fafbfc;--code:#f2f4f7}
:root:not([data-theme=light]){}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){
--bg:#111317;--fg:#e6e8ec;--muted:#98a1b0;--line:#282c34;--head:#191c22;
--accent:#e0a06a;--card:#171a20;--code:#1d2128}}
:root[data-theme=dark]{--bg:#111317;--fg:#e6e8ec;--muted:#98a1b0;--line:#282c34;
--head:#191c22;--accent:#e0a06a;--card:#171a20;--code:#1d2128}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
.wrap{max-width:1180px;margin:0 auto;padding:40px 22px 96px}
h1{font-size:1.85rem;margin:0 0 6px;letter-spacing:-.02em}
h2{font-size:1.18rem;margin:44px 0 6px;padding-top:16px;border-top:1px solid var(--line);
letter-spacing:-.01em}
h3{font-size:1rem;margin:26px 0 6px}
p{margin:8px 0}
.sub{color:var(--muted);font-size:.92rem}
a{color:var(--accent);text-decoration:none;border-bottom:1px solid transparent}
a:hover{border-bottom-color:currentColor}
code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.86em;
background:var(--code);padding:1px 4px;border-radius:3px;white-space:nowrap}
code.nm{white-space:normal;word-break:break-word}
.scroll{overflow-x:auto;border:1px solid var(--line);border-radius:8px;margin:14px 0}
table{border-collapse:collapse;width:100%;font-size:.83rem}
th,td{text-align:left;vertical-align:top;padding:8px 10px;border-bottom:1px solid var(--line)}
thead th{background:var(--head);position:sticky;top:0;font-weight:600;white-space:nowrap;
font-size:.78rem;letter-spacing:.02em;color:var(--muted);text-transform:uppercase}
tbody tr:last-child td{border-bottom:0}
tbody tr:hover{background:var(--card)}
td.msg{min-width:240px}
td.id,td.num,td.who{white-space:nowrap}
.none{color:var(--muted)}
.badge{display:inline-block;padding:1px 6px;border-radius:10px;font-size:.74rem;
font-weight:600;white-space:nowrap;border:1px solid var(--line);background:var(--card)}
.badge.ver{background:var(--code)}
.sev2{color:#b3261e;border-color:#b3261e55}
.sev3{color:#6c5ce7;border-color:#6c5ce755}
.sev4{color:#a86400;border-color:#a8640055}
.sev5{color:#1d6fa5;border-color:#1d6fa555}
.qa9{color:#b3261e;border-color:#b3261e55}
.qa6{color:#1d7a4c;border-color:#1d7a4c55}
.qa0{color:var(--muted)}
.nyr{color:var(--muted);font-weight:500}
.meta{background:var(--card);border:1px solid var(--line);border-radius:10px;
padding:6px 18px;margin:20px 0 4px}
.meta dl{display:grid;grid-template-columns:max-content 1fr;gap:0 20px;margin:0}
.meta dt{color:var(--muted);font-size:.76rem;text-transform:uppercase;
letter-spacing:.04em;font-weight:650;padding:7px 0;border-bottom:1px solid var(--line)}
.meta dd{margin:0;padding:7px 0;font-size:.88rem;border-bottom:1px solid var(--line);
overflow-wrap:anywhere}
.meta dt:last-of-type,.meta dd:last-of-type{border-bottom:0}
.meta .sub{font-size:.82rem}
@media(max-width:560px){.meta dl{grid-template-columns:1fr;gap:0}
.meta dt{padding-bottom:0;border-bottom:0}.meta dd{padding-top:2px}}
.stats{display:flex;flex-wrap:wrap;gap:10px;margin:20px 0 4px}
.stat{flex:1 1 120px;background:var(--card);border:1px solid var(--line);
border-radius:8px;padding:12px 14px}
.stat .n{font-size:1.5rem;font-weight:650;letter-spacing:-.02em}
.stat .l{color:var(--muted);font-size:.78rem;text-transform:uppercase;letter-spacing:.03em}
.legends{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px}
.note{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--accent);
border-radius:6px;padding:10px 14px;font-size:.88rem;color:var(--muted);margin:14px 0}
ul{margin:8px 0;padding-left:22px}
li{margin:3px 0}
footer{margin-top:56px;padding-top:16px;border-top:1px solid var(--line);
color:var(--muted);font-size:.82rem}
"""

META_ROWS = [
    ('Version', f'<strong>v{REPO_VERSION}</strong> of this page and repo &middot; '
                f'source spreadsheet revision <strong>'
                f'{rev_rows[-1][0].replace("<strong>", "").replace("</strong>", "")}'
                f'</strong> &middot; every code at <code>version: 1</code>'),
    ('Repository', f'<a href="{REPO_URL}">{REPO_URL.replace("https://", "")}</a>'),
    ('Published at', f'<a href="{PAGES_URL}">{PAGES_URL.replace("https://", "").rstrip("/")}</a>'
                     ' <span class="sub">(private &mdash; Etched org members)</span>'),
    ('Original spreadsheet', f'<a href="{SHEET_URL}">_Etched Error Code</a> '
                             '<span class="sub">(Google Sheets)</span>'),
    ('Source of truth', f'<a href="{REGISTRY_URL}"><code>etched-ai/sw</code> &rarr; '
                        '<code>host/system_test/error_codes/th_registry.yaml</code></a>'),
    ('Slack', f'<a href="{SLACK_URL}">{SLACK_CHANNEL}</a> &middot; '
              f'<a href="{SLACK_URL_2}">{SLACK_CHANNEL_2}</a>'),
    ('Owner', '<code>supercomputing-sw</code>'),
]

meta_html = ('<div class="meta"><dl>' + ''.join(
    f'<dt>{esc(k)}</dt><dd>{v}</dd>' for k, v in META_ROWS) + '</dl></div>')


def section(title, anchor, body, intro=''):
    return (f'<h2 id="{anchor}">{esc(title)}</h2>' +
            (f'<p class="sub">{intro}</p>' if intro else '') + body)

html_out = f"""<title>32x Error Code Registry</title>
<style>{CSS}</style>
<div class="wrap">
<h1>32x Error Code Registry</h1>
<p class="sub">Consolidated Etched test-harness error codes &mdash; MLT&nbsp;/&nbsp;1X, L10 and L11 &mdash;
with revision history and original author per code. Field names and enum values follow
<code>th_registry.yaml</code> (TH Error Code Specification v0.3 &sect;7, &sect;11.1), the source of truth.</p>

{meta_html}

<div class="stats">
{stat(total, 'error codes')}
{stat(len(mlt), 'MLT / 1X')}
{stat(len(l10), 'L10')}
{stat(len(l11), 'L11')}
{stat(in_reg, 'in th_registry.yaml')}
{stat(len(DRI), 'test cases with DRI')}
</div>

<div class="note">
<strong>Identity segments are immutable.</strong> Per <code>th_registry.yaml</code>: never renumber,
never reuse a code &mdash; a change of meaning requires a new code. The <code>-S<em>x</em>Q<em>y</em></code>
suffix carries severity and quick action; the stable identity is the <code>TH-&lt;BLOCK&gt;-&lt;NNNN&gt;</code> prefix.
</div>

{section('Download the source workbook', 'download',
         kv_table([[a, b, c] for a, b, c in download_rows],
                  ['File', 'What it is', 'Size']),
         'Everything on this page is generated from the two snapshots at the bottom '
         'of this list. Edit the workbook, commit it, re-run <code>gen.py</code>.')}

{section('Revision history', 'revisions',
         kv_table(rev_rows, ['Version', 'Comment', 'Author']),
         'From the source spreadsheet, oldest revision first.')}

{section('Error code fields', 'fields',
         kv_table(field_rows, ['Field', 'Description']))}

{section('Error ID encoding (L11 EC-* space)', 'encoding',
         kv_table(bit_rows, ['Char #', 'Describe', 'Define']),
         'Character layout of the 12-hex-digit <code>EC-</code> identifier used by the L11 block.')}

{section('Enum legends', 'legends',
         '<div class="legends"><div><h3>Category</h3>' +
         kv_table(cat_rows, ['Value', 'Name']) + '</div><div><h3>Severity</h3>' +
         kv_table(sev_rows, ['Value', 'Name']) + '</div><div><h3>Quick action</h3>' +
         kv_table(qa_rows, ['Value', 'Name']) + '</div></div>',
         'Values as used by <code>category</code>, <code>severity</code> and '
         '<code>quick_action</code> in <code>th_registry.yaml</code>.')}

{section('MLT / 1X Module Test codes', 'mlt', code_table(mlt),
         f'Introduced in sheet revision 0.2. {len(mlt)} codes.')}

{section('L10 Test codes', 'l10', code_table(l10, show_packed=True),
         f'Introduced in sheet revision 0.3, with the packed 32-bit integer form. {len(l10)} codes.')}

{section('L11 Test codes', 'l11', code_table(l11, show_root=True),
         f'Draft &mdash; L11 is still in progress (Slack #error-code-define, 2026-08-19). {len(l11)} codes.')}

{section('Test case DRI ownership', 'dri',
         kv_table(dri_table_rows, ['Test case', 'DRI 1', 'DRI 2', 'Status', 'PR']),
         'DRI 1 of a code&rsquo;s primary test case is what the <em>Original Author</em> column '
         'above resolves to; codes with no DRI listed fall back to the spec author '
         f'({esc(SPEC_AUTHOR)}). Hover an author cell to see which basis was used.')}

{section('Source data notes', 'notes', collision_html,
         'Points where the spreadsheet needed a judgment call to normalize.')}

<h2 id="sources">Sources &amp; provenance</h2>
<ul>
<li>Source of truth &mdash; <a href="https://github.com/etched-ai/sw/blob/master/host/system_test/error_codes/th_registry.yaml"><code>etched-ai/sw &rarr; host/system_test/error_codes/th_registry.yaml</code></a> ({len(reg)} codes; snapshot committed alongside this page).</li>
<li>Spreadsheet &mdash; <a href="https://docs.google.com/spreadsheets/d/1zKcxEXyYFLAQkI0AnVtZnSQ7Z-sxGqzGBpc9-0qhrqk/edit?gid=1353335746">_Etched Error Code</a> (revision {esc(rev_rows[-1][0].replace('<strong>','').replace('</strong>',''))}).</li>
<li>Discussion &mdash; Slack <a href="https://etchedai.slack.com/archives/C0B299EA7UK">#error-code-define</a>; <a href="https://etchedai.slack.com/archives/C0BMBRF327R">#tiger-error-code</a>.</li>
<li>Spec docs &mdash; <a href="https://docs.google.com/document/d/19p0DrsD3fMRnOJajcB390yxke-aAjlfLj-Dbwmoktiw/edit">Error code format definition</a>, <a href="https://docs.google.com/document/d/1rj0vtUVVIzQ_QMn-OBfLXeXAmq5mkb8G7hubHn5DQNI/edit">error-event revision</a>.</li>
</ul>

<div class="note">
Aidan Holm, 2026-08-12 in #error-code-define: &ldquo;The source of truth is going to move to the
in-repo error code directory; from there we&rsquo;re eventually going to want some automated
documentation generated from that.&rdquo; This page is generated by <code>gen.py</code> from that
registry plus the spreadsheet &mdash; regenerate rather than hand-edit.
</div>

<footer>
v{REPO_VERSION} &middot; generated by <code>gen.py</code> from <code>th_registry.yaml</code> + the _Etched Error Code sheet.
Owner of the code space: <code>supercomputing-sw</code>. Codes marked
<span class="badge nyr">sheet only</span> exist in the spreadsheet but are not yet in
<code>th_registry.yaml</code>.
</footer>
</div>
"""

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w').write(html_out)
print(f'wrote {OUT}  ({len(html_out)} bytes)')
print(f'  MLT/1X {len(mlt)}  L10 {len(l10)}  L11 {len(l11)}  total {total}  in-registry {in_reg}')
print(f'  DRI entries {len(DRI)}  revisions {len(rev_rows)}  field defs {len(field_rows)}  bitfield cols {len(bit_rows)}')
