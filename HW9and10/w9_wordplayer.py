#!/usr/bin/python3.5
# AUTHOR AlexBennett gottbenn@bu.edu
import sys


def main(argv):
    the_dict = {}

    with open(argv[0]) as f:
        for line in f:
            N = len(line)
            d_words = {}
            if N not in the_dict:
                d_words[line[0]] = [line[0:N - 1]]
                the_dict[N] = d_words
            elif line[0] not in the_dict[N]:
                d_words[line[0]] = [line[0:N - 1]]
                the_dict[N].update(d_words)
            else:
                the_dict[N][line[0]].append(line[0:N - 1])

    l_list, N = input().split()
    while(N != "0"):
        try:
            result = []

            N = int(N) + int(1)

            for key, value in the_dict[N].items():
                if key in l_list:
                    for word in value:
                        n_list = l_list
                        for c in word:
                            if c in n_list:
                                n_list = n_list.replace(c, "", 1)
                                if (len(l_list) - len(word)) == len(n_list):
                                    result += [word]
                            else:
                                break

            result.sort()
            if result == []:
                print(".")
            else:
                print(*result, sep="\n")
                print(".")
            l_list, N = input().split()
        except:
            print(".")
            l_list, N = input().split()

if __name__ == "__main__":
    main(sys.argv[1:])
