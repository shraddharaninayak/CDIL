import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = 194330
a_pos = c.rfind('<a', 0, pos)
print("a_pos:", a_pos)
print(c[a_pos:a_pos+400])

