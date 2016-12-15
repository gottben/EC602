#   Pseudo Code Template
#   use any libraries in the anaconda library
#   1st step read in the image

from os import listdir
from skimage.io import imread
import numpy as np
import json


the_alphabet = {"N": [24.0, 63.0, 103.0, 124.0, 135.0, 121.0, 80.0, 36.0],
                "U": [44.0, 49.0, 49.0, 49.0, 49.0, 49.0, 93.0, 115.0],
                "Z": [169.0, 42.0, 9.0, 16.0, 16.0, 16.0, 25.0, 169.0],
                "Y": [64.0, 64.0, 64.0, 36.0, 9.0, 9.0, 9.0, 9.0],
                "V": [49.0, 59.0, 59.0, 59.0, 49.0, 49.0, 25.0, 4.0],
                "W": [61.0, 121.0, 162.0, 169.0, 169.0, 144.0, 68.0, 25.0],
                "G": [80.0, 121.0, 16.0, 15.0, 63.0, 81.0, 92.0, 173.0],
                "T": [186.0, 41.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0],
                "L": [9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 18.0, 127.0],
                "K": [59.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0, 64.0],
                "O": [79.0, 168.0, 64.0, 49.0, 49.0, 59.0, 110.0, 169.0],
                "S": [64.0, 60.0, 11.0, 35.0, 49.0, 16.0, 24.0, 121.0],
                "I": [9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0],
                "X": [75.0, 75.0, 64.0, 36.0, 32.0, 64.0, 64.0, 64.0],
                "A": [3.0, 16.0, 36.0, 49.0, 49.0, 106.0, 196.0, 49.0],
                "P": [117.0, 90.0, 47.0, 73.0, 132.0, 18.0, 9.0, 9.0],
                "C": [83.0, 118.0, 16.0, 15.0, 15.0, 16.0, 58.0, 169.0],
                "E": [159.0, 44.0, 9.0, 74.0, 85.0, 9.0, 21.0, 161.0],
                "J": [9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 16.0, 64.0],
                "D": [142.0, 117.0, 59.0, 49.0, 49.0, 58.0, 93.0, 169.0],
                "M": [9.0, 46.0, 100.0, 169.0, 187.0, 189.0, 144.0, 100.0],
                "F": [159.0, 37.0, 9.0, 32.0, 121.0, 9.0, 9.0, 9.0],
                "B": [113.0, 83.0, 49.0, 81.0, 100.0, 49.0, 70.0, 144.0],
                "Q": [169.0, 196.0, 100.0, 81.0, 121.0, 289.0, 64.0, 25.0],
                "H": [43.0, 45.0, 45.0, 177.0, 193.0, 45.0, 45.0, 45.0],
                "R": [154.0, 99.0, 46.0, 83.0, 146.0, 49.0, 53.0, 56.0]}


def LettWordCount(sorted_edge_values, boxes_height):
    letters, btwn_box, spaces, words = 0, 0, 0, 1
    lets_in_word = []

    if ((boxes_height >= 250) and (boxes_height <= 270)) or (boxes_height >=
                                                             390):
        for pixel in range(0, len(sorted_edge_values) - 1):
            if (sorted_edge_values[pixel] + 1) != sorted_edge_values[pixel +
                                                                     1]:
                diff = sorted_edge_values[pixel + 1] - \
                    (sorted_edge_values[pixel] + 1)
                if diff >= 110 and diff <= 120:
                    letters += 1
                elif diff >= 9 and diff <= 20:
                    btwn_box += 1
                elif diff > 130:
                    spaces += 1
                    lets_in_word.append(letters)
                    letters = 0
                    words += 1
        lets_in_word.append(letters)
    else:
        for pixel in range(0, len(sorted_edge_values) - 1):   # 3x3 and 4x4
            if (sorted_edge_values[pixel] + 1) != sorted_edge_values[pixel +
                                                                     1]:
                diff = sorted_edge_values[pixel + 1] - \
                    (sorted_edge_values[pixel] + 1)
                if diff >= 130 and diff <= 160:
                    letters += 1
                elif diff >= 10 and diff <= 16:
                    btwn_box += 1
                elif diff > 170:
                    spaces += 1
                    lets_in_word.append(letters)
                    letters = 0
                    words += 1
        lets_in_word.append(letters)
    return letters, spaces, words, lets_in_word


def one_row(mid, boxes, left, right):
    box_edges = img[(1920 + mid):(1920 + (mid + 30)), (0 + left):(0 + right)]
    edge_color = np.where(box_edges == [50, 130, 198])
    sorted_edge_values = sorted(set(edge_color[1]))
    return sorted_edge_values, boxes


def two_rows(top, bottom, mid, left, right):
    row_1 = img[1920 + (top + 40):(1920 + (top + 45)), (0 + left):(0 + right)]
    row_2 = img[1920 + (mid + 40):(1920 + (mid + 45)), (0 + left):(0 + right)]
    edge_1 = np.where(row_1 == [50, 130, 198])
    edge_2 = np.where(row_2 == [50, 130, 198])
    sorted_edge_1 = sorted(set(edge_1[1]))
    sorted_edge_2 = sorted(set(edge_2[1]))
    return sorted_edge_1, sorted_edge_2


