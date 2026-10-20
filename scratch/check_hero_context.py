import os, re

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')

with open('pages/ongoing-projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('=== CONTEXT OF "hero" (offset 153666) ===')
print(html[153666-200:153666+200])

print('\n=== CONTEXT OF "slides" (offset 138966) ===')
print(html[138966-200:138966+200])

print('\n=== CSS RULES FOR framer-1eht9vy and framer-10dozng ===')
# Search all css
for m in re.finditer(r'([^{}]*framer-(?:1eht9vy|10dozng)[^{}]*\{[^{}]*\})', html):
    print(m.group(0))
