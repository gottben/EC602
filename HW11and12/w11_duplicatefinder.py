# AUTHOR BrianAppleton appleton@bu.edu
# AUTHOR AlexanderBennett gottbenn@bu.edu
# AUTHOR CathrynCallahan  cathcal@bu.edu

from os import listdir
import re
from skimage.io import imread
import numpy as np
import hashlib


result = {}
path = "./test_b/"


def filename_key(filename):
    return int(re.findall(r'\d+', filename)[0])


def list_key(list_of_filenames):
    return int(re.findall(r'\d+', list_of_filenames[0])[0])

for file in listdir(path):
    if file.endswith(".png"):
        the_image = 255 - imread(path + file)
        indices = np.nonzero(the_image)
        the_image = the_image[np.amin(indices[0]):np.amax(indices[0]) + 1,
                              np.amin(indices[1]):np.amax(indices[1]) + 1]

        OL = []
        m_OL = []
        for i in range(0, 4):
            OL += [np.rot90(the_image, i)[0].flatten().tolist()]
            m_OL += [np.rot90(np.fliplr(the_image), i)[0].flatten().tolist()]

        for i in range(0, 4):
            c1 = []
            c2 = []
            c1 += OL[0 - i] + OL[1 - i] + OL[2 - i] + OL[3 - i]
            c2 += m_OL[0 - i] + m_OL[1 - i] + m_OL[2 - i] + m_OL[3 - i]
            if str(c1).strip('[]') in result:
                result[str(c1).strip('[]')].append(file)
                break
            elif str(c2).strip('[]') in result:
                result[str(c2).strip('[]')].append(file)
                break
            elif i == 3:
                result[str(c1).strip('[]')] = [file]
                break

for key in result:
    result[key].sort(key=filename_key)

with open("answers1.txt", 'w') as f:
    for line in sorted(result.values(), key=list_key):
        f.write(' '.join(line) + '\n')

print(hashlib.sha256(open('answers1.txt', 'rb').read()).hexdigest())
