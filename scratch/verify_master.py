import os, sys, glob, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

print("=== CDIL MASTER VERIFICATION SUITE ===")
all_html = glob.glob("**/*.html", recursive=True)
print(f"Total HTML files found: {len(all_html)}")

# 1. Check data-framer-name="Services"
services_found = []
for hf in all_html:
    with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    if 'data-framer-name="Services"' in c:
        services_found.append(hf)
print(f"[CHECK 1] Services section present: {len(services_found)} files (Expected 0) -> {'PASS' if len(services_found) == 0 else 'FAIL: ' + str(services_found)}")

# 2. Check dollar prices ($[0-9])
price_matches = []
for hf in all_html:
    with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    m = re.findall(r'\$[0-9,]+', c)
    if m:
        price_matches.append((hf, m))
print(f"[CHECK 2] Currency price occurrences: {len(price_matches)} files (Expected 0) -> {'PASS' if len(price_matches) == 0 else 'FAIL: ' + str(price_matches)}")

# 3. Check Bed / Bath specs
spec_matches = []
for hf in all_html:
    with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    m = re.findall(r'\b(?:[0-9]+\s*(?:Beds?|Baths?|Sq Ft|sqft))\b', c, re.IGNORECASE)
    if m:
        spec_matches.append((hf, m))
print(f"[CHECK 3] Bed/Bath/Sqft occurrences: {len(spec_matches)} files (Expected 0) -> {'PASS' if len(spec_matches) == 0 else 'FAIL: ' + str(spec_matches)}")

# 4. Check Hero Image in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()
hero_img = 'images/ZiuHJRK3VDqMlK0bXLemGXGx8o.jpg'
hero_ok = hero_img in idx_content
print(f"[CHECK 4] Homepage Hero Image intact: {hero_ok} -> {'PASS' if hero_ok else 'FAIL'}")

# 5. Check CDIL Logo in navbar and footer
logo_count = idx_content.count('cdil-logo.png')
print(f"[CHECK 5] CDIL Logo instances in index.html: {logo_count} -> {'PASS' if logo_count >= 2 else 'FAIL'}")

# 6. Balanced <div> tags in index.html and pages/page.html
for fname in ['index.html', 'pages/page.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()
    open_divs = len(re.findall(r'<div\b', c))
    close_divs = len(re.findall(r'</div>', c))
    print(f"[CHECK 6] {fname} <div> balance: open={open_divs}, close={close_divs}, diff={open_divs - close_divs} -> {'PASS' if open_divs == close_divs else 'FAIL'}")

# 7. Check hamburger menu presence in index.html
has_menu = 'id="cdil-menu-overlay"' in idx_content and 'Schedule a Site Visit' in idx_content
print(f"[CHECK 7] Luxury hamburger menu present in index.html: {has_menu} -> {'PASS' if has_menu else 'FAIL'}")

print("=== ALL MASTER VERIFICATION CHECKS COMPLETED ===")
