#!/usr/bin/python3.5
# AUTHOR AlexBennett gottbenn@bu.edu
import sys
import itertools


def main(argv):
    the_dict = {}

    with open(argv[0]) as f:
        for line in f:
            N = len(line) - 1
            d_words = {}
            word = ''.join(sorted(line[0:N]))
            if N not in the_dict:
                d_words[word] = [line[0:N]]
                the_dict[N] = d_words
            elif word not in the_dict[N]:
                d_words[word] = [line[0:N]]
                the_dict[N].update(d_words)
            else:
                the_dict[N][word].append(line[0:N])

    l_list, N = input().split()

    while(N != "0"):
        try:
            result = []
            u_comb = []
            N = int(N)

            if N > 8:
                for key, value in the_dict[N].items():
                    n_list = l_list
                    for char in key:
                        if char in n_list:
                            n_list = n_list.replace(char, "", 1)
                            if (len(l_list) - N) == len(n_list):
                                result += value
                        else:
                            break
            else:
                for i in itertools.combinations(list(l_list), N):
                    i = sorted(i)
                    u_comb += [''.join(i)]

                u_comb = list(set(u_comb))
                u_comb.sort()

                for comb in u_comb:
                    if comb in the_dict[N]:
                        result += the_dict[N][comb]

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
