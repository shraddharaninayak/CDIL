import urllib.request
from bs4 import BeautifulSoup

url = 'https://cdilrealestate.com/gallery.html'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

soup = BeautifulSoup(html, 'html.parser')
for item in soup.find_all(['div', 'figure', 'li'], class_=lambda c: c and ('item' in c or 'gallery' in c or 'col' in c)):
    img = item.find('img')
    txt = item.get_text(strip=True)
    if img:
        print(f"Img: {img.get('src')}, Alt: {img.get('alt')}, Text: {txt[:60]}")
