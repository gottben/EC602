# AUTHOR BrianAppleton appleton@bu.edu

from numpy import zeros,exp,array,pi


def DFT(x):	
	try:
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
	x = array([1,2,3])
	X = DFT(x)
	print("x: ", x)
	print("X1: ", X)

if __name__=="__main__":
	main()
