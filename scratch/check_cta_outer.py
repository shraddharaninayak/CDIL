import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/gallery.html', 'r', encoding='utf-8') as f:
    g = f.read()

bg_pos = g.find('../images/cdil/bg/2.jpg')
print("bg_pos in gallery:", bg_pos)
print(g[bg_pos-400:bg_pos])

