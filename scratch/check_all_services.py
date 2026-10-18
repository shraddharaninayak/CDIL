import os, sys, glob

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

html_files = glob.glob("**/*.html", recursive=True)
found = []
for hf in html_files:
    with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    if 'data-framer-name="Services"' in c:
        found.append(hf)

print("Files with data-framer-name=\"Services\":", found)
