import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('scratch/framer_images_usage.txt', 'r', encoding='utf-8') as f:
    text = f.read()

sections = text.split('====================\nImage: ')
for s in sections[1:]:
    lines = s.strip().split('\n')
    img = lines[0].split()[0]
    print(f"\n>>> IMAGE: {img}")
    for l in lines[1:]:
        print(l[:140])
