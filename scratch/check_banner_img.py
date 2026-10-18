import os, sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

# Let's inspect images/cdil/banner/cdil-projects.jpeg and images/projects/banner-cdil.jpeg
for p in ["images/cdil/banner/cdil-projects.jpeg", "images/projects/banner-cdil.jpeg"]:
    if os.path.exists(p):
        im = Image.open(p)
        print(f"{p}: size={im.size}, mode={im.mode}")
