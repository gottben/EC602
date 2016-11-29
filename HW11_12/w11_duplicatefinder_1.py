# AUTHOR CathrynCallahan cathcal@bu.edu
# w11_duplicatefinder Image Processing

from os import listdir
import re
from skimage.io import imread
import numpy as np
import hashlib
# from PIL import Image

white = np.array([255, 255, 255])
red = np.array([255, 0, 0])
green = np.array([0, 255, 0])
blue = np.array([0, 0, 255])
yellow = np.array([255, 255, 0])

image1 = np.array(imread('cherr2.png'))
print(image1.sum())

# print(image1.flatten())
# print(image1.nonzero())
# print(image1)
# print(image.dtype)
# print(type(image))	# <type 'numpy.ndarray'>
# print(image.shape)	# (5, 5, 3)
# print(image1.getdata())

image2 = np.array(imread('cherry3.png'))
print(image2.sum())
# print(image2)

image3 = np.array(imread('apple9.png'))
print(image3.sum())

image4 = np.array(imread('grap12.png'))
print(image4.sum())

numpix = 0
new_image = [0, 0, 0]
for rgb in image4:
    # print(rgb)
    for p in rgb:
        # print(p)
        # print(type(p))
        if p.all() != white.all():  # gets only color pixels
            new_image += p 			# array of color pixel values
            numpix = numpix + 1		# number of pixels that are NOT white i.e. 3
print("Number of color pixels: ", numpix)
print("Sum of color pixels: ", new_image.sum())

# cs = np.cross(image1, image2)
# print(cs)
