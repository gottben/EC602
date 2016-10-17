# AUTHOR Alex Bennett gottbenn@bu.edu


from numpy import zeros,exp,array,pi

def DFT(x):
	num_types = ['intc','intp','int8','int16','int32','int64','float16','float32','float64','complex64','complex128']

	test = array(x)
	if test.dtype in num_types:
		N = len(x)
		result = [0]*N
		for i in range(0,N):
			value = 0
			for k in range(0,N):
				value += x[k] * exp((-1j*2*pi*k*i)/N)
			result[i] = value
		return array(result)
	else:
		raise ValueError
