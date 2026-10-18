import urllib.request, re, os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

headers = {'User-Agent': 'Mozilla/5.0'}
urls = [
    "https://cdilrealestate.com/3d-printed-house.html",
    "https://cdilrealestate.com/3d-printed-farmhouse.html",
    "https://cdilrealestate.com/samundi.html"
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content, re.IGNORECASE)
            print(f"{u} (Status {resp.status}): {imgs}")
    except Exception as e:
        print(f"{u}: {e}")
