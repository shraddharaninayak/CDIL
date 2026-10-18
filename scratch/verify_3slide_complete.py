import os
from bs4 import BeautifulSoup

def verify_site_updates(filepath):
    print(f"\n==========================================")
    print(f"VERIFYING {filepath}...")
    print(f"==========================================")
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')

    file_dir = os.path.dirname(filepath)

    # 1. Hero background images
    bg_slides = soup.select('.cdil-hero-slide-bg')
    print(f"[TEST 1] Background slides count: {len(bg_slides)} (Expected: 3)")
    assert len(bg_slides) == 3, f"Expected 3 bg slides, got {len(bg_slides)}"

    expected_imgs = ['hero-slide-1.jpg', 'hero-slide-2.jpg', 'hero-slide-3.jpg']
    for idx, slide in enumerate(bg_slides):
        img = slide.find('img')
        assert img, f"Slide {idx} missing <img> tag"
        src = img.get('src', '')
        print(f"  Slide {idx}: {src}")
        assert any(e in src for e in expected_imgs), f"Slide {idx} image {src} not one of the 3 provided images"
        # check file existence on disk
        abs_path = os.path.normpath(os.path.join(file_dir, src) if file_dir else src)
        exists = os.path.exists(abs_path)
        print(f"    Resolves to: {abs_path} (exists={exists}, size={os.path.getsize(abs_path) if exists else 0} bytes)")
        assert exists, f"Image file not found: {abs_path}"

    # Verify old hero image is NOT in the hero slideshow
    hero_container = soup.find('div', id='cdil-hero-slides')
    assert 'ZiuHJRK3VDqMlK0bXLemGXGx8o' not in str(hero_container), "Old hero image found in hero slideshow container!"
    print("  [CONFIRMED] ONLY the 3 provided images are in the hero slideshow.")

    # 2. Featured Project Card
    card_slides = soup.select('.cdil-card-slide')
    print(f"\n[TEST 2] Featured card slides count: {len(card_slides)} (Expected: 3)")
    assert len(card_slides) == 3, f"Expected 3 card slides, got {len(card_slides)}"

    expected_cards = [
        ("3 Leaf Farmhouse", "Samundi Village, Trimbakeshwar, Nashik"),
        ("Amboli Van-Veli", "Gunjal Farm, Amboli, Nashik"),
        ("Watertouch Farmhouse", "Mahiravni, Nashik")
    ]
    for idx, card in enumerate(card_slides):
        h3 = card.find('h3')
        p = card.find('p')
        h3_t = h3.get_text(strip=True) if h3 else ''
        p_t = p.get_text(strip=True) if p else ''
        exp_h3, exp_p = expected_cards[idx]
        print(f"  Card Slide {idx}: {h3_t} | {p_t}")
        assert h3_t == exp_h3, f"Expected {exp_h3}, got {h3_t}"
        assert p_t == exp_p, f"Expected {exp_p}, got {p_t}"

    # 3. Indicator bars
    slide_bars = soup.select('.cdil-slide-bar')
    print(f"\n[TEST 3] Slide indicator bars count: {len(slide_bars)} (Expected: 3)")
    assert len(slide_bars) == 3, f"Expected 3 slide bars, got {len(slide_bars)}"

    # 4. View Projects Button & Section
    view_btn = soup.find('a', attrs={'data-framer-name': 'View Projects Button'})
    print(f"\n[TEST 4] View Projects button:")
    assert view_btn, "View Projects Button not found"
    print(f"  href: {view_btn.get('href')} (Expected: #our-projects)")
    assert view_btn.get('href') == '#our-projects', f"Expected #our-projects, got {view_btn.get('href')}"

    target_sec = soup.find('div', id='our-projects')
    print(f"[TEST 5] Target section #our-projects:")
    assert target_sec, "Section #our-projects not found"
    print(f"  framer-name: {target_sec.get('data-framer-name')}, style: {target_sec.get('style')}")
    assert target_sec.get('data-framer-name') == 'Our Projects', "Target section is not Our Projects"

    # 5. Script checks
    script = soup.find('script', id='cdil-hero-slideshow-script')
    assert script, "Missing cdil-hero-slideshow-script"
    script_text = script.string
    assert "['Ongoing Project', 'Ongoing Project', 'Completed Project']" in script_text, "Labels array mismatch"
    assert "scrollIntoView" in script_text, "Missing scrollIntoView in script"
    assert "our-projects" in script_text, "Missing our-projects reference in script"
    print("[TEST 6] Slideshow & Smooth Scroll Script verified")

    print(f"\n>>> ALL TESTS PASSED FOR {filepath}! <<<")

verify_site_updates('index.html')
verify_site_updates('pages/page.html')
print("\n[MASTER VERIFICATION] 100% OF CHECKS PASSED FOR ALL FILES!")
