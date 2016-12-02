# AUTHOR BrianAppleton appleton@bu.edu

import time
import sys
import itertools
import collections

def possible(word, letters, N):
    #return False    
    if len(word) != N:
        return False
    for char in word:
        if char not in letters: #added to improe execution time
            return False        #added to improve execution time
        bank = letters.replace(char, "", 1)
        if len(bank) != len(letters)-1:
            return False
        else:
            letters = bank
    return True

st = time.time()

with open(sys.argv[1], 'r') as r:
    words = frozenset(r.read().split())

# make a dictionary of frozensets
    dict = {}
    for length in range(1, 29):
        this_set = frozenset([word for word in words if len(word) == length])
        # print(length, len(this_set))
        if (len(this_set) != 0):
            dict[length] = this_set
            length = length+1

print("Digestion time: ", time.time()-st)

while(True):
    letters, N = input().split()
    N = int(N)
    if N == 0:
        break
    if N in dict:
        checkpoint_1 = time.time()
        word_lst = sorted([word for word in dict[N] if possible(word,
                           letters, N)])
        checkpoint_2 = time.time()
        t1 = checkpoint_2 - checkpoint_1
        print("That took", t1, "s")
        print(*word_lst + ['.'], sep='\n')
    else:
        print('.')

print("Execution time: ", time.time()-st)
