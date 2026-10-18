import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/gallery.html', 'r', encoding='utf-8') as f:
    g = f.read()

scrim_pos = g.find('data-framer-name="Scrim"')
print("Scrim pos in gallery:", scrim_pos)
# look back 500 chars from scrim_pos
print(g[scrim_pos-500:scrim_pos+100])

