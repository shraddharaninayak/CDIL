import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

for fname in ['index.html', 'pages/page.html']:
    if not os.path.exists(fname): continue
    with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    
    # search for "VIEW" or "View" near "Laxmi Pushp" or "FEATURED PROJECTS"
    for m in re.finditer(r'VIEW', c):
        snippet = c[max(0, m.start()-200):min(len(c), m.end()+200)]
        print(f"=== {fname} at {m.start()} ===")
        print(snippet)

