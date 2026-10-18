import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('scratch/official_sources/news.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('n1.jpeg')
print(c[max(0, pos-300):min(len(c), pos+600)])
