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

# coordinate a pixel then print its value
system('cls')
shp = img.shape
print("Access a pixel")
eks = int(input("Enter 'x' coordinate value (max value "+str(shp[0])+" ) : "))
way = int(input("Enter 'y' coordinate value (max value "+str(shp[1])+" ) : "))
ch = int(input("""Select channel:
0 - blue
1 - green
2 - red
>> """))

akses = img.item(eks, way, ch)

# modify a pixel value
system('cls')
shp = img.shape
print("Modify a pixel")
eks = int(input("Enter 'x' coordinate value (max value "+str(shp[0])+" ) : "))
way = int(input("Enter 'y' coordinate value (max value "+str(shp[1])+" ) : "))
blu = int(input("Enter blue channel value: "))
grin = int(input("Enter green channel value: "))
red = int(input("Enter red channel value: "))

system('cls')

print("Outputs:")

print("\nAccessed Pixel Value:", akses)

print("Pixel value before modify:", img[eks, way])  # print before modifying

# modifying
img.itemset((eks, way, 0), blu)
img.itemset((eks, way, 1), grin)
img.itemset((eks, way, 2), red)

print("Pixel value after modified:", img[eks, way])  # print after modified

# image dimensions
wid = 300
hayt = 300

if wid > shp[1] or hayt > shp[0]:
    print("Set Image Dimension: Out of bounderies")
else:
    print("Set Image Dimension: Within the bounderies")

# total pixel count

pix = 1683001

if pix > img.size: print("Set pixel: Higher than the pixel count")
elif pix < img.size: print("Set pixel: Lower than the pixel count")
else: print("Set pixel: Equal to the pixel count")

print("Image Data Type:", img.dtype)