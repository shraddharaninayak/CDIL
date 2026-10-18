import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("File length:", len(content))

# Look for hero background image
for m in re.finditer(r'<div[^>]*class="[^"]*framer-1aiv44p[^"]*"[^>]*>', content):
    print("Found framer-1aiv44p:", m.group(0))

for m in re.finditer(r'images/[^"\'\s]+\.(?:jpg|png|webp)', content):
    img = m.group(0)
    if 'hero' in img.lower() or 'ziuh' in img.lower() or 'marisol' in img.lower():
        print("Hero-like image reference:", img)

# Let's inspect lines 380 to 460 of index.html
lines = content.splitlines()
for idx, line in enumerate(lines):
    if 'ZiuHJRK3VDqMlK0bXLemGXGx8o' in line or 'Rare homes' in line or 'framer-gtXe7' in line:
        print(f"Line {idx+1}: {line[:120]}")
