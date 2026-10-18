import os
from bs4 import BeautifulSoup

def verify_hero_slideshow(filepath):
    print(f"\nVerifying Hero Slideshow in {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # 1. Slide Images
    bg_slides = soup.select('.cdil-hero-slide-bg')
    print(f"  Found {len(bg_slides)} background slides (expected 4)")
    assert len(bg_slides) == 4, "Must have exactly 4 background slides"

    file_dir = os.path.dirname(filepath)
    for idx, slide in enumerate(bg_slides):
        img = slide.find('img')
        assert img, f"Slide {idx} missing <img>"
        src = img.get('src')
        abs_path = os.path.normpath(os.path.join(file_dir, src) if file_dir else src)
        exists = os.path.exists(abs_path)
        print(f"    Slide {idx}: {src} -> resolves to {abs_path} (exists: {exists}, {os.path.getsize(abs_path) if exists else 0} bytes)")
        assert exists, f"Slide image file does not exist: {abs_path}"

    # 2. Card Slides
    card_slides = soup.select('.cdil-card-slide')
    print(f"  Found {len(card_slides)} card slides (expected 4)")
    assert len(card_slides) == 4, "Must have exactly 4 card slides"

    expected_data = [
        ("Laxmi Pushp", "Trambak Road, Nashik"),
        ("3 Leaf Farmhouse", "Samundi Village, Trimbakeshwar, Nashik"),
        ("Amboli Van-Veli", "Gunjal Farm, Amboli, Nashik"),
        ("Watertouch Farmhouse", "Mahiravni, Nashik")
    ]

    for idx, card in enumerate(card_slides):
        h3 = card.find('h3')
        p = card.find('p')
        h3_text = h3.get_text(strip=True) if h3 else ''
        p_text = p.get_text(strip=True) if p else ''
        exp_h3, exp_p = expected_data[idx]
        print(f"    Card {idx}: {h3_text} | {p_text}")
        assert h3_text == exp_h3, f"Expected {exp_h3}, got {h3_text}"
        assert p_text == exp_p, f"Expected {exp_p}, got {p_text}"

    # 3. Slide Bars
    bars = soup.select('.cdil-slide-bar')
    print(f"  Found {len(bars)} indicator bars (expected 4)")
    assert len(bars) == 4, "Must have exactly 4 indicator bars"

    # 4. Slideshow script
    script = soup.find('script', id='cdil-hero-slideshow-script')
    assert script, "Missing cdil-hero-slideshow-script"
    print("  [PASSED] Slideshow script verified")

verify_hero_slideshow('index.html')
verify_hero_slideshow('pages/page.html')

print("\n[ALL TESTS PASSED] ALL HERO SLIDESHOW VERIFICATIONS COMPLETED SUCCESSFULLY!")
