import os

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')

for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith(('.html', '.css', '.js', '.mjs')):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as infile:
                text = infile.read()
                if 'framer-10dozng' in text:
                    print(f'Found framer-10dozng in {p}')
