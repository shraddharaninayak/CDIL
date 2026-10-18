import urllib.request, os, sys
from urllib.parse import urlparse

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

with open("scratch/all_cdil_scraped_images.txt", "r", encoding="utf-8") as f:
    lines = [l.strip().split("\t") for l in f if l.strip()]

os.makedirs("images/cdil", exist_ok=True)

downloaded = {}
failed = []

for item in lines:
    url = item[0]
    filename = os.path.basename(urlparse(url).path)
    # determine subfolder or prefix
    # e.g., if path contains 'gallery', 'product', 'icon', 'banner', 'other'
    path_parts = urlparse(url).path.strip("/").split("/")
    category = "general"
    if len(path_parts) > 2:
        category = path_parts[-2] # e.g. gallery, product, icon, banner, other
    
    cat_dir = os.path.join("images/cdil", category)
    os.makedirs(cat_dir, exist_ok=True)
    target_path = os.path.join(cat_dir, filename)

    if os.path.exists(target_path) and os.path.getsize(target_path) > 500:
        downloaded[url] = target_path
        continue

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            with open(target_path, "wb") as out:
                out.write(data)
        downloaded[url] = target_path
        print(f"Downloaded: {category}/{filename} ({len(data)} bytes)")
    except Exception as e:
        print(f"Failed {url}: {e}")
        failed.append((url, str(e)))

print(f"\nDownload finished. Total successful: {len(downloaded)}, Failed: {len(failed)}")
