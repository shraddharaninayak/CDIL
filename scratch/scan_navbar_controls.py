import glob
from bs4 import BeautifulSoup

html_files = glob.glob('*.html') + glob.glob('pages/*.html')
print(f"Total HTML files: {len(html_files)}")

has_lang = []
has_theme = []

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
        if 'aria-label="Language"' in c or '>EN<' in c or '>EN\n' in c:
            has_lang.append(f)
        if 'aria-label="Switch to light mode"' in c or 'aria-label="Switch to dark mode"' in c:
            has_theme.append(f)

print(f"Files with Language Switcher: {len(has_lang)} of {len(html_files)}")
print(f"Files with Theme Button: {len(has_theme)} of {len(html_files)}")
if len(has_lang) < len(html_files):
    missing_lang = set(html_files) - set(has_lang)
    print("Files missing language switcher:", missing_lang)
