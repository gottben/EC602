#   Pseudo Code Template
#   use any libraries in the anaconda library
#   1st step read in the image

from os import listdir
from skimage.io import imread
import numpy as np
from PIL import Image
import time
import json

[ 0.  1.  2.  2.  3.  3.  4.  4.  4.  3.  3.  3.]
[ 1.  1.  2.  3.  3.  4.  4.  4.  4.  3.  3.  2.]


train_dict_3 = {"train3_1.png": ["edi", "nbl", "ras"],
                "train3_2.png": ["hif", "ssk", "soc"],
                "train3_3.png": ["fsi", "ylc", "elk"],
                "train3_4.png": ["jaa", "nep", "ftl"],
                "train3_5.png": ["bar", "xrb", "eol"],
                "train3_6.png": ["hos", "equ", "era"],
                "train3_7.png": ["tai", "jsr", "usg"],
                "train3_8.png": ["nwl", "loe", "mel"],
                "train3_9.png": ["sho", "dgv", "ole"]}

dict_of_letters = {}

# directory = "."
# For the 3x3 matrix the squares are ~416 high and 360 wide, the distance
# between individual letters is . the white space between the pixels is
# ~44 pixels high and about 90 wide. for the 3x3 start at 568 to 1907.

# when you crop all the images between the rows 568 to 1907 the sets for a
# 3, 4, and 5x5 array become unique
directory = "./train_files"

for file in listdir(directory):
    if file.endswith(".png"):
        print(file)
        img = 255 - imread(directory + "/" + file)
        index = np.where(img[568:1907] == 0)

# print(len(index[0]), len(index[1]))
# print(index)
# print(index2[1])
# print(index3[1])
# print(len(index2[0]), len(index2[1]))
# print(len(index3[0]), len(index3[1]))
# index = set(index)
# index2 = set(index2)
# index3 = set(index3)
# print(len(index))
# print(len(index2))
# print(len(index3))

# if index2 == index3:
#     print("damn")
# else:
#     print("hurray")


#   2nd step, identify if the image is 3, 4, or 5 letter grid
#   Find the coordinates of where each size grid begins and ends.

# a 3x3 array is 1240, 4x4 1229, 5x5 1220. this way was too slow so I
# looked for a faster method. the problem is taking the set of all unique
# elements in an array takes forever. So instead to determine which matrix
# we are dealing with I make the assumption at the very beginning that we
# are dealing with a 3x3 array and crop the image file vertically by
# croping the image from 568 - 1907. Once this is done if I look at where
# the next non-zero vertical index starts it is unique and constant for
# each matrix type. For a 3x3 array the matrix begins at 387 to 1660. for
# a 4x4 it begins at 358 to 1690. for a 5x5 it begins at 348 to 1700.

#   3rd step, crop the image to capture the grid
# this is for a 3x3 array
        data = img[567:1907, 387:1660]
        data[data < 170] = 0
        data[data > 0] = 255
        color = np.array([193, 198, 208])
# print(np.bincount(letter.flatten())[0])
# img2 = Image.fromarray(data[0:415, 0:350], 'RGB')
# # img.show()
# img2.show()
#   4th step, crop the grid to identify each box that contains a letter
# this code is for a 3x3 array
        key = 0
        for j in range(0, 3):
            for i in range(0, 3):
                # img = Image.fromarray(data, 'RGB')
                letter = data[i * (416 + 46):415 + i * (416 + 46),
                              j * (350 + 112): 345 + j * (350 + 112)]
                # img2 = Image.fromarray(letter, 'RGB')
                # # img.show()
                # img2.show()
                # key = np.bincount(letter.flatten())[255]
                # print(roundup(key))
                # key += 1
                # if key in dict_of_letters:
                #     dict_of_letters[key] = dict_of_letters[key] + 1
                # else:
                #     dict_of_letters[key] = 1
                if key not in dict_of_letters:
                    dict_of_letters[key] = letter.flatten()

        for key, value in dict_of_letters.items():
            print(((dict_of_letters[2] - dict_of_letters[key]) ** 2).mean())




#   5th step, identify the letter in each box How to identify the letters.
#   First I need to identify the box around the letter
#
#   Mean-Squared Error
#   Cross Product
#   Sum

#   6th step, create the grid of letters.

#   7th step, identify the length of the words that need to be created.
#   identify patterns in a numpy array to find the number of boxes.

#   8th step, output the results in a json text to match the input file format
#   for problem 13


# s = imread("train3_1.png", as_grey=True)
# plt.imshow(s)
# plt.show()
# Training dictionary of all files
# {filename.png : ['abc', 'gef', 'jkl'],[]...}

train_dict_4 = {"train4_1.png": ["egel", "aaeg", "tvmn", "iear"],
                "train4_2.png": ["beot", "txia", "lfrh", "efes"],
                "train4_3.png": ["yeho", "slnl", "onca", "nnab"],
                "train4_4.png": ["eoca", "wplt", "cimk", "usel"],
                "train4_5.png": ["unod", "leos", "lbrl", "smal"],
                "train4_6.png": ["tofr", "npoi", "ypmj", "tume"],
                "train4_7.png": ["bika", "ttnr", "eezu", "nlzp"]}

train_dict_5 = {"train5_1.png": ["strtb", "imoha", "oranp", "skaep", "hctaf"],
                "train5_2.png": ["oksra", "emfci", "ataon", "nolog", "ppill"],
                "train5_3.png": ["alebu", "lfrnm", "almla", "blsae", "house"],
                "train5_4.png": ["dleif", "bwoow", "hodrc", "rebeo", "llsro"],
                "train5_5.png": ["htroo", "yhpny", "segie", "gnloa", "gnolb"],
                "train5_6.png": ["khpdo", "oiowo", "ellku", "peacb", "retni"],
                "train5_7.png": ["slbop", "siokp", "erleg", "geias", "fruct"],
                "train5_8.png": ["ghnef", "scvla", "eeonb", "llard", "timbe"],
                "train5_9.png": ["tegde", "kjrtu", "nougi", "ketin", "yrinf"],
                "train5_10.png": ["rspls", "eepit", "lorel", "diupe", "boliv"],
                "train5_11.png": ["wigbb", "egana", "tnrcp", "eecec", "nakle"],
                "train5_12.png": ["vittm", "aposi", "nvami", "merep", "oordb"],
                "train5_13.png": ["erost", "atcho", "kshtm", "epeed", "hatch"],
                "train5_14.png": ["nanao", "naobs", "ebroa", "dbeor", "tldsw"]}