def three_rows(top, bottom, mid, left, right):
    row_1 = img[1920 + (top + 40):(1920 + (top + 55)), (0 + left):(0 + right)]
    row_2 = img[1920 + (mid + 30):(1920 + (mid + 45)), (0 + left):(0 + right)]
    row_3 = img[1920 + (mid + 90):(1920 + (mid + 95)), (0 + left):(0 + right)]
    edge_1 = np.where(row_1 == [50, 130, 198])
    edge_2 = np.where(row_2 == [50, 130, 198])
    edge_3 = np.where(row_3 == [50, 130, 198])
    sorted_edge_1 = sorted(set(edge_1[1]))
    sorted_edge_2 = sorted(set(edge_2[1]))
    sorted_edge_3 = sorted(set(edge_3[1]))
    return sorted_edge_1, sorted_edge_2, sorted_edge_3


total_dict = {}

directory = "."
dog = listdir(directory)
dog.sort()
for file in dog:
    if file.endswith(".png"):
        img = 255 - imread(directory + "/" + file)
        index = np.where(img[568:1907] == 0)
        if index[1][0] == 387:
            row = 416
            colu = 350
            r_w = 46
            c_w = 112
            rc = 415
            cc = 345
            N = 3
            M1 = 387
            M2 = 1660
            D = 50
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
            D = 28
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
            D = 18

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
                for t in range(0, 8):
                    R = letter[t * (len(letter) // (8)):
                               (t + 1) * (len(letter) // (8))]
                    L = np.count_nonzero(R) // (8 * D)
                    pix_c = np.append(pix_c, L)
                pix_c = pix_c ** 2

                keys = []
                values = []
                for key, value in the_alphabet.items():
                    keys += [key]
                    diff = (value - pix_c)**2
                    for i in range(1, len(diff) + 1):
                        diff[i - 1] = (diff[i - 1] * i * 50 +
                                       diff[i - 1] * 50 * (len(diff) + 1 - 1))
                    values += [diff.mean()]
                the_matrix += keys[values.index(min(values))]

        box_area = img[1920:2440]
        index = np.where(box_area == [50, 130, 198])

        left = min(list(index[1])) - 2
        right = max(list(index[1])) + 2

        top = min(list(index[0]))
        bottom = max(list(index[0]))
        boxes_height = bottom - top

        mid = int((bottom + top) / 2)
        boxes = img[(1920 + top):(1920 + bottom), (0 + left):(0 + right)]

        if boxes_height <= 180:     # single row for 3x3
            # call 3x3 single row function
            sorted_edge_values, boxes = one_row(mid, boxes, left, right)
            letters, spaces, words, lets_in_word = \
                LettWordCount(sorted_edge_values, boxes_height)
            total_ls = lets_in_word
            print(lets_in_word)
        elif (boxes_height >= 310) and (boxes_height <= 330):   # 4x4 2 rows
            # call 4x4 function
            sorted_edge_1, sorted_edge_2 = two_rows(top, bottom, mid, left,
                                                    right)
            letters, spaces, words, lets_in_word = LettWordCount(sorted_edge_1,
                                                                 boxes_height)
            ls = lets_in_word
            letters, spaces, words, lets_in_word = LettWordCount(sorted_edge_2,
                                                                 boxes_height)
            total_ls = ls + lets_in_word
            print(total_ls)
        elif (boxes_height >= 250) and (boxes_height <= 270):    # 5x5 2 rows
            # call 5x5 function
            sorted_edge_1, sorted_edge_2 = two_rows(top, bottom, mid, left,
                                                    right)
            letters, spaces, words, lets_in_word = LettWordCount(sorted_edge_1,
                                                                 boxes_height)
            ls = lets_in_word
            letters, spaces, words, lets_in_word = LettWordCount(sorted_edge_2,
                                                                 boxes_height)
            total_ls = ls + lets_in_word
            print(total_ls)
        elif (boxes_height >= 390):    # 5x5 3 rows
            sorted_edge_1, sorted_edge_2, sorted_edge_3 = \
                three_rows(top, bottom, mid, left, right)
            letters, spaces, words, lets_in_word = LettWordCount(sorted_edge_1,
                                                                 boxes_height)
            ls = lets_in_word
            letters, spaces, words, lets_in_word = LettWordCount(sorted_edge_2,
                                                                 boxes_height)
            ls = ls + lets_in_word
            letters, spaces, words, lets_in_word = LettWordCount(sorted_edge_3,
                                                                 boxes_height)
            total_ls = ls + lets_in_word
            print(total_ls)

        rm = []
        for i in range(0, N):
            rm += [''.join(the_matrix[i * N: (i + 1) * N])]
        result = {}
        result["lengths"] = total_ls
        result["grid"] = rm
        result["size"] = N
        print('"', file, '"', ":", rm)
        with open('data.json', 'a') as outfile:
            json.dump(result, outfile)
