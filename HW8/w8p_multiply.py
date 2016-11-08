import numpy 
import sys 

ERROR_ONE = 1
ERROR_TWO = 2
ERROR_THREE = 3
ERROR_FOUR = 4

def main(argv):
	input_length = len(sys.argv) -1 


	if (input_length != 5) and (input_length !=7):
		print("Test 1")
		print("ERROR_ONE: wrong inputs")
		sys.exit(ERROR_ONE)


	if input_length == 7:
		dtype = argv[input_length - 7]
		if(dtype != "int" and dtype !="double"):
			print("Test 2")
			print("ERROR_ONE: wrong inputs")
			sys.exit(ERROR_ONE) 
	elif input_length == 5:
		dtype = argv[input_length - 5]
		if(dtype != "int" and dtype != "double"):
			print("Test 3")
			print("ERROR_ONE: wrong inputs")
			sys.exit(ERROR_ONE) 

	filename1 = argv[input_length-3]
	filename2 = argv[input_length-2]
	filename3 = argv[input_length-1]

	file1 = open(filename1,'r')
	file2 = open(filename2,'r')







if __name__=="__main__":
	main(sys.argv[1:])
