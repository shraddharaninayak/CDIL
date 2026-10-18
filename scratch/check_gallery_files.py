import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

gallery_files = [
    'av1.jpg', 'av2.jpg', 'av5.jpg', 'av7.jpg', 'av4.png', 'av.png',
    'tk5.jpeg', 'wt5.jpeg', 'teakwood1.jpeg', 'tk4.jpeg', 'tk6.jpeg', 'tk7.jpeg', 'tk3.jpeg',
    'watertouch.jpeg', 'wt1.jpeg', 'wt2.jpeg', 'wt3.jpeg',
    'riverranch.jpeg', 'rvr11.jpg', 'rr2.jpg', 'khand.jpg',
    'mb4.jpeg', 'mb1.jpeg', 'mb2.jpeg', 'wt4.jpeg', 'hills.jpeg'
]

missing = []
for f in gallery_files:
    p = os.path.join('images', 'cdil', 'gallery', f)
    if not os.path.exists(p):
        missing.append(f)

print(f"Total checked: {len(gallery_files)}, Missing: {len(missing)}")
if missing:
    print("Missing files:", missing)
else:
    print("All 26 gallery images exist locally in images/cdil/gallery/!")

