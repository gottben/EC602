#!/usr/bin/env python3.5
# AUTHOR BrianAppleton appleton@bu.edu
# AUTHOR AlexBennett gottbenn@bu.edu
# AUTHOR CathrynCallahan cathcal@bu.edu
# AUTHOR PreranaHaridoss preranah@bu.edu

# git repository https://github.com/gottben/EC602

# w2c_addinghalf.py

#code by Prerana
'''def number_from_half(s):
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
'''
from math import inf

def number_from_half(s : str):
	
	s = int(s,16)    	
	
	#return the number represented by s, a binary16 stored as a 4-character hex number
	MASK_SIGN     = 0x1   << 15 #sign occupies one bit
	MASK_EXPONENT = 0x1F  << 10 #exponent occupies five bits
	MASK_FRACTION = 0x3FF       #fraction occupies ten bits
	
	#print masks to double-check definitions	
	#print(bin(MASK_SIGN)[2:].zfill(16), " (sign)")
	#print(bin(MASK_EXPONENT)[2:].zfill(16), " (exponent)")
	#print(bin(MASK_FRACTION)[2:].zfill(16), " (fraction)")	

	#display decimal and binary representation of s	
	binary_rep = bin(s)[2:].zfill(16)	
	#print(s, " (s)")	
	#print(binary_rep, " (s in binary)")
	
	#calculate sign, exponent, and fraction parts of s
	sign     = (s & MASK_SIGN)     >> 15
	exponent = (s & MASK_EXPONENT) >> 10
	fraction = (s & MASK_FRACTION)
	
	#display binary representation of masked components of s
	#print("half-precision components of s:")	
	#print(bin(sign)[2:], " (sign)")
	#print(bin(exponent)[2:].zfill(5), " (exponent)")
	#print(bin(fraction)[2:].zfill(10), " (fraction)")

	#Implement half-precision calculation formula from: https://en.wikipedia.org/wiki/Half-precision_floating-point_format
	if   exponent == 0:	
		#print("exponent is zero")		
		sign_value  = (-1)**sign
		significand = fraction / 2**10
		exponent    = 2**(-14)
		result      = sign_value * significand * exponent
	
	elif exponent == 0b11111:
		#print("exponent is all 1's")		
		sign_value  = (-1)**sign
		
		if fraction == 0:
			significand = float('inf')
		else:
			significand = float('NaN')
		
		result      = sign_value * significand
	
	else:
		#print("regular number")		
		sign_value  = (-1)**sign
		significand = 1 + fraction / 2**10
		exponent    = 2**(exponent-15)
		result      = sign_value * significand * exponent
		

	#This significand caluclation method follows from https://en.wikipedia.org/wiki/IEEE_754-1985
	#It seems to match the result given by the significand calculation (1+ fraction / 2**10).
	#significand_2 = 0
	#fraction_string = str(bin(fraction)[2:].zfill(10))
	#for s in range(0,10):
	#	print(fraction_string[s])
	#	significand_2 += int(fraction_string[s])*2**(-(s+1))
	#significand_2 += 1;	
	#print(significand_2)
	
	
	return result

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

#======= Code by Prerana
'''	sum = 0.0;	
	while True:
		try:
			sum+=number_from_half(input())	#this converts the input 
		except:
			break
	print(sum)
'''
    # hint1: use int(input(),16)
    # hint2: use try: except: to halt


#this part allows this script to be used as a standalone program, or inside another script (i.e., import w2c_addinghalf)
if __name__ == '__main__':
    main()

