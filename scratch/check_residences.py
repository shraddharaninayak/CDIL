import os, sys

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')
sys.stdout.reconfigure(encoding='utf-8')

if os.path.exists('pages/residences.html'):
    with open('pages/residences.html', 'r', encoding='utf-8') as f:
        print('residences.html size:', len(f.read()))
else:
    print('residences.html does not exist')
