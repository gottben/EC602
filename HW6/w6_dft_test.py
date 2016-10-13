# AUTHOR BrianAppleton appleton@bu.edu

import unittest
from random import random
from numpy import fft,testing,array,ndarray
from w6_dft import DFT
#from matplotlib import pyplot as plt

class DFTTestCase(unittest.TestCase):
	def setUp(self):
		pass
	
	def test_random_x(self):		
		'''
		Automatically generate a number of test cases for DFT() and compare results to numpy.fft.ftt
		This will generate and test input lists of length 2 to max_N a total of 10 times each
		'''
	
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
		#plot_rand(x)

	def test_dft_return(self):
		'''
		Make sure that the value returned from DFT() is a numpy.ndarray, of length N, and of shape (N,)
		'''		
		
		x = [1,2,3,4,0,5,0]
		X = DFT(x)

		#make sure you give me an ndarray of the proper shape and length
		self.assertIsInstance(X, ndarray, msg='You did not return a numpy.ndarray')
		self.assertEqual(X.shape,(len(x),), msg = 'You must return a one-dimensional array of the same length as the input')		
		
	def test_dft_error_hnd(self):
		'''
		For invalid inputs to DFT, make sure a ValueError is generated
		Also make sure we catch case where no error occurs in DFT() for an invalid input
		This test includes invalid test cases of type list, tuple, and ndarray
		'''		
	
		#create some invalid input test cases		
		w = ["1","2","3"]
		x = ("1", 2, 3)
		y = array(["1","2","3"])
		z = array([[1,2],[3,4]])
				
		w_msg = 'You need to throw an error for lists containing a string'
		x_msg = 'You need to throw an error for tuples containing a string'
		y_msg = 'You need to throw an error for ndarrays containing a string'
		z_msg = 'You need to throw an error for multidimensional arrays'

		#examine errors that are thrown
		for test_case,err_msg in [[w,w_msg],[x,x_msg],[y,y_msg],[z,z_msg]]:
			error_occurred = False	
			try:		
				DFT(w)
				DFT(x)
				DFT(y)
				DFT(z)
			except Exception as e:
				error_occurred = True			
				#did you give me a ValueError? If not, your program is wrong.			
				self.assertEqual(type(e), ValueError, msg='You need to throw a ValueError for invalid input')		
			finally:
				#if your program didn't throw an error AT ALL for invalid input, it's wrong.
				self.assertEqual(error_occurred, True, msg=err_msg)	

	def tearDown(self):
		pass

def plot_rand(x):
	'''
	Use this function to plot an input x for DFT in the complex plane
	Helpful to understand whether random number generation in -1<=Re(x)<=1 and -1<=Im(x)<=1 has been correctly implemented
	Note that <#from matplotlib import pyplot as plt> as well as <plot_rand(x)>, in test_random_x(self), must be uncommented.
	'''	
	plt.scatter(array(x).real, array(x).imag)
	plt.show()
	
if __name__ == '__main__':
	unittest.main()
