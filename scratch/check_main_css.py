import os, sys

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')
sys.stdout.reconfigure(encoding='utf-8')

with open('pages/ongoing-projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect the CSS for #main, framer-NbQct, or anything with position: absolute / fixed
import re

css_blocks = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
all_css = '\n'.join(css_blocks)

# Check classes on #main children:
# framer-NbQct framer-9Wydl framer-37WET framer-Cz1ej framer-IBDky framer-yopia framer-pM77G framer-nleCA framer-aPTbP framer-PtZKX framer-uMTfn framer-FaGLP framer-67z4u0
for c in ['framer-NbQct', 'framer-9Wydl', 'framer-37WET', 'framer-Cz1ej', 'framer-IBDky', 'framer-yopia', 'framer-pM77G', 'framer-nleCA', 'framer-aPTbP', 'framer-PtZKX', 'framer-uMTfn', 'framer-FaGLP', 'framer-67z4u0']:
    matches = re.findall(r'\.' + c + r'[^{]*\{[^}]*\}', all_css)
    if matches:
        print(f'Rule for {c}: {matches[:2]}')

# How about #main itself?
matches = re.findall(r'#main[^{]*\{[^}]*\}', all_css)
print('Rules for #main:', matches)
