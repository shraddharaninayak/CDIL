with open('index.html', 'r', encoding='utf-8-sig') as f:
    text = f.read()

import re

print("HTML tag:", text[:text.find('>')+1].encode('ascii', 'ignore').decode('ascii'))
body_start = text.find('<body')
print("Body tag:", text[body_start:body_start+80].encode('ascii', 'ignore').decode('ascii'))

# Search for any theme-related scripts
found = False
for m in re.finditer(r'<script[^>]*>.*?</script>', text, re.DOTALL):
    s = m.group(0)
    if 'theme' in s.lower() or 'dark' in s.lower() or 'light' in s.lower() or 'color-scheme' in s.lower():
        print("Script with theme keywords:")
        print(s[:300].encode('ascii', 'ignore').decode('ascii'))
        print("=" * 40)
        found = True

if not found:
    print("No theme scripts found in index.html!")
