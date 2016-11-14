# AUTHOR BrianAppleton appleton@bu.edu

import sys
import time


def possible(word, letters, N):
    if len(word) != N:
        return False
    for char in word:
        bank = letters.replace(char, "", 1)
        if len(bank) != len(letters)-1:
            return False
        else:
            letters = bank
    return True

st = time.time()

with open(sys.argv[1], 'r') as r:
    words = frozenset(r.read().split())

while(True):
    letters, N = input().split()
    N = int(N)
    if N == 0:
        break
    word_list = sorted([word for word in words if possible(word, letters, N)])
    print(*word_list + ['.'], sep='\n')

print("Execution time: ", time.time()-st)
