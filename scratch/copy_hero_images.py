import os
import shutil

src_dir = r'C:\Users\nshra\.gemini\antigravity\brain\007ee1d0-9729-45f4-9a80-ff5db8d72ad4\.user_uploaded'
dst_dir = r'images\hero'
os.makedirs(dst_dir, exist_ok=True)

files_map = {
    'media_1792330359401_b56fa670.jpg': 'hero-slide-1.jpg',
    'media_1792330367250_8f2c6052.jpg': 'hero-slide-2.jpg',
    'media_1792330367498_d984e1b7.jpg': 'hero-slide-3.jpg'
}

for src_name, dst_name in files_map.items():
    s = os.path.join(src_dir, src_name)
    d = os.path.join(dst_dir, dst_name)
    shutil.copy2(s, d)
    print(f"Copied {s} -> {d} ({os.path.getsize(d)} bytes)")

print("All hero slides copied successfully!")
