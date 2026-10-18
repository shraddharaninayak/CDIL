import os, sys, glob, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

framer_images = [
    "1WE8VVvhM5ILXM8zlwp4JTbDcg.jpg",
    "2TOsdQ0l1UFLP08nIBuvp5YE0.jpg",
    "3fSSK360dEzMizQHdrXt1Dbhw0.jpg",
    "44IzJSemp73a6BgdeKY6t9A1Xk.jpg",
    "6gAYT1fHxFFVy3Ei5y2n9JlNs.jpg",
    "7Ob5jUxK0GfjhrfOQIFfzBI668o.jpg",
    "AjQp2dUVDzqj5LSzanz06FUWbU.jpg"
]

all_html = glob.glob("**/*.html", recursive=True)

for img in framer_images:
    print(f"\n==========================================")
    print(f"IMAGE: {img}")
    for hf in all_html:
        with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
            c = f.read()
        if img in c:
            idx = c.find(img)
            snippet = c[max(0, idx-200):min(len(c), idx+200)]
            alts = re.findall(r'alt=["\']([^"\']*)["\']', snippet)
            print(f"  File: {hf} | Alts: {alts}")
