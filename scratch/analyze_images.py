import os, sys, glob, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

# List all files currently in images/
local_imgs = []
for root, dirs, files in os.walk("images"):
    for f in files:
        rel = os.path.relpath(os.path.join(root, f), "images").replace("\\", "/")
        local_imgs.append(rel)

print(f"--- Files currently in images/ ({len(local_imgs)}) ---")
for f in sorted(local_imgs):
    print(f)

# Find all framerusercontent image IDs / filenames
all_html = glob.glob("**/*.html", recursive=True)
all_framer_imgs = set()
for hf in all_html:
    with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    # find images/xxx.jpg or https://framerusercontent.com/images/xxx.jpg
    matches = re.findall(r'(?:images/|framerusercontent\.com/images/)([a-zA-Z0-9_\-]+\.(?:jpg|jpeg|png|webp))', c)
    for m in matches:
        all_framer_imgs.add(m)

print(f"\n--- All Framer / AYLAAA image hashes referenced across all HTML ({len(all_framer_imgs)}) ---")
for m in sorted(all_framer_imgs):
    print(m)
