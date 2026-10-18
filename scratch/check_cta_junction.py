import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/about.html', 'r', encoding='utf-8') as f:
    c = f.read()

cta_idx = c.find('data-framer-name="CTA"')
print("CTA index:", cta_idx)
print("Snippet around CTA junction:")
print(c[max(0, cta_idx-400):cta_idx+200])
