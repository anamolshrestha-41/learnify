import numpy as np

def increase_brightness(img, val):
    bright= np.clip(img.astype(np.int16)+val, 0, 255)
    return bright.astype(np.uint8)

def decrease_brightness(img, val):
    dark= np.clip(img.astype(np.int16)-val, 0, 255)
    return dark.astype(np.uint8)
# Pixel Value	Color
# 0	            Black
# 64	       Dark Gray
# 128	       Gray
# 192	       Light Gray
# 255	       White