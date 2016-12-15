# AUTHORS ALEXBENNETT gottbenn@bu.edu


import json
import numpy as np
from collections import Counter
import sys


the_dict = {}
other_dict = {}


def word_search(letters, index, indices, word, s_pos, length, start_i, w_arr):
        word += letters[start_i]
        if len(word) == length:
            w_arr += [word]
            print(w_arr)
        for i in indices:
            if i in index:
                index = np.delete(index, np.where(index == i))
        # print(index)
        for i in range(0, len(index)):
            index = np.where(s_pos[i] == 1)[0]
            indices += [start_i]
            if len(w_arr) == (length*length):
                # print(len(w_arr), (length*length))
                break
            if i == (len(index) - 1):
                indices = []
            word_search(letters, index, indices, word, s_pos, length, i, w_arr)


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

position_dict = {3: np.array([[0, 1, 0, 1, 1, 0, 0, 0, 0],
                              [1, 0, 1, 1, 1, 1, 0, 0, 0],
                              [0, 1, 0, 0, 1, 1, 0, 0, 0],
                              [1, 1, 0, 0, 1, 0, 1, 1, 0],
                              [1, 1, 1, 1, 0, 1, 1, 1, 1],
                              [0, 1, 1, 0, 1, 0, 0, 1, 1],
                              [0, 0, 0, 1, 1, 0, 0, 1, 0],
                              [0, 0, 0, 1, 1, 1, 1, 0, 1],
                              [0, 0, 0, 0, 1, 1, 0, 1, 0]])}

for game in data:
    N = game["size"]
    word_lengths = game["lengths"]
    for y in range(0, N * N):
        letters = ''.join(game["grid"])
        start = letters[y]
        s_pos = position_dict[N]
        index = np.where(s_pos[y] == 1)[0]
        for length in word_lengths:
            word_array = []
            indices = [y]
            if len(letters) == length:
                stop = 1
                break
            word_search(letters, index, indices, word, s_pos, length, y, word_array)
