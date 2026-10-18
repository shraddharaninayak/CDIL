import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# search for CSS of framer-1pvpn3z, framer-60zqrq, framer-91yw29
for cls in ['framer-1pvpn3z', 'framer-60zqrq', 'framer-91yw29', 'framer-gtXe7']:
    m = re.search(rf'\.{cls}\b[^{{]*\{{([^}}]+)\}}', c)
    if m:
        print(f"CSS .{cls}: {m.group(1)}")

