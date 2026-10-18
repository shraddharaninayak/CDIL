import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/gallery.html', 'r', encoding='utf-8') as f:
    c = f.read()

# find grid start
pos1 = c.find('framer-111okhc')
print("Grid pos in gallery:", pos1)
# find the next section or container
# Let's search for "Schedule a Site Visit"
pos2 = c.find('Schedule a Site Visit')
print("Schedule pos in gallery:", pos2)
print("Between grid and schedule in gallery:")
print(c[pos1+500:pos2])

