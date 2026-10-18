import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/journal.html', 'r', encoding='utf-8') as f:
    c = f.read()

# find all sections or framer-names in body
body_pos = c.find('<body')
for m in re.finditer(r'data-framer-name="([^"]+)"', c[body_pos:]):
    print("Framer name:", m.group(1), "pos:", m.start() + body_pos)

