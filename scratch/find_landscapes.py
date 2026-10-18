import os, sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

landscapes = []
for root, dirs, files in os.walk("images/cdil"):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            p = os.path.join(root, f)
            try:
                im = Image.open(p)
                w, h = im.size
                if w >= 1200 and w/h >= 1.4:
                    landscapes.append((p.replace("\\", "/"), w, h, os.path.getsize(p)/1024))
            except:
                pass

print(f"High-res wide landscapes (width >= 1200, aspect >= 1.4): {len(landscapes)}")
for p, w, h, size_kb in sorted(landscapes, key=lambda x: -x[3]):
    print(f"  {p}: {w}x{h} ({size_kb:.1f} KB)")
