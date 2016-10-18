# AUTHOR BrianAppleton appleton@bu.edu

import unittest
from random import random
from numpy import fft,testing,array,ndarray
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
		Test this for a list and a bytearray; tuples and numpy.array tests might be added in the future. Together these constitute the list of valid inputs.
		'''		
		
		x = [1,2,3,4,0,5,0]
		X = DFT(x)

		#make sure you give me an ndarray of the proper shape and length
		self.assertIsInstance(X, ndarray, msg='You did not return a numpy.ndarray')
		self.assertEqual(X.shape,(len(x),), msg = 'You must return a one-dimensional array of the same length as the input')

		y = bytearray([1,2,3,4,0,5,0])
		Y = DFT(y)

		#make sure you give me an ndarray of the proper shape and length
		self.assertIsInstance(Y, ndarray, msg='You did not return a numpy.ndarray')
		self.assertEqual(Y.shape,(len(y),), msg = 'You must return a one-dimensional array of the same length as the input')	
			
		
	def test_dft_error_hnd(self):
		'''
		For invalid inputs to DFT, make sure a ValueError is generated
		Also make sure we catch case where no error occurs in DFT() for an invalid input
		This test includes invalid test cases of type list, tuple, and ndarray
		'''		
		
		#self.assertRaises(ValueError, DFT(None))		

		#create some invalid input test cases		
		r = True		
		s = None
		t = 1	
		u = "fail"		
		v = {1:4,6:7}		
		w = ["1","2","3"]
		x = ("1", 2, 3)
		y = array(["1","2","3"])
		z = array([[1,2],[3,4]])
				
		w_msg = 'You need to throw an error for lists containing a string'
		x_msg = 'You need to throw an error for tuples containing a string'
		y_msg = 'You need to throw an error for ndarrays containing a string'
		z_msg = 'You need to throw an error for multidimensional arrays'
		v_msg = 'You need to throw an error for dictionaries'
		u_msg = 'You need to throw an error for a string'
		t_msg = 'You need to throw an error for an integer'
		s_msg = 'You need to throw an error for None'
		r_msg = 'You need to throw an error for a boolean'

		#examine errors that are thrown
		for test_case,err_msg in [[w,w_msg],[x,x_msg],[y,y_msg],[z,z_msg],[v,v_msg],[u,u_msg],[t,t_msg],[s,s_msg],[r,r_msg]]:
			error_occurred = False	
			try:		
				DFT(test_case)
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
	plt.suptitle("Randomly-generated complex input for DFT")
	plt.xlabel("Re(x)")
	plt.ylabel("Im(x)")
	plt.grid(True)
	plt.show()
	
if __name__ == '__main__':
	from w6_dft import DFT
	unittest.main()
