import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/gallery.html', 'r', encoding='utf-8') as f:
    g = f.read()

cta_btn_pos = g.find('Schedule a Site Visit Button')
# look back to find the outer container of the CTA
print("1000 chars before CTA button:")
print(g[cta_btn_pos-1000:cta_btn_pos])

