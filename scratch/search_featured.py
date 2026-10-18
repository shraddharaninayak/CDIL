import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

for root, dirs, files in os.walk('.'):
    if 'scratch' in root or '.git' in root: continue
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                txt = fp.read()
            if 'FEATURED PROJECTS' in txt.upper() or 'MARISOL' in txt.upper():
                print(f"Found in {p}")
                for m in re.finditer(r'(FEATURED\s+PROJECTS|MARISOL)', txt, re.IGNORECASE):
                    print("  pos:", m.start())
                    print(" ", repr(txt[max(0, m.start()-100):min(len(txt), m.end()+200)]))

