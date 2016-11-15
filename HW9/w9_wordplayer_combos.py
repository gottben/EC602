# AUTHOR BrianAppleton appleton@bu.edu



import time
import sys
import itertools
import math
import collections

st = time.time()

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

#Goal is to make a dictionary structure:
#   Keys are sorted tuple of letters
#   Contents are the words
#       Not positive about the best way to store the words.
#       Strings? Tuples? TBD.

with open(sys.argv[1], 'r') as r:
    words = list(map(tuple,r.read().split()))
    

dict_words = {}

for word in words:
    n = tuple(sorted(word)) 
    if n in dict_words:           
        dict_words[n].add(word) 
    else:
        dict_words[n] = set()
        dict_words[n].add(word)


print("Digestion: ", time.time()-st)

while(True):
    letters, r = input().split()
    r = int(r)
    if r == 0:
        break
    
    
    n = len(letters)  
    letters = tuple(sorted(letters))
      

    #checkpoint = time.time()    
    
    if n < 9:
        word_lst = [list(map(''.join,dict_words[combo])) for combo in itertools.combinations(letters,r) if combo in dict_words]
        #print(list(itertools.chain.from_iterable(word_lst)))
        #print(set(itertools.chain.from_iterable(word_lst)))
        print(*sorted(set(itertools.chain.from_iterable(word_lst))), sep='\n')
        print('.')
        #print(*sorted(list(itertools.chain.from_iterable(word_lst))), sep='\n')
        #for combo in itertools.combinations(letters,r):
        #    print(combo)
        
    #print("That took ", time.time()-checkpoint, "seconds.")

print("Execution time: ", time.time()-st)
