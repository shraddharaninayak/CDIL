import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

for cls in ['framer-155z5sd', 'framer-1hju704', 'ay-glass-lg']:
    matches = re.findall(rf'([^{{}}]*\.{cls}[^{{}}]*\{{[^}}]+\}})', c)
    print(f"\nCSS rules for {cls}:")
    for m in matches:
        print(m.strip())
