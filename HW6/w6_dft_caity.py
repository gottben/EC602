# AUTHOR Cathryn Callahan cathcal@bu.edu
#
#
# Part A: python DFT function
#
# Write a python function DFT of a sequence of complex numbers.
# [X] DFT must return a numpy.ndarray with shape (N,) and this returned value should 
#		match the definition of the DFT provided in this assignemnt
# [X] The function DFT must raise a ValueError exception if the input value x is not 
#	 	a sequence of numerical values
# [X] Must use one and only one import statement
#		from numpy import zeros, exp, array, pi

from numpy import zeros, exp, array, pi, fft



# Compute DFT 
def DFT(x): 
	try:
		N = x.size
		X_k = zeros((N,), dtype="complex")	# gives an array of length N with all 0's
		for k in range(0,N):
			#X_k[k] = 0
			for n in range(0,N):
				X_k[k] += x[n]*exp((-1j*2*pi*n*k)/N)
		return X_k
	except:
		raise ValueError("Input is invalid")
		# exception ValueError is raised when a built-in operation or function receives an 
		# argument that has the right type but an inappropriate value, and the situation is
		# not descibed by a more precise exception




if __name__=="__main__":
	#main()
	# Hard coded array for testing
	x = array([3,4,5], dtype="complex")

	print(DFT(x))

	X = fft.fft(x)
	print(X)

