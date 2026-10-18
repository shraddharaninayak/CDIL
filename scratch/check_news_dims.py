import os, sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

for i in range(1, 10):
    p = f"images/cdil/icon/n{i}.jpeg"
    if os.path.exists(p):
        im = Image.open(p)
        print(f"n{i}.jpeg: {im.size}, format: {im.format}")

