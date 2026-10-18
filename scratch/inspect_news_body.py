import os, sys, re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/news-updates.html', 'r', encoding='utf-8') as f:
    c = f.read()

body_pos = c.find('<body')
cta_pos = c.find('<div class="framer-1eht9vy" data-framer-name="CTA">')

body_content = c[body_pos:cta_pos]
print("Length of body before CTA in news-updates.html:", len(body_content))
print("\n--- SNIPPET OF BODY CONTENT ---")
print(body_content[:2000])

