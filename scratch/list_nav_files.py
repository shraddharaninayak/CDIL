import glob

html_files = glob.glob('*.html') + glob.glob('pages/*.html')
active_nav_files = []
for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
        if 'framer-vllTC' in c and ('aria-label="Language"' in c or 'Switch to light mode' in c):
            active_nav_files.append(f)

print(f"Total active nav files: {len(active_nav_files)}")
for f in active_nav_files:
    print(" -", f)
