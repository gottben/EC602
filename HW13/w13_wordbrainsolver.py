# AUTHOR BrianAppleton appleton@bu.edu
# AUTHOR Alex Bennett gottbenn@bu.edu
# AUTHOR Cathryn Callahan cathcal@bu.edu

import sys
import json
import copy
import itertools

neighbor_offsets = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1],
                    [0, -1], [1, -1]]
neighbors = dict()
for sz in [3, 4, 5]:
    neighbors[sz] = dict()
    for c in range(0, sz):
        for r in range(0, sz):
            neighbors[sz][str(c)+str(r)] = list()
            for co, ro in neighbor_offsets:
                if(c+co < sz and c+co >= 0):
                    if(r+ro < sz and r+ro >= 0):
                        neighbors[sz][str(c) + str(r)].append([c + co, r + ro])


def solve(grid, words, lengths, wordlist):
    if (len(lengths)) == 0:
        solutions.append(' '.join(words))
        return
    flattened_grid = list(itertools.chain.from_iterable(grid))
    spellings.clear()
    for col_pos, col in enumerate(grid):
        for row_pos, letter in enumerate(col):
            if (lengths[0], grid[col_pos][row_pos]) in wordlist:
                for word in wordlist[(lengths[0], grid[col_pos][row_pos])]:
                    if(possible(word, ''.join(flattened_grid))):
                        spell2(grid, word, word, col_pos, row_pos)
    spellings_copy = copy.deepcopy(spellings)
    for key in spellings_copy:
        for grid in spellings_copy[key]:
            lengths_copy = lengths[:]
            lengths_copy.pop(0)
            solve(grid, words + [key], lengths_copy, wordlist)


def collapse(grid):
    collapsed = []
    for col in grid:
        collapsed.append([letter for letter in col if letter != ' '])
    return collapsed

spellings = dict()
solutions = []


def spell2(grid, word, letter_list, col, row):

    try:
        if len(letter_list) == 1 and letter_list[0] == grid[col][row]:
            modified_grid = [col[:] for col in grid]
            modified_grid[col][row] = " "
            if word not in spellings:
                spellings[word] = list()
            modified_grid = collapse(modified_grid)
            if modified_grid not in spellings[word]:
                spellings[word].append(modified_grid)
        elif grid[col][row] == letter_list[0]:
            for neighbor in my_neighbors[str(col)+str(row)]:
                modified_grid = [col[:] for col in grid]
                modified_grid[col][row] = " "
                spell2(modified_grid, word, letter_list[1:], neighbor[0],
                       neighbor[1])
    except:
        pass


def possible(word, letters):
    for char in word:
        if char not in letters:
            return False
        bank = letters.replace(char, "", 1)
        if len(bank) != len(letters)-1:
            return False
        else:
            letters = bank
    return True

wl1 = dict()
wl2 = dict()

try:
    for filename, wordlist in [[sys.argv[1], wl1], [sys.argv[2], wl2]]:
        with open(filename, 'r') as file:
            for line in file:
                if(len(line) > 1):
                    if (len(line[:-1]), line[0]) not in wordlist:
                        wordlist[(len(line[:-1]), line[0])] = list()
                    wordlist[(len(line[:-1]), line[0])].append(line[:-1])
except:
    pass

while(True):
    try:
        game_data = json.loads(input())
        size = game_data['size']
        lengths = game_data['lengths']
        grid = [list(col[::-1]) for col in game_data['grid']]
    except:
        break
    flattened_grid = list(itertools.chain.from_iterable(grid))
    if len(flattened_grid) != size**2:
        break
    my_neighbors = neighbors[size]
    solutions.clear()
    solve(grid, [], lengths, wl1)
    if (len(solutions) == 0):
        tailored_wl2 = dict()
        for key in wl2:
            if key[0] in lengths and key[1] in flattened_grid:
                for word in wl2[(key[0], key[1])]:
                    if possible(word, ''.join(flattened_grid)):
                        if (len(word), word[0]) not in tailored_wl2:
                            tailored_wl2[(len(word), word[0])] = list()
                        tailored_wl2[(len(word), word[0])].append(word)
        solve(grid, [], lengths, tailored_wl2)
    solutions = sorted(solutions)
    print(*solutions, sep='\n')
    print('.')
