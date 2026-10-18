import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/gallery.html', 'r', encoding='utf-8') as f:
    c = f.read()

# find footer in gallery.html
pos = c.find('CDIL Real Estate &amp; Infrastructure')
print("Footer pos in gallery:", pos)
# find the container right after gallery grid
# Let's inspect from pos - 1000 to pos + 500
print(c[pos-1000:pos+500])

