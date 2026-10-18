import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/journal.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos1 = c.find('<a class="framer-sdggsy framer-f7ld5o"')
print("First card start:", pos1)
print(c[pos1-300:pos1])

# find the last card
pos_last = c.rfind('<a class="framer-sdggsy framer-f7ld5o"')
pos_last_end = c.find('</a><!--/$-->', pos_last) + len('</a><!--/$-->')
print("Last card end:", pos_last_end)
print(c[pos_last_end:pos_last_end+300])

