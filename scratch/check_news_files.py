import os, sys

sys.stdout.reconfigure(encoding='utf-8')
WORKSPACE = r"d:\INTERNSHIPS\SOCIAL MEDIA MANANGMENT[SKILLNEX]\WEBSITES\CDIL-Constrution"
os.chdir(WORKSPACE)

for i in range(1, 10):
    for folder in ['images/cdil/icon', 'images/cdil', 'images/cdil/news', 'images']:
        p = os.path.join(folder, f"n{i}.jpeg")
        if os.path.exists(p):
            print(f"n{i}.jpeg found at {p}")
            break
    else:
        print(f"n{i}.jpeg NOT found!")

