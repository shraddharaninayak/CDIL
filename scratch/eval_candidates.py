import os, sys
from PIL import Image, ImageStat

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

candidates = [
    "images/cdil/gallery/av5.jpg",
    "images/cdil/gallery/av1.jpg",
    "images/cdil/gallery/hills.jpeg",
    "images/cdil/bg/2.jpg",
    "images/cdil/product/riverranch.jpeg",
    "images/cdil/product/tw3.jpeg",
    "images/cdil/gallery/watertouch.jpeg",
]

for p in candidates:
    im = Image.open(p)
    stat = ImageStat.Stat(im)
    mean_brightness = sum(stat.mean[:3]) / 3
    print(f"{p}: size={im.size}, aspect={im.size[0]/im.size[1]:.2f}, mean_brightness={mean_brightness:.1f}")
