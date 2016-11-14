# AUTHOR BrianAppleton appleton@bu.edu

import sys
import itertools


def poss(word, letters, N):
    if (len(word) != N):
        return False
    for char in word:
        bank = letters.replace(char, "", 1)
        if len(bank) != len(letters)-1:
            return False
        else:
            letters = bank
    return True

with open(sys.argv[1], 'r') as r:
    words = frozenset(r.read().split())

    dict = {}
    for word in words:
        key1 = len(word)
        key2 = ''.join(sorted(set(word)))
        if key1 in dict:
            if key2 in dict[key1]:
                dict[key1][key2].add(word)
            else:
                dict[key1][key2] = set([word])
        else:
            dict[key1] = {key2: set([word])}

learned_sets = {}
while(True):
    letters, N = input().split()
    N = int(N)
    if N == 0:
        break
    letter_set = set(letters)

    if N in dict:
        key_learning = (N, ''.join(sorted(letter_set)))
        if key_learning in learned_sets:
            pw = learned_sets[key_learning]
        else:
            pw = set()
            for x in dict[N].keys():
                if set(x).issubset(letter_set):
                    pw = pw | dict[N][x]
            learned_sets[key_learning] = pw
    wl = list(itertools.filterfalse(lambda x: not poss(x, letters, N), pw))
    if len(wl) > 0:
        print(*sorted(wl) + ['.'], sep='\n')
    else:
        print('.')
