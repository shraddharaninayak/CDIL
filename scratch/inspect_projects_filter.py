import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/projects.html', 'r', encoding='utf-8') as f:
    c = f.read()

# find the filter container and cards container
pos_filter = c.find('framer-name="Filter"')
if pos_filter == -1:
    pos_filter = c.find('Projects')
print("Position:", pos_filter)
print("Snippet around filter / heading:")
print(c[pos_filter:pos_filter+1200])
