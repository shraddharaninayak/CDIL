import numpy as np
from PIL import Image

uploaded = [
    r'C:\Users\nshra\.gemini\antigravity\brain\007ee1d0-9729-45f4-9a80-ff5db8d72ad4\.user_uploaded\media_1792330359401_b56fa670.jpg',
    r'C:\Users\nshra\.gemini\antigravity\brain\007ee1d0-9729-45f4-9a80-ff5db8d72ad4\.user_uploaded\media_1792330367250_8f2c6052.jpg',
    r'C:\Users\nshra\.gemini\antigravity\brain\007ee1d0-9729-45f4-9a80-ff5db8d72ad4\.user_uploaded\media_1792330367498_d984e1b7.jpg'
]

for idx, p in enumerate(uploaded):
    im = Image.open(p).convert('RGB')
    arr = np.array(im)
    print(f"Uploaded {idx+1}: shape={arr.shape}, mean color={arr.mean(axis=(0,1))}")
