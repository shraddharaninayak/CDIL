import os, sys, glob, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

all_files = glob.glob("**/*.html", recursive=True) + glob.glob("**/*.css", recursive=True) + glob.glob("**/*.js", recursive=True)

img_patterns = re.compile(r'([a-zA-Z0-9_\-\./\\]+\.(?:jpg|jpeg|png|webp|svg|gif)(?:\?[^"\'\s>\)]*)?)', re.IGNORECASE)

all_found = {}

for fpath in all_files:
    if "scratch" in fpath or ".system_generated" in fpath or "images\\cdil" in fpath or "images/cdil" in fpath:
        continue
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    matches = img_patterns.findall(content)
    for m in matches:
        # filter out common non-image file extensions or script names if any
        base = os.path.basename(m.split('?')[0])
        if base not in all_found:
            all_found[base] = []
        all_found[base].append(fpath)

print(f"Total unique image basenames found across codebase: {len(all_found)}")
for base, files in sorted(all_found.items()):
    is_framer = len(base.split('.')[0]) > 20 and not base.startswith("cdil") and not base.startswith("assets_") and not base.startswith("s_")
    print(f"{'[AYLAAA]' if is_framer else '[OTHER] '} {base} (in {len(set(files))} files)")
