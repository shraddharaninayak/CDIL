import os, sys, re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find filter buttons / links
for a in soup.find_all('a'):
    txt = a.get_text(strip=True)
    if 'Project' in txt or 'ongoing' in str(a.get('href')):
        print("LINK:", txt, "HREF:", a.get('href'), "PARENT:", a.parent.name)

# Find script tags at the bottom to see if there is filtering JS
scripts = soup.find_all('script')
for s in scripts:
    st = s.get_text()
    if 'filter' in st.lower() or 'ongoing' in st.lower():
        print("\n--- SCRIPT WITH FILTER/ONGOING ---")
        print(st[:500])

