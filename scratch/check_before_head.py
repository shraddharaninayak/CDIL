import os, sys

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')
sys.stdout.reconfigure(encoding='utf-8')

with open('pages/ongoing-projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('<div class="framer-16vp6ax"')
print(f'Markup 600 chars before framer-16vp6ax:')
print(html[idx-600:idx])
