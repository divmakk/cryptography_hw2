import numpy as np
from PIL import Image

img1 = Image.open("image1.png").convert("L")
img2 = Image.open("image2.png").convert("L")

a1 = np.array(img1, dtype=np.uint8)
a2 = np.array(img2, dtype=np.uint8)

b1 = (a1 == 255).astype(np.uint8)
b2 = (a2 == 255).astype(np.uint8)

d = b1 ^ b2 

out = (d * 255).astype(np.uint8)
Image.fromarray(out, mode="L").save("xor_leak.png")