import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/journal.html', 'r', encoding='utf-8') as f:
    c = f.read()

pos_articles = c.find('data-framer-name="Articles"')
pos_cta = c.find('data-framer-name="CTA"')

print("Articles start:")
print(c[pos_articles-50:pos_articles+150])

print("\nArticles end (before CTA):")
print(c[pos_cta-300:pos_cta+50])

