import numpy as np
import matplotlib.pyplot as plt

def creat_histogram(gray):
    # bins → The edges of the histogram bins.
    histogram, bins= np.histogram(gray, bins=256, range=(0, 256))

    #plot histogram
    plt.plot(histogram)
    plt.title("GrayScale Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")

    plt.savefig("histogram.png")
    plt.show()

    return histogram