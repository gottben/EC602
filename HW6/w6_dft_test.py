import unittest
from random import random
from numpy import fft,testing,array
from w6_dft import DFT
from matplotlib import pyplot as plt

class DFTTestCase(unittest.TestCase):
	def setUp(self):
		pass
	
	def xtest_random_x(self):		
		max_N=20
		
		#for x of length 2 to max_N (inclusive)
		for N in range(2,max_N+1):						
			#generate and test x ten times
			for t in range(0,10):
				#randomly generate x
				x = []
				for i in range(0,N):
					x.append((random()-0.5)*2+(random()-0.5)*2j)
				#test DFT by comparing to fft.fft out to 6 decimal places
				testing.assert_array_almost_equal(DFT(x),fft.fft(x), err_msg='Your results do not agree with numpy.fft.fft',verbose=True)
	def test_dft_return(self):
		pass

	def test_dft_error_hnd(self):
				
		x = ["1","2","3"]
		print(DFT(x))
		
			

	def tearDown(self):
		pass

def plot_rand(x):
	#visualize real and imaginary parts of list x
	#Need to do: from matplotlib import pyplot as plt
	plt.scatter(array(x).real, array(x).imag)
	plt.show()
	

if __name__ == '__main__':
	unittest.main()
