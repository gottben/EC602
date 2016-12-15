# AUTHOR BrianAppleton appleton@bu.edu

import sys
import json

def print_game(grid):
    #print("attempting to print:", grid)
    depth = max(map(len,grid))    
    for row in reversed(range(0,depth+1)):
        row_string = ""        
        for column in grid:
            if len(column)>row:
                row_string = row_string + column[row] + ' '
            else:
                row_string = row_string + '  '
        print(row_string)

three_neighbors = {
    '00': [[1,0],[1,1],[0,1]],
    '10': [[0,0],[0,1],[1,1],[2,1],[2,0]],
    '20': [[1,0],[1,1],[2,1]],
    '01': [[0,0], [1,0], [1,1], [1,2], [0,2]],
    '11': [[0,0],[1,0],[2,0],[0,1],[2,1],[0,2],[1,2],[2,2]],
    '21': [[2,0], [1,0], [1,1], [1,2], [2,2]],
    '02': [[0,1], [1,1], [1,2]],
    '12': [[0,2], [0,1], [1,1], [2,1], [2,2]],
    '22': [[1,2], [1,1], [2,1]]
    }
        
def solve(grid, words, lengths):
    #grid: current game state
    #words: words that have been played
    #lengths: permissible lengths

    '''
    Loop through the dictionary to figure out what words can be played, and then call 
    solve again with all of those words removed
    '''
    if (len(lengths)) == 0:
        print("Hold up. ran out of lengths")
        #print("Words are:" , words)
        solutions.append(' '.join(words))
        return
        #exit()        
    #pick a single word and try to spell it?
    #word = "hoe"
    wl2 = {3:["hoe"], 6:["square"]}
    for word in wl2[lengths[0]]:
        spellings.clear()
        #print("Word is:", word, "Spellings is:", spellings)
        #print("grid is:", grid)
        for col_pos, col in enumerate(grid):
            #print(col_pos, ":", col)
            for row_pos,letter in enumerate(col):
                #print("Element at col", col_pos, "row", row_pos, "is", grid[col_pos][row_pos])
                spell(grid, word, col_pos, row_pos)
        if len(spellings) != 0 and len(word) in lengths:
            print("found", len(spellings), "ways to spell", word, ":")
            for ways in spellings:
                print_game(ways)
                #print_game(collapse(ways))
                lengths_copy = lengths[:]
                lengths_copy.remove(len(word))
                solve(ways, words + [word], lengths_copy)
        

def collapse(grid):
    collapsed = []
    for col in grid:
        collapsed.append([letter for letter in col if letter != ' '])
    return collapsed
    
spellings = []
solutions = []

def spell(grid, letter_list, col, row):
    '''
    Figure out all possible spellings of letter_list that begin at col, row.
    If we find a way to spell it, add an updated game grid to the spellings list.
    '''
    if len(letter_list) == 1 and letter_list[0]==grid[col][row]:
        # If we're on the last letter and it matches the given position in the grid, we've found a way to spell the word        
        #grid[col][row]=" "
        #spellings.append(grid)
        modified_grid = [col[:] for col in grid]
        modified_grid[col][row]=" "
        spellings.append(modified_grid)
    elif grid[col][row] == letter_list[0]:
        # If we're not on the last letter, but the given position matches the next letter in the letter list, 
        # recurse with all of my neighbors to try to complete the word.
        for neighbor in three_neighbors[str(col)+str(row)]:
            modified_grid = [col[:] for col in grid]
            modified_grid[col][row]=" "
            spell(modified_grid, letter_list[1:], neighbor[0], neighbor[1])


    
with open(sys.argv[1], 'r') as read_wl1:
    wl1 = read_wl1.read().split()

with open(sys.argv[2], 'r') as read_wl2:
    wl2 = read_wl2.read().split()

while(True):
    try:    
        game_data = json.loads(input())
        size      = game_data['size']
        lengths   = game_data['lengths']
        grid      = [list(col[::-1]) for col in game_data['grid']]
    except:
        print("\nDone")        
        break
    #print(grid)
    #print(grid[0].reverse())
    #print(grid[0])
    print("Input game:")
    print_game(grid)
    print('\n')
    solve(grid, [], lengths)
    print("Solutions:")
    print(*solutions, sep='\n')
    print('.')