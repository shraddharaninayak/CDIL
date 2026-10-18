import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/projects.html', 'r', encoding='utf-8') as f:
    c = f.read()

body_pos = c.find('<body')
# find headings in body
for m in re.finditer(r'<h[1-4][^>]*>([^<]+)</h[1-4]>', c[body_pos:]):
    print(m.group(0))

pos_cards = c.find('Laxmi Pushp')
print("Laxmi Pushp pos:", pos_cards)
print(c[max(0, pos_cards-300):pos_cards+300])
