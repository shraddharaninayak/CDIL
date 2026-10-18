import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/laxmi-pushp.html', 'r', encoding='utf-8') as f:
    c = f.read()

cta_pos = c.find('Schedule a Site Visit')
print("CTA pos in laxmi-pushp:", cta_pos)
print("From cta_pos-200 to end:")
print(c[cta_pos-200:cta_pos+300])

