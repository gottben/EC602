# AUTHOR BrianAppleton appleton@bu.edu
# AUTHOR Alex Bennett gottbenn@bu.edu
# AUTHOR Cathryn Callahan cathcal@bu.edu

from os import listdir
import re
from skimage.io import imread
import numpy as np
from hashlib import sha1, sha256


directory = '.'


def crop(img):
    img2 = np.sum(img, axis=2)
    nonzero_row = img2.nonzero()[0]
    nonzero_col = img2.nonzero()[1]
    row_min = min(nonzero_row)
    row_max = max(nonzero_row)
    col_min = min(nonzero_col)
    col_max = max(nonzero_col)
    return img[row_min:row_max+1, col_min:col_max+1]


def filename_key(filename):
    return int(re.findall(r'\d+', filename)[0])


def list_key(list_of_filenames):
    return int(re.findall(r'\d+', list_of_filenames[0])[0])

imgs = dict()

for file in listdir(directory):
    if file.endswith(".png"):
        img = crop(255 - imread(directory+"/"+file))
        file_matched = False
        for i in range(0, 4):
            h1 = (sha1(np.rot90(img, i).flatten()).hexdigest())
            h2 = (sha1(np.fliplr(np.rot90(img, i)).flatten()).hexdigest())
            if h1 in imgs:
                imgs[h1].append(file)
                file_matched = True
                break
            elif h2 in imgs:
                imgs[h2].append(file)
                file_matched = True
                break
        if not file_matched:
            imgs[h1] = list([file])

for key in imgs:
    imgs[key].sort(key=filename_key)

with open("answers.txt", 'w') as f:
    for line in sorted(imgs.values(), key=list_key):
        f.write(' '.join(line) + '\n')

print(sha256(open('answers.txt', 'rb').read()).hexdigest())
