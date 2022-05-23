import cv2 as cv
import numpy as np
from os import system
from time import sleep


# accept image from images folder
system('cls')

filepath = "images/ayane.jpg"

img = cv.imread(filepath)

# check if the image is grayscale
if len(img.shape) < 3:
    print("Image is grayscale")
    sleep(3)
    exit()
else:
    print("Image is not grayscale")
    sleep(3)

# coordinate a pixel then print its value
system('cls')
shp = img.shape
eks = int(input("Enter 'x' coordinate value (max value "+str(shp[0])+" ) : "))
way = int(input("Enter 'y' coordinate value (max value "+str(shp[1])+" ) : "))
ch = int(input("""Select channel:
0 - blue
1 - green
2 - red
>> """))

print("Pixel value accessed: ", img.item(eks,way,ch))