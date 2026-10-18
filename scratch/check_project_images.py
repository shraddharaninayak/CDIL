import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

candidates = [
    'images/projects/av3.jpg',
    'images/cdil/project/av3.JPG',
    'images/cdil/project/hills.jpeg',
    'images/cdil/gallery/mb1.jpeg',
    'images/projects/3leaf1.jpeg',
    'images/cdil/project/3leaf1.jpeg',
    'images/projects/lp1.jpeg',
    'images/cdil/project/teakwood1.jpeg',
    'images/projects/teakwood.jpeg',
    'images/cdil/project/watertouch.jpeg',
    'images/projects/water.jpg',
    'images/cdil/project/ps33.jpeg',
    'images/cdil/product/ps1.jpeg',
    'images/cdil/project/riverranch.jpeg',
    'images/projects/riverranch.jpeg',
    'images/cdil/banner/Ocean Of Beze.png',
    'images/cdil/banner/ocean_of_beze.png'
]

for c in candidates:
    print(c, "EXISTS:", os.path.exists(c))

