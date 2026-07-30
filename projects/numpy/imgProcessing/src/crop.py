import numpy as np

def crop_center(img):

    #image dimension
    height, width= img.shape[:2]

    #compute crop noundaries
    top=height//4
    bottom=3*height//4
    left=width//4
    right= 3*width//4

    # crop 
    return img[top:bottom, left:right]
