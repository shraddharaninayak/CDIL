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
    "AjQp2dUVDzqj5LSzanz06FUWbU.jpg",
    "HrKKcFQ3DVsJ9P9jkiiXZh5juE.jpg",
    "IjxtO3SV152XjF7XWHpYAOLUJMg.jpg",
    "KcexKs0xLJniVsGT2OwYYSwL4I.jpg",
    "O5kbDDgCLmTDDKwDeuBnqIDG0Y.jpg",
    "PC9CvBmAqTkuV7nSuyR6cyq5ss.jpg",
    "XdflLOICap9i3yayush9YNU6o.jpg",
    "XiHIAV0HFUSKlrC1YLOOARfPj4.jpg",
    "Xqe3z10c8F84k5DXRwTjeR3WYCw.jpg",
    "ZiuHJRK3VDqMlK0bXLemGXGx8o.jpg",
    "c2ENN0w6FyOgaTz5OytE1ye0flo.jpg",
    "cCYedN2F79ejMcgWgXCOfU73a8.jpg",
    "gynlhAwJLfMLFJEhh4xjXpPCPQ.jpg",
    "hntiEJ8LUjfWfuFyUy2KSsGrqDE.jpg",
    "htqVoCdq8HKHyjSa8i9Qo4yCU8w.jpg",
    "kLLCGbGu6fjY89G5W0bfPMNl6HA.png",
    "rURwvrDaaU0CEAVcJ7aKoh4CFo.jpg",
    "uCarZ02wIibfZsAt8yCmnDEAwk.jpg",
    "up3HHBNHrsLu5dUK10kakAq7Y.jpg",
    "uzcv3F3dlHJZ9GsmosUxczA3lU.jpg",
    "yp7gODnubKyOzhmsbHhfNC0RPeI.jpg"
]

all_html = glob.glob("**/*.html", recursive=True)

results = {}
for img in framer_images:
    results[img] = []
    for hf in all_html:
        with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
            c = f.read()
        if img in c:
            # find all tags or img elements containing this image
            # look for alt="..."
            alts = re.findall(rf'<img[^>]+{re.escape(img)}[^>]+alt=["\']([^"\']*)["\']', c)
            if not alts:
                alts = re.findall(rf'alt=["\']([^"\']*)["\'][^>]+{re.escape(img)}', c)
            # look for closest data-framer-name
            data_names = []
            for m in re.finditer(re.escape(img), c):
                idx = m.start()
                sub = c[max(0, idx-400):idx]
                framer_name = re.findall(r'data-framer-name=["\']([^"\']+)["\']', sub)
                if framer_name:
                    data_names.append(framer_name[-1])
            results[img].append({
                'file': hf,
                'alts': set(alts),
                'framer_names': set(data_names)
            })

for img, occurrences in results.items():
    if not occurrences:
        continue
    print(f"\n==========================================")
    print(f"IMAGE: {img}")
    for occ in occurrences:
        print(f"  File: {occ['file']} | Alts: {occ['alts']} | Components: {occ['framer_names']}")
