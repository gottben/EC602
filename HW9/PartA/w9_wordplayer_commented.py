# AUTHOR BrianAppleton appleton@bu.edu



import time
import sys
import itertools
import collections

st = time.time()

def possible(word, letters, N):
    #return False    
    if len(word) != N:
        return False
    
    '''
    #This method is super slow. Unsure how to use collections effectively.
    bank = collections.Counter(letters)
    bank.subtract(word)
    return all(count >= 0 for count in bank.values())
    '''
    for char in word:
        if char not in letters: #added to improe execution time
            return False        #added to improve execution time
        bank = letters.replace(char, "", 1)
        if len(bank) != len(letters)-1:
            return False
        else:
            letters = bank
    return True

#Description of algorithm 1
#This is staightforward. Store all words in a dictionary
#Keys are the number of letters in the word
#Contents are sets of words


#Description of algorithm 2
#Goal is to make a dictionary structure:
#   Keys are sorted tuple of letters
#   Contents are sets of the words
#       Not positive about the best way to store the words.
#       Strings? Tuples? TBD.
#The beauty of this approach is that words that are spelled with the same letters and same number of letters are stored together
#This is very fast when r~n in the query for n choose r letters. For n=r, only a single dictionary lookup is needed. Blazing fast.


with open(sys.argv[1], 'r') as r:
    words = list(map(tuple,r.read().split()))
    
alg1_words = {}
alg2_words = {}

for word in words:
        
    n = tuple(sorted(word))         
        
    #Take care of algorithm 1. (Search approach)
    #Keys are number of letters
    x = len(word)
    if x in alg1_words:
        alg1_words[x].add(word)
    else:
        alg1_words[x] = set()
        alg1_words[x].add(word)
    
    #Take care of algorithm 2. (Combination approach)
    #Keys are sorted tuples of letters in the words
    if n in alg2_words:           
        alg2_words[n].add(word) 
    else:
        alg2_words[n] = set()
        alg2_words[n].add(word)


print("Digestion: ", time.time()-st)

while(True):
    letters, r = input().split()
    r = int(r)
    if r == 0:
        break
    
    
    n = len(letters)  
    l2 = tuple(sorted(letters))
    
    #Criteria for using algorithm 1. To be refined based on some experimentation.
    use_alg_1 = (n-r) > 5
    
    if (use_alg_1):
        if (r in alg1_words):
            #Iterate through the dictionary and search for matching words        
            word_lst = sorted([''.join(word) for word in alg1_words[r] if possible(word,
                               letters, r)])
            if len(word_lst) !=0:
                print(*word_lst, sep='\n')
    else:
        #Generate all combinations of n choose r letters and see if they're in the dictionary.
        word_lst = [list(map(''.join,alg2_words[combo])) for combo in itertools.combinations(l2,r) if combo in alg2_words]
        if len(word_lst) != 0:       
            print(*sorted(set(itertools.chain.from_iterable(word_lst))), sep='\n')
    print('.')



print("Execution time: ", time.time()-st)
