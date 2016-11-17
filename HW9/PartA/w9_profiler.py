# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 13:39:47 2016

@author: Brian Appleton

Purpose:
    We want to profile execution times for two different wordplayer algorithms.
    The given dictionary is a constant.
    We want to profile exeuction times for n choose r letters
        n is the number of letters we have to make words of r length
        n between 1 and 28, r between 1 and n
        The execution times will ignore the "digestion" time for the big_wordlist,
            because we're interested simply in algorithm efficiency as a function
            of n and r.
    Results will be written to a text file for subsequent analysis.
    
"""

import subprocess
import time
import itertools
import numpy as np
from string import ascii_lowercase
from random import choice
from math import factorial
import matplotlib.pyplot as plt


'''
Measure execution time for program using input_file
Ignore 'digestion' time.
Useful for investigating algorithm efficiency after we've taken
    the digestion hit.
'''
def run_test(program, input_file):
    # Open a process and digest the big_wordlist    
    process = subprocess.Popen(['python3',program,'big_wordlist.txt'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    # Give the program enough time to digest the big wordlist
    # This is not ubiqitous; I know my programs finish in less than this time
    time.sleep(3)
    # Open an input file
    f = open(input_file).read()
    # Get a start time
    st = time.time()
    # Give the program the input file. Note that this MUST contain an 'exit 0' line
    process.communicate(input=f.encode(), timeout=None)
    # Wait until the program exits
    process.wait(timeout=None)
    # Clean up and return the execution time
    exec_time = time.time()-st
    process.terminate()
    return exec_time
    

'''
Get rid of some overhead for random_word at startup
    See random_word function for more info
'''
rel_occur = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,
             0.772,4.025,2.406,6.749, 7.507,1.929,0.095,5.987,6.327,9.056,
             2.758,0.978,2.360,0.150, 1.974,0.074]

weights = (np.array(rel_occur)*100).round().astype(int)
   
weighted_ascii_lowercase = [list(itertools.repeat(let,n)) for let,n in zip(ascii_lowercase,weights)]
weighted_ascii_lowercase = list(itertools.chain.from_iterable(weighted_ascii_lowercase))
'''
'''

def random_word(length):
    '''    
    Below is the most straightforward appraoch. However, not all
        letters occur with the same frequency. Could that matter?
    '''
    #return ''.join(choice(ascii_lowercase) for i in range(length))
    
    '''
    Approach more characteristic of letter occurrence
        re: wikipedia: Letter_frequency
    '''        
    return ''.join(choice(weighted_ascii_lowercase) for i in range(length))

def rm_input_file(filename):
    subprocess.run(['rm',filename])  

def write_input_file(n,r,trials):
    filename = str(n)+'-'+str(r)+'-'+str(trials)+'.txt'  
    f = open(filename, 'w')    
    for i in range(0,trials):
        f.write(random_word(n)+' '+str(r)+'\n')
    f.write('exit 0\n')
    f.close()
    return filename

def nCr(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))


def main():
        
    '''
    User-configurable test parameters:
    '''
    
    # Programs of interest. Set selected_program to one of these.
    combo_program = 'w9_wordplayer_combos.py'
    search_program = 'w9_wordplayer_rev2.py'
    final_program = 'w9_wordplayer_final_profiler.py'
    
    # Selected program
    selected_program = final_program    
    
    # Maximum number of letters to test
    max_n = 28
    
    # Maximum length of words to form
    max_r = max_n
    
    # Number of trials for each n,r pair
    num_trials = 1000
    
    # Combination limit (n choose r). We won't test nCr that exceeds comb_limit
    comb_limit = nCr(30,15)

    '''
    End user-configureable parameters
    '''

    # Organization like: results[n][r] = average execution time, milliseconds
    results = np.zeros((max_n+1,max_r+1), dtype=np.float64)
    
    # Run analysis. This takes a while.
    for n in range(1,max_n+1):
        for r in range(1,n+1):
            if nCr(n,r) <= comb_limit:            
                filename = write_input_file(n,r,num_trials)
                results[n][r] = run_test(selected_program,filename)*1000/num_trials
                rm_input_file(filename)
        print(n/max_n*100, "% complete.")
    
    # Save results for later analysis
    results_fname = 'profiler_' + selected_program + '_' + str(max_n)+'_'+str(max_r)+'_'+str(num_trials)
    np.savetxt(results_fname+'.txt', results, fmt='%.4e')
    
    # Take a quick look at the results
    plt.contourf(results)
    plt.colorbar()
    plt.xlabel('r')
    plt.ylabel('n')
    plt.title('Execution time (ms) for ' + selected_program)
    plt.savefig(results_fname+'.png')


if __name__=="__main__":
    main()