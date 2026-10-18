with open('index.html', 'r', encoding='utf-8-sig') as f:
    text = f.read()

import re

# Find hardcoded backgrounds like #0a0b09, rgb(10, 11, 9), rgb(27, 42, 33)
bgs = re.findall(r'background(?:-color)?:\s*([^;!]+)', text)
print(f"Total background declarations in index.html: {len(bgs)}")
unique_bgs = set(b.strip() for b in bgs if len(b.strip()) < 50)
print(f"Unique background values (sample of 25):")
for b in sorted(unique_bgs)[:25]:
    print(" ", b)

# Check custom classes in index.html
custom_classes = set(re.findall(r'cdil-[a-zA-Z0-9_-]+', text))
print("\nCDIL Custom classes found:")
for c in sorted(custom_classes):
    print(" ", c)
