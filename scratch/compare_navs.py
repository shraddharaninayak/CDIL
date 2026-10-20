import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

root_dir = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"

with open(os.path.join(root_dir, "index.html"), "r", encoding="utf-8") as f:
    text_index = f.read()

with open(os.path.join(root_dir, "pages", "about.html"), "r", encoding="utf-8") as f:
    text_about = f.read()

# Extract from framer-ck16ym-container to </nav>
def get_nav(text):
    m = re.search(r'(<div class="framer-ck16ym-container.*?</nav>)', text, re.DOTALL)
    return m.group(1) if m else "NOT FOUND"

print("INDEX NAV:")
print(get_nav(text_index))
print("\n" + "="*50 + "\n")
print("ABOUT NAV:")
print(get_nav(text_about))
