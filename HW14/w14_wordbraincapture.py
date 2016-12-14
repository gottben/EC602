#   Pseudo Code Template
#   use any libraries in the anaconda library
#   1st step read in the image

from os import listdir
from skimage.io import imread
import numpy as np
import json


the_alphabet = {"R": [33.0, 9.0, 25.0, 10.0, 9.0],
                "U": [9.0, 9.0, 9.0, 11.0, 25.0],
                "T": [27.0, 1.0, 1.0, 1.0, 1.0],
                "J": [1.0, 1.0, 1.0, 1.0, 9.0],
                "C": [25.0, 4.0, 3.0, 4.0, 28.0],
                "F": [25.0, 1.0, 16.0, 3.0, 1.0],
                "D": [35.0, 12.0, 9.0, 10.0, 36.0],
                "N": [8.0, 24.0, 31.0, 25.0, 9.0],
                "M": [4.0, 24.0, 41.0, 40.0, 25.0],
                "H": [9.0, 9.0, 49.0, 9.0, 9.0],
                "V": [9.0, 11.0, 11.0, 9.0, 1.0],
                "A": [1.0, 9.0, 9.0, 28.0, 16.0],
                "L": [1.0, 1.0, 1.0, 1.0, 16.0],
                "K": [14.0, 16.0, 16.0, 16.0, 16.0],
                "Q": [49.0, 25.0, 25.0, 49.0, 4.0],
                "Y": [16.0, 16.0, 4.0, 1.0, 1.0],
                "E": [25.0, 1.0, 23.0, 1.0, 22.0],
                "B": [25.0, 9.0, 25.0, 9.0, 25.0],
                "O": [25.0, 16.0, 9.0, 16.0, 35.0],
                "S": [16.0, 4.0, 9.0, 4.0, 19.0],
                "W": [16.0, 36.0, 40.0, 25.0, 5.0],
                "I": [1.0, 1.0, 1.0, 1.0, 1.0],
                "P": [25.0, 9.0, 25.0, 4.0, 1.0],
                "G": [25.0, 4.0, 9.0, 16.0, 36.0],
                "X": [16.0, 16.0, 4.0, 16.0, 16.0]}

total_dict = {}

directory = "./train_files2"
dog = listdir(directory)
dog.sort()
for file in dog:
    if file.endswith(".png"):
        img = 255 - imread(directory + "/" + file)
        index = np.where(img[568:1907] == 0)
        # print(file)
        if index[1][0] == 387:
            row = 416         # row changing width
            colu = 350        # column changing width
            r_w = 46          # white space row width
            c_w = 112       # white space column width
            rc = 415          # Row constant dimension
            cc = 345          # Column constant dimension
            N = 3               # array size
            M1 = 387
            M2 = 1660
            D = 270
            F = 2
        elif index[1][0] == 358:
            N = 4
            M1 = 353
            M2 = 1710
            cc = 302
            rc = 293
            r_w = 44
            c_w = 39
            row = 304
            colu = 308
            F = 2
            D = 145  # 120  # 100
        elif index[1][0] == 348:
            N = 5
            M1 = 348
            M2 = 1800
            cc = 230
            rc = 230
            r_w = 50
            c_w = 50
            row = 228
            colu = 228
            F = 2
            D = 95  # 130  # 100

        data = img[569:1910, M1:M2]
        data[data < 170] = 0
        data[data > 0] = 255
        the_matrix = []
        for j in range(0, N):
            for i in range(0, N):
                letter = data[i * (row + r_w):rc + i * (row + r_w),
                              j * (colu + c_w): cc + j * (colu + c_w)]

                indices = np.where(letter == [255, 255, 255])
                letter = letter[np.min(indices[0]): np.max(indices[0]),
                                np.min(indices[1]): np.max(indices[1])]

                pix_c = np.array([])
                for t in range(0, 5):  # 5):   # F * N):
                    R = letter[t * (len(letter) // (5)):    # (F * N)): (5)):
                               (t + 1) * (len(letter) // (5))]    # (F * N))]
                    L = np.count_nonzero(R) // (5 * D)    # (N * D)
                    pix_c = np.append(pix_c, L)
                pix_c = pix_c ** 2  # 8 , 2

                keys = []
                values = []
                for key, value in the_alphabet.items():
                    keys += [key]
                    diff = (value - pix_c)**2
                    for i in range(1, len(diff)+1):
                        diff[i-1] = (diff[i-1]*i*50 +
                                     diff[i-1]*50*(len(diff) + 1 - 1))
                    values += [diff.mean()]
                the_matrix += keys[values.index(min(values))]

        rm = []
        for i in range(0, N):
            rm += [''.join(the_matrix[i * N: (i + 1) * N])]
        # print(the_matrix)
        result = {}
        result["lengths"] = []
        result["grid"] = rm
        result["size"] = N
        print('"', file, '"', ":", rm)
