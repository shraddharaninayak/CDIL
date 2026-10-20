import os

os.chdir(r'D:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution')

for path in ['styles/cdil-theme.css', 'scripts/cdil-theme.js']:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()
        print(f'=== {path} ({len(c)} bytes) ===')
        for word in ['2.jpg', 'hero', 'Page Head', 'framer-16vp6ax', 'framer-10dozng', 'framer-1eht9vy', 'background', 'fixed', 'absolute', 'lakeside']:
            cnt = c.count(word)
            if cnt > 0:
                print(f'  contains "{word}": {cnt} times')
