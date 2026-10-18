from PIL import Image
import numpy as np

p1 = r'C:\Users\nshra\.gemini\antigravity\brain\007ee1d0-9729-45f4-9a80-ff5db8d72ad4\.user_uploaded\media_1792330359401_b56fa670.jpg'
p2 = r'C:\Users\nshra\.gemini\antigravity\brain\007ee1d0-9729-45f4-9a80-ff5db8d72ad4\.user_uploaded\media_1792330367250_8f2c6052.jpg'
p3 = r'C:\Users\nshra\.gemini\antigravity\brain\007ee1d0-9729-45f4-9a80-ff5db8d72ad4\.user_uploaded\media_1792330367498_d984e1b7.jpg'

im1 = Image.open(p1)
im2 = Image.open(p2)
im3 = Image.open(p3)

print("Im1:", im1.size, im1.format)
print("Im2:", im2.size, im2.format)
print("Im3:", im3.size, im3.format)
