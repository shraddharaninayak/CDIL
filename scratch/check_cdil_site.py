import urllib.request
import re

urls = [
    'https://cdilrealestate.com/',
    'https://cdilrealestate.com/about.html',
    'https://cdilrealestate.com/outgoing-project.html',
    'https://cdilrealestate.com/completed-project.html',
    'https://cdilrealestate.com/upcoming-project.html',
    'https://cdilrealestate.com/gallery.html',
    'https://cdilrealestate.com/3d-printed-farmhouse.html'
]

headers = {'User-Agent': 'Mozilla/5.0'}

for url in urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            print(f"URL: {url} (length {len(html)})")
            imgs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', html)
            print(f"  Total images: {len(imgs)}")
            # show first 5 and any mentioning project names
            for img in imgs[:8]:
                print("   -", img)
    except Exception as e:
        print(f"Failed {url}: {e}")
