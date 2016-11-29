# AUTHOR CathrynCallahan cathcal@bu.edu
# w11_duplicatefinder Image Processing
# Goes through all *.png in directory and sorts into dictionary
# dictionary format:
#    sum_dict {colors.sum(): {numpix: ['filename1', 'filename2']}}
from os import listdir
import re
from skimage.io import imread
import numpy as np
import hashlib
import glob
# from PIL import Image

white = np.array([255, 255, 255])
image_list = []
sum_dict = {}

for filename in glob.glob('*.png'):
    # print(filename)
    features = {}

    image = np.array(imread(filename))
    image_list.append(image)

    numpix = 0
    colors = [0, 0, 0]
    for rgb in image:
        # print(rgb)
        for p in rgb:
            # print(p)
            # print(type(p))
            if p.all() != white.all():  # gets only color pixels
                colors += p 			# array of color pixel values
                numpix = numpix + 1		# number of pixels that are NOT white
    # print("Number of color pixels: ", numpix)
    # print("Sum of color pixels: ", colors.sum())
    if colors.sum() not in sum_dict:
        features[numpix] = [filename]
        sum_dict[colors.sum()] = features
    else:
        # sum_dict[colors.sum()].update(features)
        sum_dict[colors.sum()][numpix].append(filename)

print("sum_dict: ", sum_dict)

# cs = np.cross(image1, image2)
# print(cs)
