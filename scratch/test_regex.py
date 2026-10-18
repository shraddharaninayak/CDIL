import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Check hero background pattern
bg_pattern = r'<div class="framer-qlv4de-container" data-code-component-plugin-id="mcp001"><!--\$--><div style="height:100%;width:100%;position:relative;overflow:hidden;background:rgb\(27, 42, 33\);isolation:isolate;z-index:0">.*?</div><!--/\$--></div>'
m_bg = re.search(bg_pattern, text, re.DOTALL)
print("BG pattern found:", bool(m_bg))
if m_bg:
    print("BG snippet length:", len(m_bg.group(0)))

# Check card pattern
card_pattern = r'<div class="framer-gtXe7.*?</div></div></div><!--/\$--></div>'
m_card = re.search(card_pattern, text, re.DOTALL)
print("Card pattern found:", bool(m_card))
if m_card:
    print("Card snippet length:", len(m_card.group(0)))
