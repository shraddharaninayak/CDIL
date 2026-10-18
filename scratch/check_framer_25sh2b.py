with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'<div[^>]*framer-25sh2b', text)]
print("HTML matches for framer-25sh2b:", matches)
for m in matches:
    print(text[m:m+1000])
