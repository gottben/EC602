#!/usr/bin/env python3.5
# AUTHOR BrianAppleton appleton@bu.edu
# AUTHOR AlexBennett gottbenn@bu.edu
# AUTHOR CathrynCallahan cathcal@bu.edu
# AUTHOR PreranaHaridoss preranah@bu.edu

# git repository https://github.com/gottben/EC602

# w2c_addinghalf.py

def number_from_half(s):
        """return the nuimber represented by s, a binary16 stored as a 4-character hex number"""
        binarynum = bin(int(s,16))[2:]

	#converting the number to 16 bit binary 
        binarynum = binarynum.zfill(16)

        sign = int(binarynum[:1],2)
        exponent = int(binarynum[1:6],2)
        fraction = binarynum[6:]

        #print(sign, exponent, fraction)
        if exponent == 0:
            sign_value  = (-1)**sign
            significand = fraction / 2**10
            exponent = 2**(-14)
            number = sign_value * significand * exponent
            #number = (-1**sign)*(2**-14)*(fraction//(2**10))
        elif exponent == 31:
            if fraction == 0:
                number = float("inf")
            else:
                number = float("NaN")
        else:
            sign_value  = (-1)**sign
            significand = 1 + (float(fraction)/2**10)
            exponent = 2**(exponent-15)
            number = sign_value * significand * exponent
            #number = (-1**sign)*(2**(exponent-15))*(1+(fraction//(2**10)))
        #print(sign_value,significand,exponent)
        #print(number)
        return number

def main():
        """add all binary16 numbers from standard input until a non-number is entered, then print the total.
        Numbers are represented in 4-character hex string format, one per line"""
        sum = 0.00
        while 1:
                try:
                        s = str(input("4 character hex number:"))
                        number = number_from_half(s)
                        sum = sum +number
                except:
                        break
        print(sum)

if __name__ == '__main__':
    main()

