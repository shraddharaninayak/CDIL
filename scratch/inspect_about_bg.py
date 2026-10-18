import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# find CD.jpeg in index.html
pos = c.find('CD.jpeg')
print("Position of CD.jpeg in index.html:", pos)
if pos != -1:
    print("\n--- Snippet around CD.jpeg ---")
    print(c[max(0, pos-400):min(len(c), pos+400)])
