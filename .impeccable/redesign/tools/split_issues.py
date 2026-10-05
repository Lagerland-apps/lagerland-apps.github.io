#!/usr/bin/env python3
"""Split critic issue files into per-surface issue files and a shared notes file; back up the pre-revision cards."""
import json, os, shutil, glob
BOARD = '/tmp/claude-0/-home-user-lagerland-apps-github-io/5553b341-96c8-5ef2-9d5c-b9201c3f3508/scratchpad/board'
os.makedirs(f'{BOARD}/data/issues', exist_ok=True)
os.makedirs(f'{BOARD}/data/orig', exist_ok=True)
per, notes = {}, []
import re
KNOWN = sorted({os.path.basename(p)[:-5] for p in glob.glob(f'{BOARD}/data/*.json') if not os.path.basename(p).startswith(('_', 'issues', 'sketch', 'plan'))}, key=len, reverse=True)
def match_surfaces(text):
    t = text.strip().lower()
    if t in ('all', '*', 'catalogue', 'all surfaces'):
        return list(KNOWN)
    found = []
    for sid in KNOWN:
        if re.search(r'(?<![a-z0-9-])' + re.escape(sid) + r'(?![a-z0-9-])', t):
            found.append(sid)
            t = re.sub(r'(?<![a-z0-9-])' + re.escape(sid) + r'(?![a-z0-9-])', ' ', t)
    if not found:
        print('UNMATCHED surface field:', text)
    return found
for f in sorted(glob.glob(f'{BOARD}/data/issues-*.json')):
    lens = os.path.basename(f)[7:-5]
    d = json.load(open(f))
    notes.append(f'## {lens}\n\n{d.get("catalogueNotes", "")}\n')
    for i in d['issues']:
        i['lens'] = lens
        for sid in match_surfaces(i['surface']):
            per.setdefault(sid, []).append(i)
open(f'{BOARD}/data/issues/_notes.md', 'w').write('\n'.join(notes))
known = {os.path.basename(p)[:-5] for p in glob.glob(f'{BOARD}/data/*.json') if not os.path.basename(p).startswith(('_', 'issues', 'sketch', 'plan'))}
for sid, items in per.items():
    if sid not in known:
        print('issue for unknown surface:', sid, len(items))
        continue
    json.dump(items, open(f'{BOARD}/data/issues/{sid}.json', 'w'), indent=1, ensure_ascii=False)
for sid in known:
    src = f'{BOARD}/data/{sid}.json'
    dst = f'{BOARD}/data/orig/{sid}.json'
    if not os.path.exists(dst):
        shutil.copy(src, dst)
rows = sorted(((sid, len(v), sum(1 for x in v if x['severity'] == 'blocker'), sum(1 for x in v if x['severity'] == 'major')) for sid, v in per.items() if sid in known), key=lambda r: -r[1])
for r in rows:
    print(f'{r[0]:14s} issues={r[1]:3d} blockers={r[2]} majors={r[3]}')
print('REVISE:', json.dumps([r[0] for r in rows if r[2] + r[3] > 0 or r[1] > 0]))
