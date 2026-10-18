import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

required_cards = [
    "Years of Expertise",
    "Projects Delivered on Time",
    "Prime Locations",
    "Trusted Reputation",
    "Customer Centric Approach",
    "Exceptional Amenities"
]

for fname in ['index.html', 'pages/page.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()
    
    print(f"\n=== Verifying {fname} ===")
    # 1. <div> balance
    open_divs = len(re.findall(r'<div\b', c))
    close_divs = len(re.findall(r'</div>', c))
    print(f"<div> balance: open={open_divs}, close={close_divs}, diff={open_divs - close_divs} -> {'PASS' if open_divs == close_divs else 'FAIL'}")
    
    # 2. Check 6 cards
    missing_cards = [card for card in required_cards if card not in c]
    print(f"Missing cards: {missing_cards} -> {'PASS' if not missing_cards else 'FAIL'}")
    
    # 3. Check section name
    has_why = 'data-framer-name="Why Choose Us"' in c
    print(f"Why Choose Us section present: {has_why} -> {'PASS' if has_why else 'FAIL'}")
    
    # 4. Check About section is gone
    has_old_about = 'data-framer-name="About"' in c
    print(f"Old About section present: {has_old_about} -> {'PASS' if not has_old_about else 'FAIL'}")
    
    # 5. Check junction context
    idx_why = c.find('id="why-choose-us"')
    print("Junction before why-choose-us:")
    print(repr(c[idx_why-120:idx_why]))
    
    idx_end = c.find('</section>', idx_why) + len('</section>')
    print("Junction after why-choose-us:")
    print(repr(c[idx_end:idx_end+120]))
