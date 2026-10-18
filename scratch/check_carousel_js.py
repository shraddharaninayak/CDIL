import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# check if there's any JS referencing 91yw29 or lbuxg6 or 1wgasjr
for term in ['91yw29', 'lbuxg6', '25sh2b', '1wgasjr', '2qhus3']:
    matches = list(re.finditer(term, c))
    print(f"Occurrences of {term}: {len(matches)}")
    for m in matches:
        # print if it's in a <script> tag
        script_idx = c.rfind('<script', 0, m.start())
        script_end = c.find('</script>', m.start())
        if script_idx != -1 and script_end != -1 and script_idx < m.start() < script_end:
            print(f"  In script: {c[m.start()-50:m.start()+50]}")

