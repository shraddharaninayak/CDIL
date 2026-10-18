import re
from bs4 import BeautifulSoup
from test_builders import build_hero_bg_html, build_card_html, build_slideshow_script

def update_file(filepath, prefix):
    print(f"\nProcessing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Replace Hero Background
    bg_pattern = r'<div class="framer-qlv4de-container" data-code-component-plugin-id="mcp001"><!--\$--><div style="height:100%;width:100%;position:relative;overflow:hidden;background:rgb\(27, 42, 33\);isolation:isolate;z-index:0">.*?</div><!--/\$--></div>'
    new_bg = build_hero_bg_html(prefix)
    text, n_bg = re.subn(bg_pattern, new_bg, text, count=1, flags=re.DOTALL)
    print(f"  Hero BG replacements: {n_bg}")
    assert n_bg == 1, f"Failed to replace hero bg in {filepath}"

    # 2. Replace Card
    card_pattern = r'<div class="framer-gtXe7.*?</div></div></div><!--/\$--></div>'
    new_card = build_card_html()
    text, n_card = re.subn(card_pattern, new_card, text, count=1, flags=re.DOTALL)
    print(f"  Card replacements: {n_card}")
    assert n_card == 1, f"Failed to replace card in {filepath}"

    # 3. Insert or update slideshow script
    script_html = build_slideshow_script()
    if 'id="cdil-hero-slideshow-script"' in text:
        text = re.sub(r'<script id="cdil-hero-slideshow-script">.*?</script>', script_html, text, flags=re.DOTALL)
        print("  Updated existing slideshow script")
    else:
        # insert right before </body>
        body_pos = text.rfind('</body>')
        assert body_pos != -1, f"Could not find </body> in {filepath}"
        text = text[:body_pos] + script_html + '\n' + text[body_pos:]
        print("  Inserted new slideshow script before </body>")

    # Verify HTML syntax
    soup = BeautifulSoup(text, 'html.parser')
    imgs = soup.select('.cdil-hero-slide-bg img')
    print(f"  Verified {len(imgs)} background slide images in DOM")
    cards = soup.select('.cdil-card-slide')
    print(f"  Verified {len(cards)} card slides in DOM")
    bars = soup.select('.cdil-slide-bar')
    print(f"  Verified {len(bars)} indicator bars in DOM")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"  Successfully wrote {filepath}")

# Update both index.html and pages/page.html
update_file('index.html', prefix='./')
update_file('pages/page.html', prefix='../')
print("\nALL FILES UPDATED SUCCESSFULLY!")
