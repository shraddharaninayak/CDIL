import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/page.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = 194318
print(c[pos-1000:pos-300])

