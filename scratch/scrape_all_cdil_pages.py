import urllib.request, re, os, sys
from urllib.parse import urljoin

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

headers = {'User-Agent': 'Mozilla/5.0'}

pages = [
    "nashik-first-3d-printed-farmhouse.html",
    "3-leaf-farmhouse-project.html",
    "amboli-van-veli-farmhouse.html",
    "laxmi-pushp-na-plots-deolali-nashik.html",
    "mountain-bless-farm-project.html",
    "water-touch-farmhouse.html",
    "teakwood-farm-project.html",
    "prophius-farmhouse-project.html",
    "river-ranch-farm-project.html",
    "outgoing-project.html",
    "completed-project.html",
    "upcoming-project.html",
    "video-gallery.html",
    "news-updates.html",
    "blog.html",
    "about.html",
    "gallery.html"
]

base_url = "https://cdilrealestate.com/"
all_discovered_images = {}

for p in pages:
    page_url = urljoin(base_url, p)
    try:
        req = urllib.request.Request(page_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'src=["\']([^"\']+\.(?:jpg|jpeg|png|webp))["\']', content, re.IGNORECASE)
            bg_imgs = re.findall(r'url\(["\']?([^"\'\)\?#]+\.(?:jpg|jpeg|png|webp))', content, re.IGNORECASE)
            combined = set(imgs + bg_imgs)
            for img in combined:
                full_img_url = urljoin(page_url, img)
                if "cdilrealestate.com" in full_img_url:
                    all_discovered_images[full_img_url] = p
            print(f"Scraped {p}: found {len(combined)} images")
    except Exception as e:
        print(f"Error {p}: {e}")

print(f"\nTotal authentic CDIL images discovered across all pages: {len(all_discovered_images)}")
os.makedirs("images/cdil", exist_ok=True)

with open("scratch/all_cdil_scraped_images.txt", "w", encoding="utf-8") as f:
    for img_url, source_page in sorted(all_discovered_images.items()):
        f.write(f"{img_url}\t{source_page}\n")
        print(f"  {img_url}  (from {source_page})")
