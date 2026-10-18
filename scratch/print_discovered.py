import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('scratch/discovered_cdil_images.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total discovered images: {len(lines)}")
for l in lines:
    print(l.strip())
