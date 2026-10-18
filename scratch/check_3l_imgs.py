import os
from PIL import Image

for f in ['images/cdil/gallery/3l2.png', 'images/cdil/gallery/3l6.png', 'images/cdil/gallery/3l10.jpeg', 'images/cdil/gallery/av1.jpg', 'images/cdil/gallery/av5.jpg']:
    if os.path.exists(f):
        im = Image.open(f)
        print(f"{f}: size={im.size}, mode={im.mode}")
