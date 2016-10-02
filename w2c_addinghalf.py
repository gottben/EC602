#Author ... 

# w2c_addinghalf.py

import math 

positive = 0 

def number_from_half(s : str):
    """return the number represented by s, a binary16 stored as a 4-character hex number"""
    
    bin_string = bin(s)

    sign_mask = 0x1 << 15
    expo_mask = 0x1f << 10


    sign = (s & sign_mask) >> 15
    expo = (s & expo_mask) >> 10
    frac = s & (2**10 - 1)

    #print(sign)

    significant_bit = frac & 1 
    if(expo == 0): 
    	if (frac == 0):
    		#print('help')
    		return -0.0 if sign else 0.0
    	else:
    		#print('help1')
    		#print((-1)**sign)
    		#print((-1**sign)* frac / 2**10 * 2**-14)
    		return ((-1)**sign)* frac / 2**10 * 2**-14
    elif(expo == 0x1f):
    	if(frac == 0):
    		#print('help2')
    		return float('-inf') if sign else float('inf')
    	else:
    		#print('help3')
    		return float('nan') 
   # print((-1**sign) * 2**(expo - 15) * (1 + frac/2**10))
    return ((-1)**sign) * 2**(expo - 15) * (1 + frac/2**10)

def main():
    """add all binary16 numbers from standard input until a non-number is entered, then print the total.
    Numbers are represented in 4-character hex string format, one per line"""
    summation = 0
    while 1:
    	try:
    		#if math.isnan(summation += number_from_half(int(input(),16))):

    		#print(summation)
    		summation += number_from_half(int(input(),16))
    		#print(summation)
    	except:
    		print(summation)
    		return summation
   



    # hint1: use int(input(),16)
    # hint2: use try: except: to halt


if __name__ == '__main__':
    main()