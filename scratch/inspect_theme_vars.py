with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Look for :root and body CSS variables
body_vars = re.findall(r'body\{--token-[^}]+\}', text)
print(f"Found {len(body_vars)} body var blocks:")
for b in body_vars:
    print(b[:300])
    print("=" * 40)

# Also look for @media (prefers-color-scheme:dark)
dark_media = re.findall(r'@media\s*\(prefers-color-scheme:\s*dark\)\s*\{([^}]+(?:\{[^}]+\}[^}]+)*)\}', text)
print(f"Found {len(dark_media)} dark media blocks:")
for d in dark_media:
    print(d[:300])
    print("=" * 40)
