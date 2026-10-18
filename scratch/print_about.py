import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

print("=== ABOUT PAGE CONTENT ===")
with open('scratch/official_sources/about_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    # Filter out header/footer boilerplate
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    for l in lines:
        print(l)
