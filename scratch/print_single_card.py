import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

pos1 = html.find('<a class="framer-zzaslx framer-1u6c2pf" href="../pages/laxmi-pushp.html">')
pos2 = html.find('</a><!--/$--><!--$-->', pos1)
print(html[pos1:pos2+4])

