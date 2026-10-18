import os, sys, urllib.request, re
from urllib.parse import urljoin, urlparse

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

pages_to_check = [
    "https://cdilrealestate.com/",
    "https://cdilrealestate.com/about.html",
    "https://cdilrealestate.com/projects.html",
    "https://cdilrealestate.com/ongoing-projects.html",
    "https://cdilrealestate.com/completed-projects.html",
    "https://cdilrealestate.com/upcoming-projects.html",
    "https://cdilrealestate.com/gallery.html",
    "https://cdilrealestate.com/blog.html",
    "https://cdilrealestate.com/news-updates.html",
    "https://cdilrealestate.com/contact.html",
    "https://cdilrealestate.com/3d-printed-house.html",
    "https://cdilrealestate.com/amboli-van-veli.html",
    "https://cdilrealestate.com/mountain-bless.html",
    "https://cdilrealestate.com/3-leaf-farmhouse.html",
    "https://cdilrealestate.com/laxmi-pushp.html",
    "https://cdilrealestate.com/watertouch.html",
    "https://cdilrealestate.com/teakwood-farm.html",
    "https://cdilrealestate.com/prophius-farm.html",
    "https://cdilrealestate.com/river-ranch.html",
    "https://cdilrealestate.com/ocean-of-beze.html"
]

all_images = set()

for page_url in pages_to_check:
    try:
        req = urllib.request.Request(page_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # find img src, background-image url, a href
            imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html, re.IGNORECASE)
            bg_imgs = re.findall(r'url\(["\']?([^"\'\)\?#]+\.(?:jpg|jpeg|png|webp))', html, re.IGNORECASE)
            for img in imgs + bg_imgs:
                full_url = urljoin(page_url, img)
                if any(full_url.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.webp']):
                    all_images.add((full_url, page_url))
        print(f"Scraped {page_url}: found {len(imgs)} imgs")
    except Exception as e:
        print(f"Failed {page_url}: {e}")

print(f"\nTotal unique images discovered: {len(all_images)}")
with open("scratch/discovered_cdil_images.txt", "w", encoding="utf-8") as f:
    for img, page in sorted(all_images):
        f.write(f"{img}\t{page}\n")
        print(f"  {img} (from {page})")
