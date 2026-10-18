import urllib.request
from bs4 import BeautifulSoup

project_pages = [
    'amboli-van-veli-farmhouse.html',
    'mountain-bless-farm-project.html',
    '3-leaf-farmhouse-project.html',
    'teakwood-farm-project.html',
    'water-touch-farmhouse.html',
    'prophius-farmhouse-project.html',
    'river-ranch-farm-project.html'
]

for p in project_pages:
    url = f'https://cdilrealestate.com/{p}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            soup = BeautifulSoup(resp.read().decode('utf-8', errors='ignore'), 'html.parser')
            imgs = [img.get('src') for img in soup.find_all('img') if 'icon' not in img.get('src', '') and 'cdil' not in img.get('src', '')]
            title = soup.find('h2') or soup.find('h1') or soup.find('h3')
            title_text = title.get_text(strip=True) if title else p
            print(f"{p} ({title_text}): {len(imgs)} imgs -> {imgs[:5]}")
    except Exception as e:
        print(f"Error {p}: {e}")
