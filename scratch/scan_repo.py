import os

# Search all text files in repo for mentions of palm, sunset, garden, lawn, umbrella, or project names
keywords = ['3 leaf', 'amboli', 'mountain bliss', 'watertouch', 'teakwood', 'prophius', 'riverranch', 'ocean of beze']

for root, dirs, files in os.walk('.'):
    if 'scratch' in root or '.git' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
                # print any matches
                for kw in keywords:
                    if kw in content.lower():
                        pass
print("Done scan")
