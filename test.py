#Author ... 

# w2c_addinghalf.py

import math


def number_from_half(s):
    """return the number represented by s, a binary16 stored as a 4-character hex number"""
    
    bin_string = bin(s)
    if len(bin_string) > 18:
    	print("Please enter a valid input")
    	return 0 

    for i in bin_string[2:len(bin_string)]:
    	print(i) 

    return bin_string

def main():
    """add all binary16 numbers from standard input until a non-number is entered, then print the total.
    Numbers are represented in 4-character hex string format, one per line"""
    A = int(input(),16)
    B = int(input(),16)

    C = A+B 

    Z = number_from_half(A)
    print(len(Z))
    print(A, B, C)
    print(Z)


    # hint1: use int(input(),16)
    # hint2: use try: except: to halt


if __name__ == '__main__':
    main()