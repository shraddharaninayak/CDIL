with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
scripts = re.findall(r'<script.*?</script>', content, re.DOTALL)
print("Total script tags in index.html:", len(scripts))
for idx, s in enumerate(scripts):
    if 'hsZoom' in s or 'framer-91yw29' in s or 'slideshow' in s.lower() or 'slide' in s.lower():
        print(f"Script {idx+1} mentions slide:", s[:300])

# Also check pages/page.html if any
