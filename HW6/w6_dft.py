# AUTHOR Brian Appleton appleton@bu.edu
# AUTHOR Alex Bennett gottbenn@bu.edu
# AUTHOR Cathryn Callahan cathcal@bu.edu

from numpy import zeros,exp,array,pi


def DFT(x):	
	try:
		#Need to fail a dictionary input, all other invalid inputs produce errors
		if type(x) is dict:
			raise Exception()		
	
		#Compute dictionary inputs		
		N = len(x)	
		X = zeros(N, dtype="complex")	
		#compute the DFT of x and store it in X
		for k in range(0,N):
			#for each element in X, perform the DFT summation
			for n,x_n in enumerate(x):								
				X[k]+=x_n*exp(-2j*pi*n*k/N)
		return X
	except:
		raise ValueError("Invalid input encountered")		

def main():
	x = bytearray([1,2,3,4])
	X = DFT(x)
	print("x: ", x)
	print(x[0])
	print("X1: ", X)



if __name__=="__main__":
	main()
