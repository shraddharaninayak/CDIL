with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
scripts = [m.start() for m in re.finditer(r'<script', text)]
print("Scripts positions:", scripts)
for p in scripts:
    print(text[p:p+120].encode('ascii', 'ignore').decode('ascii'))
    print("-" * 30)
