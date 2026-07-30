from loadImage import(load_image, print_image, show_image, save_image)
from grayscale import convert_to_grayscale
from rotate import  (rotate90, rotate180, rotate270)
from brightness import (increase_brightness, decrease_brightness)
from crop import crop_center
from histogram import creat_histogram

def main():
    print("NumPy Image Processing!!")

    img= load_image("../data/meSpain.jpg")
    if img is None:
        print("Failed to load image.")
        return
    print_image(img)
    # show_image(img, "Original Image")

    print("Converting to grayscale")

    gray= convert_to_grayscale(img)
    save_image(gray, "../outputs/grayscale.png",cmap="gray")
    # show_image(gray, "grayScale", cmap="gray")

    print("Rotating Image")
    rotate1= rotate90(img)
    rotate2=rotate180(img)
    rotate3= rotate270(img)
    save_image(rotate1, "../outputs/rotated90.png")
    save_image(rotate2, "../outputs/rotated180.png")
    save_image(rotate3, "../outputs/rotated270.png")
    # show_image(rotate1, "Rotated 90")
    # show_image(rotate2, "Rotated 180")
    # show_image(rotate3, "Rotated 270")

    print("Brightness Increment And Decrement")
    bright= increase_brightness(img, val=20.2)
    dark= decrease_brightness(img, val=20.2)
    save_image(bright, "../outputs/brigthness.png")
    save_image(dark, "../outputs/darkness.png")
    # show_image(bright, "Brightness Increased")
    # show_image(dark, "Brightness decreased")

    print("Crop image")
    cropped= crop_center(img)
    save_image(cropped, "../outputs/cropped.png")
    # show_image(cropped, "Center crop")

    print("Histogram")
    creat_histogram(gray)
    print("PROJECT COMPLETED SUCCESSFULLY")
    print("All processed images have been saved in outputs")


#Run the program
if __name__=="__main__":
    main()