from bs4 import BeautifulSoup
import glob

for p in ['pages/laxmi-pushp.html', 'pages/3-leaf-farmhouse.html', 'pages/watertouch.html', 'pages/amboli-van-veli.html', 'pages/residences.html']:
    with open(p, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        title = soup.title.string if soup.title else ''
        h1 = soup.find('h1').get_text(strip=True) if soup.find('h1') else ''
        print(f"=== {p} ({h1}) ===")
        for img in soup.find_all('img'):
            src = img.get('src', '')
            alt = img.get('alt', '')
            if 'logo' not in src and 'flag' not in src:
                print(f"  img: src={src}, alt={alt[:60]}")
