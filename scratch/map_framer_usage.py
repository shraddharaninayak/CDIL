import os, sys, glob, re

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

framer_images = [
    "0Qm4OY4UcG1uVN9g8PnmPNocxc.jpg",
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
    "NcSzfG2MOf7GEGphpuQSIR7Anro.jpg",
    "O5kbDDgCLmTDDKwDeuBnqIDG0Y.jpg",
    "PC9CvBmAqTkuV7nSuyR6cyq5ss.jpg",
    "UoWwFB4OyFidOYYZHb9oAWuk.jpg",
    "XdflLOICap9i3yayush9YNU6o.jpg",
    "XiHIAV0HFUSKlrC1YLOOARfPj4.jpg",
    "Xqe3z10c8F84k5DXRwTjeR3WYCw.jpg",
    "ZQv8BKsWPC72tyN8aojAMg1Xg.jpg",
    "ZiuHJRK3VDqMlK0bXLemGXGx8o.jpg", # Hero image
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

all_html = glob.glob("**/*.html", recursive=True) + glob.glob("**/*.css", recursive=True) + glob.glob("**/*.js", recursive=True)

img_usages = {img: [] for img in framer_images}

for file_path in all_html:
    if "scratch" in file_path or ".system_generated" in file_path:
        continue
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    for img in framer_images:
        if img in content:
            # find context
            matches = [m.start() for m in re.finditer(re.escape(img), content)]
            for pos in matches:
                start = max(0, pos - 100)
                end = min(len(content), pos + 100)
                context = content[start:end].replace("\n", " ").strip()
                img_usages[img].append((file_path, context))

with open("scratch/framer_images_usage.txt", "w", encoding="utf-8") as f:
    for img, usages in img_usages.items():
        f.write(f"\n====================\nImage: {img} (Used in {len(usages)} places)\n")
        print(f"Image {img}: {len(usages)} occurrences")
        for fp, ctx in usages:
            f.write(f"  [{fp}]: {ctx}\n")

print("Usage scan complete. Saved to scratch/framer_images_usage.txt")
