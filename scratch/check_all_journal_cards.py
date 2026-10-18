import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

with open('pages/journal.html', 'r', encoding='utf-8') as f:
    c = f.read()

# find all framer-sdggsy
cards = list(re.finditer(r'<a class="framer-sdggsy[^"]*"', c))
print(f"Total framer-sdggsy cards: {len(cards)}")
for i, m in enumerate(cards):
    title_m = re.search(r'<h3[^>]*>(.*?)</h3>', c[m.start():m.start()+1500])
    print(f"Card {i+1} at {m.start()}: {title_m.group(1) if title_m else 'N/A'}")

# find the end of the last card
last_card = cards[-1]
end_pos = c.find('</div></div></div>', last_card.start())
print("End of articles container:", end_pos)
print(c[end_pos-100:end_pos+200])

