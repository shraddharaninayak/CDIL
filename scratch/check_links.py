import os, re

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')

with open('pages/ongoing-projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

links = re.findall(r'<link[^>]*>', html)
for l in links:
    print(l)
