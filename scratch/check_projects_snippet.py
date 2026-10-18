import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/projects.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('Laxmi Pushp')
print("Position of Laxmi Pushp in projects.html:", pos)
if pos != -1:
    print(c[max(0, pos-400):min(len(c), pos+400)])
