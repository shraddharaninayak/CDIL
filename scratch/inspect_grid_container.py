import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's locate the container holding the cards
pos1 = html.find('framer-111okhc')
print("Position of framer-111okhc:", pos1)
# print 2000 chars from pos1
print(html[pos1:pos1+2500])

