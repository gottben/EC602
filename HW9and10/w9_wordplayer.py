# AUTHOR BrianAppleton appleton@bu.edu
# AUTHOR AlexanderBennett gottbenn@bu.edu
# AUTHOR CathrynCallahan cathcal@bu.edu

import sys
import itertools


the_dict = {}

with open(sys.argv[1]) as f:
    for line in f:
        N = len(line) - 1
        word = ''.join(sorted(line[0:N]))
        if N not in the_dict:
            the_dict[N] = {word: [line[0:N]]}
        elif word not in the_dict[N]:
            the_dict[N].update({word: [line[0:N]]})
        else:
            the_dict[N][word].append(line[0:N])

while(True):
    l_list, N = input().split()
    if N == "0":
        break
    try:
        result = []
        u_comb = []
        N = int(N)

        if len(l_list) - N > 5:
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
        if result != []:
            print(*result, sep="\n")
        print(".")
    except:
        print(".")
