import numpy as np
import matplotlib.pyplot as plt

def load_image(path):
    try:
        img= plt.imread(path)
        print("Image loaded successfully.")
        return img
    except FileNotFoundError:
        print("Image not found!")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None


def print_image(img):
    print("Image Information")
    print(f"Shape      : {img.shape}")
    print(f"Dimensions : {img.ndim}")
    print(f"Data Type  : {img.dtype}")
    print(f"Size       : {img.size}")
    print(f"Memory     : {img.nbytes} bytes")

def show_image(img, title="Image", cmap=None):
    """Display image."""
    plt.figure(figsize=(8,6))
    plt.imshow(img, cmap=cmap)
    plt.title(title)
    plt.axis("off")
    plt.show()

def save_image(img, path, cmap=None):
    plt.imsave(path, img, cmap=cmap)
    print(f"Saved: {path}")

#Testing:
# if __name__=="__main__":
#     img=load_image("../data/meSpain.jpg")
#     if img is not None:
#         print_image(img)
#         show_image(img, "Original Image")
#         save_image(img, "../outputs/original_copy.png")
#OutPut:
# Image loaded successfully.
# Image Information
# Shape      : (720, 1280, 3)
# Dimensions : 3
# Data Type  : uint8
# Size       : 2764800
# Memory     : 2764800 bytes
# Saved: ../outputs/original_copy.png
