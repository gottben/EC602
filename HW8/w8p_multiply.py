import numpy as np
import sys 

ERROR_ONE = 1
ERROR_TWO = 2
ERROR_THREE = 3
ERROR_FOUR = 4

def main(argv):
	input_length = len(argv)
	#print(input_length)


#	Test for first error 


	if (input_length != 5) and (input_length !=7):
		#print("Test 1")
		#print("ERROR_ONE: wrong inputs")
		exit(ERROR_ONE)

	# # 	Shape matrices 
	if input_length == 7:
		M = int(argv[1])
		N = int(argv[2])
		T = int(argv[3])
	elif input_length == 5:
		M = int(argv[1])
		N = int(argv[1])
		T = int(argv[1])

	if(M < 1 or N <1 or T < 1):
		exit(ERROR_ONE)

	if input_length == 7:
		dtype = argv[0]
		if(dtype != "int" and dtype !="double"):
			#print("Test 2")
			#print("ERROR_ONE: wrong inputs")
			exit(ERROR_ONE) 
	elif input_length == 5:
		dtype = argv[0]
		if(dtype != 'int' and dtype != 'double'):
			#print("Test 3")
			#print("ERROR_ONE: wrong inputs")
			exit(ERROR_ONE) 

	if argv[0] == 'int':
		data_type = int 
	elif argv[0] == 'double':
		data_type = float
	else: 
		#print("ERROR_ONE: wrong inputs")
		exit(ERROR_ONE)


#	Test for second error and read files into vectors

	try:
		filename1 = argv[input_length-3]
		filename2 = argv[input_length-2]
		output_file = argv[input_length-1]
	except:
		exit(ERROR_ONE)


	try:
		M1 = np.loadtxt(filename1,dtype = data_type)
		M2 = np.loadtxt(filename2, dtype = data_type)
	except: 
		#print("ERROR_TWO: one or two input files does not exist")
		exit(ERROR_THREE)


	try: 
		M1.shape = (M,N)
		M2.shape = (N,T)
	except:
		#print("ERROR_FOUR: cannot form matrix")
		exit(ERROR_FOUR)

#	Multiply and create output matrix
	M3 = np.mat(M1)*np.mat(M2)
	try:
		np.savetxt(output_file, M3, fmt='%s', delimiter = ' ', newline = '\n')
	except:
		#print("ERROR_FOUR: cannot write to file")
		exit(ERROR_FOUR)



if __name__=="__main__":
	main(sys.argv[1:])
