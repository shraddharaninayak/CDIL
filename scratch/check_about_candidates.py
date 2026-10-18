import os, sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

candidates = [
    "images/cdil/banner/cdil-projects.jpeg",
    "images/cdil/gallery/hills.jpeg",
    "images/cdil/bg/2.jpg",
    "images/cdil/banner/3leaf-layout.jpeg",
    "images/projects/banner-cdil.jpeg",
    "images/cdil/gallery/av5.jpg",
    "images/cdil/gallery/khand.jpg",
    "images/cdil/product/riverranch.jpeg",
    "images/cdil/gallery/watertouch.jpeg",
    "images/cdil/other/riverranch1.jpg"
]

for p in candidates:
    if os.path.exists(p):
        try:
            im = Image.open(p)
            print(f"{p}: size={im.size}, aspect={im.size[0]/im.size[1]:.2f}")
        except Exception as e:
            print(f"{p}: error {e}")
    else:
        print(f"{p}: not found")
