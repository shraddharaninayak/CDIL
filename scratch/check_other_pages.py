import os, sys

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['about.html', 'watertouch.html', 'laxmi-pushp.html', '3-leaf-farmhouse.html']:
    p = os.path.join('pages', fname)
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            html = f.read()
        has_cta_css = 'framer-1eht9vy' in html[:html.find('</head>')]
        print(f'{fname}: has framer-1eht9vy in head style? {has_cta_css}')
