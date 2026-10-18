import os, sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

for fname in ['journal.html', 'blog.html']:
    with open(f'pages/{fname}', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    cards = soup.find_all('a', class_=lambda c: c and 'cdil-blog-card' in c)
    modal = soup.find('div', id='cdilBlogModal')
    cta = soup.find('div', attrs={'data-framer-name': 'CTA'})
    footer = soup.find('footer')
    print(f"=== pages/{fname} ===")
    print(f"  Blog Cards: {len(cards)}")
    print(f"  Blog Modal: {modal is not None}")
    print(f"  CTA Present: {cta is not None}")
    print(f"  Footer Present: {footer is not None}")

