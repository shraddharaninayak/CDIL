import os, sys

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')
sys.stdout.reconfigure(encoding='utf-8')

with open('pages/ongoing-projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('<div class="framer-16vp6ax"')
print(f'HTML occurrence at index {idx}:')
print(html[idx:idx+1500])
