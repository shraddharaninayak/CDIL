import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = 0
idx = 1
while True:
    pos = c.find('CD.jpeg', pos)
    if pos == -1:
        break
    print(f"\n--- Occurrence {idx} at {pos} ---")
    print(c[max(0, pos-150):min(len(c), pos+150)])
    idx += 1
    pos += 7
