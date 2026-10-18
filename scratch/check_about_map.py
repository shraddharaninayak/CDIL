import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/about.html', 'r', encoding='utf-8') as f:
    c = f.read()

# find all img tags in pages/about.html
imgs = re.findall(r'<img[^>]+>', c)
print(f"Total img tags in pages/about.html: {len(imgs)}")
for i, img in enumerate(imgs):
    print(f"\n--- Img {i+1} ---")
    print(img[:200])

# check where each img is located by snippet
for m in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', c):
    src = m.group(1)
    pos = m.start()
    print(f"\nImage src: {src} at pos {pos}")
    snippet = c[max(0, pos-250):min(len(c), pos+350)]
    print(snippet)
