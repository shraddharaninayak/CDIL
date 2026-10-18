import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

# index.html
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

old_str_idx = 'srcset="./images/cdil/other/CD.jpeg" src="./images/cdil/other/CD.jpeg" alt="Double-height entrance hall in natural stone"'
new_str_idx = 'srcset="./images/cdil/gallery/av5.jpg" src="./images/cdil/gallery/av5.jpg" alt="Scenic farmhouse land developments in Nashik | CDIL"'

assert old_str_idx in c, "Target string not found in index.html"
c_idx = c.replace(old_str_idx, new_str_idx)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c_idx)
print("Updated index.html background image successfully.")

# pages/page.html
with open('pages/page.html', 'r', encoding='utf-8') as f:
    c_p = f.read()

old_str_p = 'srcset="../images/cdil/other/CD.jpeg" src="../images/cdil/other/CD.jpeg" alt="Double-height entrance hall in natural stone"'
new_str_p = 'srcset="../images/cdil/gallery/av5.jpg" src="../images/cdil/gallery/av5.jpg" alt="Scenic farmhouse land developments in Nashik | CDIL"'

assert old_str_p in c_p, "Target string not found in pages/page.html"
c_p_upd = c_p.replace(old_str_p, new_str_p)

with open('pages/page.html', 'w', encoding='utf-8') as f:
    f.write(c_p_upd)
print("Updated pages/page.html background image successfully.")
