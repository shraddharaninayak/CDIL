import os, sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/news-updates.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

articles = soup.find_all('article', class_=lambda c: c and 'cdil-news-card' in c)
lb = soup.find('div', id='cdilNewsLightbox')
cta = soup.find('div', attrs={'data-framer-name': 'CTA'})
footer = soup.find('footer')

print(f"News Articles: {len(articles)}")
print(f"News Lightbox: {lb is not None}")
print(f"CTA Present: {cta is not None}")
print(f"Footer Present: {footer is not None}")

for a in articles:
    h3 = a.find('h3')
    img = a.find('img')
    print("  Article:", h3.get_text()[:60] if h3 else "N/A", "| Img:", img.get('src') if img else "N/A")

