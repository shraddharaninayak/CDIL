import re
from bs4 import BeautifulSoup
from test_3slide_builders import build_3slide_hero_bg, build_3slide_card, build_3slide_script

def apply_3slide_update(filepath, prefix):
    print(f"\nUpdating {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Update Hero BG with exactly 3 provided images
    bg_pattern = r'<div class="framer-qlv4de-container" data-code-component-plugin-id="mcp001"><!--\$--><div id="cdil-hero-slides".*?</div><!--/\$--></div>'
    new_bg = build_3slide_hero_bg(prefix)
    text, n_bg = re.subn(bg_pattern, new_bg, text, count=1, flags=re.DOTALL)
    print(f"  Hero BG replacement count: {n_bg}")
    assert n_bg == 1, f"Failed to replace hero bg in {filepath}"

    # 2. Update Card with exactly 3 slides & 3 indicator bars
    card_pattern = r'<div class="framer-gtXe7.*?</div></div></div><!--/\$--></div>'
    new_card = build_3slide_card()
    text, n_card = re.subn(card_pattern, new_card, text, count=1, flags=re.DOTALL)
    print(f"  Card replacement count: {n_card}")
    assert n_card == 1, f"Failed to replace card in {filepath}"

    # 3. Update "View Projects" button href to #our-projects
    btn_pattern = r'<a class="framer-1bpnpn1 framer-lux5qc ay-pill" data-framer-name="View Projects Button" href="[^"]*">'
    new_btn = '<a class="framer-1bpnpn1 framer-lux5qc ay-pill" data-framer-name="View Projects Button" href="#our-projects">'
    text, n_btn = re.subn(btn_pattern, new_btn, text, count=1)
    print(f"  View Projects button href replacement count: {n_btn}")
    assert n_btn == 1, f"Failed to update View Projects button in {filepath}"

    # 4. Add id="our-projects" and scroll-margin-top to Our Projects section
    # Check if id="our-projects" is already present
    if 'id="our-projects"' not in text:
        sec_pattern = r'<div class="framer-1vsy57f" data-framer-name="Our Projects">'
        new_sec = '<div class="framer-1vsy57f" id="our-projects" data-framer-name="Our Projects" style="scroll-margin-top: 80px;">'
        text, n_sec = re.subn(sec_pattern, new_sec, text, count=1)
        print(f"  Our Projects section id replacement count: {n_sec}")
        assert n_sec == 1, f"Failed to add id to Our Projects section in {filepath}"
    else:
        print("  Our Projects section already has id='our-projects'")

    # 5. Update Slideshow Script
    script_html = build_3slide_script()
    script_pattern = r'<script id="cdil-hero-slideshow-script">.*?</script>'
    text, n_scr = re.subn(script_pattern, script_html, text, count=1, flags=re.DOTALL)
    print(f"  Slideshow script replacement count: {n_scr}")
    assert n_scr == 1, f"Failed to update slideshow script in {filepath}"

    # 6. Verify with BeautifulSoup
    soup = BeautifulSoup(text, 'html.parser')
    bg_imgs = soup.select('.cdil-hero-slide-bg img')
    print(f"  Verified {len(bg_imgs)} background slide images (expected 3)")
    assert len(bg_imgs) == 3, f"Expected 3 bg images, found {len(bg_imgs)}"

    card_slides = soup.select('.cdil-card-slide')
    print(f"  Verified {len(card_slides)} card slides (expected 3)")
    assert len(card_slides) == 3, f"Expected 3 card slides, found {len(card_slides)}"

    slide_bars = soup.select('.cdil-slide-bar')
    print(f"  Verified {len(slide_bars)} indicator bars (expected 3)")
    assert len(slide_bars) == 3, f"Expected 3 slide bars, found {len(slide_bars)}"

    our_sec = soup.find('div', id='our-projects')
    assert our_sec, "Missing #our-projects section"
    print("  Verified #our-projects section exists")

    view_btn = soup.find('a', attrs={'data-framer-name': 'View Projects Button'})
    assert view_btn and view_btn.get('href') == '#our-projects', f"View Projects button href is {view_btn.get('href') if view_btn else None}"
    print("  Verified View Projects button links to #our-projects")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"  Successfully wrote {filepath}")

# Apply to index.html and pages/page.html
apply_3slide_update('index.html', prefix='./')
apply_3slide_update('pages/page.html', prefix='../')
print("\n[SUCCESS] Both index.html and pages/page.html updated to 3-slide layout with smooth scrolling!")
