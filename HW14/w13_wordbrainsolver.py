# AUTHORS ALEXBENNETT gottbenn@bu.edu


import json
import numpy as np
from collections import Counter
import sys


the_dict = {}
other_dict = {}

with open(sys.argv[1]) as f:
    for line in f:
        N = len(line) - 1
        word = ''.join(sorted(line[0:N]))
        if N not in the_dict:
            the_dict[N] = {word: [line[0:N]]}
        elif word not in the_dict[N]:
            the_dict[N].update({word: [line[0:N]]})
        else:
            the_dict[N][word].append(line[0:N])

with open(sys.argv[2]) as f:
    for line in f:
        N = len(line) - 1
        word = ''.join(sorted(line[0:N]))
        if N not in other_dict:
            other_dict[N] = {word: [line[0:N]]}
        elif word not in other_dict[N]:
            other_dict[N].update({word: [line[0:N]]})
        else:
            other_dict[N][word].append(line[0:N])

data = []
with open('puzzles.txt') as data_file:
    for line in data_file:
        data.append(json.loads(line))

three_matrix = np.array([[0, 1, 0, 1, 1, 0, 0, 0, 0],
                         [1, 0, 1, 1, 1, 1, 0, 0, 0],
                         [0, 1, 0, 0, 1, 1, 0, 0, 0],
                         [1, 1, 0, 0, 1, 0, 1, 1, 0],
                         [1, 1, 1, 1, 0, 1, 1, 1, 1],
                         [0, 1, 1, 0, 1, 0, 0, 1, 1],
                         [0, 0, 0, 1, 1, 0, 0, 1, 0],
                         [0, 0, 0, 1, 1, 1, 1, 0, 1],
                         [0, 0, 0, 0, 1, 1, 0, 1, 0]])



for game in data:
    N = game["size"]
    word_lengths = game["lengths"]
    for length in word_lengths:
