import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

found_files = []
for root, dirs, files in os.walk('.'):
    if 'scratch' in root or '.git' in root: continue
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                txt = fp.read()
            if 'framer-1pvpn3z' in txt or 'View →' in txt:
                cnt = txt.count('View →')
                print(f"File {p}: 'View →' count = {cnt}, framer-1pvpn3z = {'framer-1pvpn3z' in txt}")
                found_files.append(p)

