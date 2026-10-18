import os, sys
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
            'img': img_src,
            'link': link
        })

print(f"Unique blogs found: {len(blogs)}")
for i, b in enumerate(blogs):
    print(f"[{i+1}] {b['title']} | Img: {b['img']} | Link: {b['link']}")
    # verify if img exists
    local_img = b['img'].replace('assets/img/', 'images/cdil/')
    print(f"     local_img: {local_img} exists: {os.path.exists(local_img)}")

