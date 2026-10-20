import os, re

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')

with open('pages/ongoing-projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
script_tags = re.findall(r'<script[^>]*>', html)

print(f'Total script tags: {len(script_tags)}')
for tag in script_tags:
    print('TAG:', tag)

# Check all occurrences of 'hero' or 'slides' or 'mcp' or 'slideshow' or '2.jpg'
for word in ['hero', 'slides', 'slideshow', '2.jpg', 'cdil-theme', 'script_main', 'rolldown']:
    matches = [m.start() for m in re.finditer(word, html, re.IGNORECASE)]
    print(f'Word "{word}": {len(matches)} occurrences at {matches[:5]}')
