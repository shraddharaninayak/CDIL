import os
from PIL import Image

uploaded_dir = r'C:\Users\nshra\.gemini\antigravity\brain\007ee1d0-9729-45f4-9a80-ff5db8d72ad4\.user_uploaded'
uploaded = [
    'media_1792330359401_b56fa670.jpg',
    'media_1792330367250_8f2c6052.jpg',
    'media_1792330367498_d984e1b7.jpg'
]

# Let's inspect exif metadata if any
for up in uploaded:
    p = os.path.join(uploaded_dir, up)
    im = Image.open(p)
    exif = im.getexif()
    print(f"\nExif for {up}:")
    for k, v in exif.items():
        print(f"  {k}: {v}")
