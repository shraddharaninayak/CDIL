import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/gallery.html', 'r', encoding='utf-8') as f:
    c = f.read()

body_pos = c.find('<body')
cta_pos = c.find('<div class="framer-1eht9vy" data-framer-name="CTA">')

print(c[body_pos:cta_pos])

