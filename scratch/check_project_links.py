import urllib.request, re, os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

headers = {'User-Agent': 'Mozilla/5.0'}
for p in ["https://cdilrealestate.com/projects.html", "https://cdilrealestate.com/ongoing-projects.html", "https://cdilrealestate.com/completed-projects.html"]:
    try:
        req = urllib.request.Request(p, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            links = re.findall(r'href=["\']([^"\']+\.html)["\']', content)
            imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
            print(f"=== {p} ===")
            print("Links:", set(links))
            print("Images:", imgs[:10])
    except Exception as e:
        print(f"Error {p}: {e}")
