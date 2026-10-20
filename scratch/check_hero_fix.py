import os, sys

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')
sys.stdout.reconfigure(encoding='utf-8')

with open('pages/ongoing-projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('cdil-hero-fix')
if idx != -1:
    print('=== FOUND cdil-hero-fix ===')
    print(html[idx-100:idx+800])
else:
    print('cdil-hero-fix NOT FOUND')
