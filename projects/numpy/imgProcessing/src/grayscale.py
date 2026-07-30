import numpy as np

def convert_to_grayscale(img):
#Extraction of rgb
    red= img[:, :, 0] #height width red (Red green blue)
    green= img[:, :, 1]
    blue= img[:, :, 2]

#Apply grayscale formula
    gray=(
        0.299 * red + 0.587* green + 0.114*blue
    )

    return gray