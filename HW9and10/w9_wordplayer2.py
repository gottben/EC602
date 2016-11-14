#!/usr/bin/python3.5
# AUTHOR AlexBennett gottbenn@bu.edu
import sys


def main(argv):
    the_dict = {}

    with open(argv[0]) as f:
        for line in f:
            N = len(line)
            d_words = {}
            if line[0] not in the_dict:
                d_words[N] = [line[0:N - 1]]
                the_dict[line[0]] = d_words
            elif N not in the_dict[line[0]]:
                d_words[N] = [line[0:N - 1]]
                the_dict[line[0]].update(d_words)
            else:
                the_dict[line[0]][N].append(line[0:N - 1])

    l_list, N = input().split()
    for i in range(0, 10000000):
        try:
            result = []

            if N == "0":
                break

            N = int(N) + int(1)

            for key, value in the_dict.items():
                if key in l_list:
                    for word in the_dict[key][N]:
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
            if(N == "0"):
                break

if __name__ == "__main__":
    main(sys.argv[1:])


# #!/usr/bin/python3.5
# # AUTHOR AlexBennett gottbenn@bu.edu
# import sys


# def main(argv):
#     d_words = {}
#     with open(argv[0]) as f:
#         for line in f:
#             N = len(line)
#             if N not in d_words:
#                 d_words[N] = [line[0:N - 1]]
#             else:
#                 d_words[N].append(line[0:N - 1])

#     letter_list, N = input().split()
#     for i in range(0, 10000000):
#         try:
#             result = []

#             if N == "0":
#                 break

#             N = int(N) + int(1)

#             for word in d_words[N]:
#                 new_list = letter_list
#                 for c in word:
#                     if c in new_list:
#                         new_list = new_list.replace(c, "", 1)
#                         if (len(letter_list) - len(word)) == len(new_list):
#                             result += [word]
#                     else:
#                         break

#             result.sort()
#             if result == []:
#                 print(".")
#             else:
#                 print(*result, sep="\n")
#                 print(".")
#             letter_list, N = input().split()
#         except:
#             print(".")
#             letter_list, N = input().split()
#             if(N == "0"):
#                 break

# if __name__ == "__main__":
#     main(sys.argv[1:])
