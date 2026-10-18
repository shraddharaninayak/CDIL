import os, sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/gallery.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

cards = soup.find_all('div', class_=lambda c: c and 'cdil-gal-card' in c)
buttons = soup.find_all('button', class_=lambda c: c and 'cdil-gal-btn' in c)
lb = soup.find('div', id='cdilLightbox')
cta = soup.find('div', attrs={'data-framer-name': 'CTA'})
footer = soup.find('footer')

print(f"Gallery Cards: {len(cards)}")
print(f"Filter Buttons: {len(buttons)}")
print(f"Lightbox Modal: {lb is not None}")
print(f"CTA Present: {cta is not None}")
print(f"Footer Present: {footer is not None}")

