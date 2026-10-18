import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/journal.html', 'r', encoding='utf-8') as f:
    c = f.read()

cta_pos = c.find('<div class="framer-1eht9vy" data-framer-name="CTA">')
print("CTA pos in journal.html:", cta_pos)
print("From 157000 to CTA pos:")
print(c[157000:cta_pos])

