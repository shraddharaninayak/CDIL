import os, re
from bs4 import BeautifulSoup

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')

with open('pages/ongoing-projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's search for every <style> tag or CSS rule mentioning framer-1eht9vy, framer-10dozng, or 2.jpg
styles = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
print(f'Total style tags: {len(styles)}')
for i, s in enumerate(styles):
    for target in ['framer-1eht9vy', 'framer-10dozng', 'framer-16vp6ax', 'fixed', 'sticky']:
        if target in s:
            print(f'Style #{i} contains {target}')
            # print rules
            for rule in s.split('}'):
                if target in rule:
                    print('   ', rule.strip() + '}')

# Also let's check where the navbar is! Where is the navbar in ongoing-projects.html?
print('\n=== Navbar check ===')
nav_matches = re.findall(r'<nav[^>]*>|data-framer-name="[Nn]av[^"]*"', html)
print('Nav matches:', nav_matches)

# Let's check all elements with data-framer-name
names = re.findall(r'data-framer-name="([^"]+)"', html)
print('\n=== All data-framer-name in ongoing-projects.html ===')
for n in names:
    print(' -', n)
