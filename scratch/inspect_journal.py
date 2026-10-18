import os, sys, re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/journal.html', 'r', encoding='utf-8') as f:
    c = f.read()

body_pos = c.find('<body')
cta_pos = c.find('<div class="framer-1eht9vy" data-framer-name="CTA">')

body_content = c[body_pos:cta_pos]
print("Journal body before CTA length:", len(body_content))
print("First 1500 chars of body content:")
print(body_content[:1500])

# check articles or cards
soup = BeautifulSoup(c, 'html.parser')
cards = soup.find_all(['article', 'a'], class_=lambda cl: cl and any(k in str(cl).lower() for k in ['journal', 'blog', 'card', 'post']))
print("Cards count:", len(cards))

