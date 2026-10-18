import os, sys, json
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('scratch/official_sources/blog.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

blogs = []
seen = set()
for div in soup.find_all('div', class_=lambda c: c and any(k in str(c).lower() for k in ['single-product', 'blog', 'post', 'item'])):
    h4 = div.find(['h4', 'h3', 'h5', 'h2'])
    p = div.find('p')
    img = div.find('img')
    a = div.find('a')
    if h4 and not any(x in h4.get_text().lower() for x in ['cdil', 'our project', 'location', 'blog']):
        title = h4.get_text(strip=True)
        if title in seen:
            continue
        seen.add(title)
        desc = p.get_text(strip=True) if p else ""
        img_src = img.get('src') if img else ""
        link = a.get('href') if a else ""
        blogs.append({
            'title': title,
            'desc': desc,
            'img': img_src.replace('assets/img/', '../images/cdil/'),
            'link': link
        })

print(f"Total authentic blogs: {len(blogs)}")
for i, b in enumerate(blogs):
    print(f"[{i+1}] {b['title']}")
    print(f"    Img: {b['img']}")
    print(f"    Link: {b['link']}")
    print(f"    Desc: {b['desc'][:100]}...")

with open('scratch/authentic_blogs.json', 'w', encoding='utf-8') as f:
    json.dump(blogs, f, indent=2)

