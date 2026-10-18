with open('pages/projects.html', 'r', encoding='utf-8') as f:
    text = f.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(text, 'html.parser')

# Find cards or project headings
h3s = soup.find_all('h3')
print("H3s in projects.html:")
for h in h3s:
    print(" -", h.get_text(strip=True))

# Check images and their alt texts
imgs = soup.find_all('img')
print("\nImages in projects.html:")
for img in imgs:
    src = img.get('src')
    alt = img.get('alt')
    if src and ('project' in src or 'leaf' in src or 'pushp' in src or 'water' in src or 'amboli' in src):
        print(f"  src={src}, alt={alt}")
