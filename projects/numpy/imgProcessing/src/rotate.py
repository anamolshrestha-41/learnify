import numpy as np

#np.rot90(image, k)

def rotate90(img):
    rotn90= np.rot90(img, 1)
    return rotn90

def rotate180(img):
    rotn180= np.rot90(img, 2)
    return rotn180

def rotate270(img):
    rotn270= np.rot90(img, 3)
    return rotn270