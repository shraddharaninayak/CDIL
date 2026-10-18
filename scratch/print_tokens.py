with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m1 = re.search(r'body\{(--token-[^}]+)\}', text)
if m1:
    print("=== Default Body Tokens ===")
    tokens = m1.group(1).split(';')
    for t in tokens:
        print(" ", t)

m2 = re.search(r'@media\s*\(prefers-color-scheme:dark\)\s*\{body\{(--token-[^}]+)\}', text)
if m2:
    print("\n=== Dark Body Tokens ===")
    tokens = m2.group(1).split(';')
    for t in tokens:
        print(" ", t)

# Search for --ay-
ay_vars = set(re.findall(r'--ay-[a-zA-Z0-9_-]+', text))
print("\n=== AY Variables ===")
for v in sorted(ay_vars):
    print(" ", v)
