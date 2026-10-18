import os, sys, glob, re
from urllib.parse import urlparse

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

all_html = glob.glob("**/*.html", recursive=True)

broken_links = []
total_refs = 0

for hf in all_html:
    with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # find all src, href, srcset, and url(...) references to images
    doc_dir = os.path.dirname(hf)
    
    # img src
    srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content, re.IGNORECASE)
    # link rel="icon"
    favicons = re.findall(r'<link[^>]+href=["\']([^"\']+\.(?:png|ico|svg|jpg))["\']', content, re.IGNORECASE)
    # meta content images
    metas = re.findall(r'<meta[^>]+content=["\']([^"\']+\.(?:png|jpg|jpeg|webp))["\']', content, re.IGNORECASE)
    # srcset
    srcsets = re.findall(r'srcset=["\']([^"\']+)["\']', content, re.IGNORECASE)
    
    all_paths = srcs + favicons + metas
    for s in srcsets:
        for item in s.split(','):
            tokens = item.strip().split()
            if tokens:
                all_paths.append(tokens[0])
                
    for p in all_paths:
        if p.startswith('http://') or p.startswith('https://'):
            continue
        total_refs += 1
        # resolve relative to doc_dir
        # strip queries or hashes
        clean_p = p.split('?')[0].split('#')[0]
        resolved = os.path.normpath(os.path.join(doc_dir, clean_p))
        if not os.path.exists(resolved):
            broken_links.append((hf, p, resolved))

print(f"Total local image references checked: {total_refs}")
print(f"Total broken image links found: {len(broken_links)}")
if broken_links:
    for doc, link, resolved in broken_links:
        print(f"  BROKEN in {doc}: {link} (resolved as {resolved})")
else:
    print("ALL LOCAL IMAGE LINKS RESOLVE PERFECTLY!")
