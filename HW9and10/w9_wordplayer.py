# AUTHOR AlexBennett gottbenn@bu.edu
import sys


def main(argv):
    # place holder in the meantime
    dict_of_words = {}
    dict_of_first_char = {}
    dict_of_indexes = {}

    with open(argv[0]) as f:
        for line in f:
            if not len(line) in dict_of_words:
                dict_of_words[len(line)] = [line[0:len(line) - 1]]
            else:
                dict_of_words[len(line)].append(line[0:len(line) - 1])

# Now I want to organize the words associated with each key in
# alphabetical order. Keeping track of where the first char in each
# word changes.
    for key, value in dict_of_words.items():
        # This part of for loop sorts the words in each value list
        value.sort()
        dict_of_words[key] = value
        # Now we prepare our values such that each of them
        index = 0
        first_word = value[0]
        dict_of_first_char[key] = [first_word[0]]
        dict_of_indexes[key] = [index]
        # This for loop creates two arrays one for each first character in
        # a word for a specific key, one indexing where that first character
        # changes in this list. I am doing this for optimized searches.
        for words in value:
            if first_word[0] < words[0]:
                first_word = words
                dict_of_first_char[key].append(first_word[0])
                dict_of_indexes[key].append(index)
            index += 1

#   Time to start doing some processing on this data.
# let us assume some constant inputs
    letter_list, N = input().split()
    N = int(N)

    while(N != 0):
        N = N + 1
        words = dict_of_words[N]
        F_characters = dict_of_first_char[N]
        indexes = dict_of_indexes[N]

        check_words = []
#   ''.join(set(letter_list)) is there to get only the unique letters in
#   the letter list
        for c in ''.join(set(letter_list)):
            if c in F_characters:
                the_index = F_characters.index(c)
                check_words += (words[indexes[the_index]:
                                      indexes[the_index + 1]])

#   This for loop actually checks to see if the words match the letters
#   For every letter in a word that matches a word in the letter_list
#   it will remove that letter form the letter list and check to see if any
#   other words match that letter.
        result = []
        for words in check_words:
            Correct = N - 1
            new_list = letter_list
            for c in words:
                if c in new_list:
                    Correct -= 1
                    new_list = new_list.replace(c, "", 1)
                if Correct == 0:
                    result += [words]
        result.sort()
        print("\n".join(result))
        print(".")

        letter_list, N = input().split()
        N = int(N)


if __name__ == "__main__":
    main(sys.argv[1:])
