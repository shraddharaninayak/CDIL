import os, sys, re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/projects.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos = c.find('Laxmi Pushp')
print("--- SNIPPET AROUND LAXMI PUSHP ---")
print(c[pos-400:pos+600])

print("\n--- ALL H3 TAGS IN PROJECTS.HTML ---")
for m in re.finditer(r'<h3[^>]*>(.*?)</h3>', c, re.DOTALL):
    clean = re.sub(r'<[^>]+>', '', m.group(1)).strip()
    print("H3:", clean, "pos:", m.start())

