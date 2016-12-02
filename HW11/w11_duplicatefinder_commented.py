# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 08:34:43 2016

@author: brian
"""

from os import listdir
import re
from skimage.io import imread
import matplotlib.pyplot as plt
import numpy as np
import hashlib

import time

st = time.time()

#directory = "example1"
directory = "test_b"
#professor's code takes 2 seconds
#professor actually 

def crop(img):
    #print(img[0])
    img2 = np.sum(img, axis=2)
    #print(img2)
    #print(img2.nonzero())
    nonzero_row = img2.nonzero()[0]
    nonzero_col = img2.nonzero()[1]
    '''
    row_min = min(img2.nonzero()[0])
    row_max = max(img2.nonzero()[0])
    col_min = min(img2.nonzero()[1])
    col_max = max(img2.nonzero()[1])
    '''
    row_min = min(nonzero_row)
    row_max = max(nonzero_row)
    col_min = min(nonzero_col)
    col_max = max(nonzero_col)
    #print(row_min, row_max, col_min, col_max)
    return img[row_min:row_max+1, col_min:col_max+1]


def filename_key(filename):
    return int(re.findall(r'\d+', filename)[0])
def list_key(list_of_filenames):
    return int(re.findall(r'\d+', list_of_filenames[0])[0])
    

imgs = dict()

for file in listdir(directory):
    if file.endswith(".png"):    
        img = crop(255 - imread(directory+"/"+file))
        #print("File", file)
        file_matched = False
        # Generate all 8 possible flips/rotations
        for i in range(0,4):            
            h1 = (hashlib.sha1(np.rot90(img,i).flatten()).hexdigest())
            h2 = (hashlib.sha1(np.fliplr(np.rot90(img,i)).flatten()).hexdigest())
            #print(h1)
            #print(h2)
            if h1 in imgs:
                #print("Found matching hash", h1, "for", file)
                imgs[h1].append(file)
                file_matched = True
                break
            elif h2 in imgs:
                #print("Found matching hash", h2, "for", file)
                imgs[h2].append(file)
                file_matched = True
                break
        if not file_matched:
            imgs[h1] = list([file])
        #print(file, filename_key(file))

#Sort all child lists
for key in imgs:
    imgs[key].sort(key=filename_key)
    #print(imgs[key])  

#Write answers.txt
with open("answers.txt", 'w') as f:
    for line in sorted(imgs.values(), key=list_key):
        f.write(' '.join(line) + '\n')

#Compute SHA256 of answers.txt
print(hashlib.sha256(open('answers.txt','rb').read()).hexdigest())


print("Execution time: ", time.time()-st)

#use sorted(thing, key=f) to sort a dictionary based on the contents
