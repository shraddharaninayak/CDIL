import os
import glob
import re

# Search projects in html files or pages/
project_files = glob.glob('pages/*project*.html') + glob.glob('pages/*.html')
print("Pages:", project_files)

projects_found = set()
for p in project_files:
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()
        # Find project names like Laxmi Pushp, 3 Leaf Farmhouse, Watertouch, etc.
        for name in ['Laxmi Pushp', '3 Leaf', 'Watertouch', 'Vrindavan', 'Anandvan', 'Farmhouse', 'NA Plot', 'River', 'Lake', 'Siddhivinayak']:
            if name.lower() in text.lower():
                projects_found.add((p, name))

print("Found project mentions:")
for p, name in sorted(projects_found):
    print(f"  {p}: {name}")
