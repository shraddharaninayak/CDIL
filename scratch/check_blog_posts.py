import os, sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('scratch/official_sources/blog.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

blogs = []
# Find all blog cards
for div in soup.find_all('div', class_=lambda c: c and any(k in str(c).lower() for k in ['single-product', 'blog', 'post', 'item'])):
    h4 = div.find(['h4', 'h3', 'h5', 'h2'])
    p = div.find('p')
    img = div.find('img')
    a = div.find('a')
    date_el = div.find(class_=lambda c: c and 'date' in str(c).lower())
    if h4 and not any(x in h4.get_text().lower() for x in ['cdil', 'our project', 'location', 'blog']):
        title = h4.get_text(strip=True)
        desc = p.get_text(strip=True) if p else ""
        img_src = img.get('src') if img else ""
        link = a.get('href') if a else ""
        date = date_el.get_text(strip=True) if date_el else ""
        blogs.append({
            'title': title,
            'desc': desc,
            'img': img_src,
            'link': link,
            'date': date
        })

print(f"Total blogs found: {len(blogs)}")
for i, b in enumerate(blogs[:10]):
    print(f"\n[{i+1}] Title: {b['title']}")
    print(f"    Date: {b['date']}")
    print(f"    Img: {b['img']}")
    print(f"    Desc: {b['desc'][:120]}")
    print(f"    Link: {b['link']}")
