# AUTHOR Cathryn Callahan 
#
#
#Part B: Unit Test for DFT(x) 
#
# [ ] Write a python calss DFTTestCase() which tests the function DFT of the module
#		w6_Dft.
# Must complete the following tests:
# [X] Ensure that the value returned by DFT is of the correct type and shape
# [ ] Tests the behavior of DFT when invalid inputs are provided (anything other than
#		a numeric sequence)
# [ ] Compares the results of DFT to the values calculated by bumy.fft.fft, which 
#		should match (be almost equal). Must do this for all values of N between
#		2 and 20 (inclusive) using random complex numbers for the sequence. 
# [ ] The random complex numbers can be generated using random.random and must be 
#		in the square with side length 2 centered on the origin.
# [ ] Should compare the results of DFT and fft ten times at each sequence length. 
#		If you only test once, you may miss errors in the DFT function

import unittest

from random import random
from numpy import fft, testing, array, ndarray
from w6_dft import DFT


authors = ['cathcal@bu.edu']	

class DFTTestCase(unittest.TestCase):

	def setUp(self):
		pass
		

	def test_return(self):
		# Tests the behavior of DFT when invalid inputs are provided 
		# Check if an ndarray is returned and if it is of the correct shape
		
		x = [2, 3, 4, 0, 5, 6]
		X = DFT(x)

		self.assertIsInstance(x, ndarray, "Did not return ndarray")
		self.assertEqual(X.shape, (len(x),), "Did not return 1-d array")

	def test_input(self):
		# Test for invalid inputs for DFT (anything other than a numeric sequence)
		
		# Create some invalid inputs
		A = ["5", "6", "7"]			#list containing all strings
		B = [1, 2, "3"]				#list containing 1 string
		C = (1, 2, "3")				#tuple containing strings
		D = array(["5", "6", "7"])	#array containig strings
		E = array([[5,6],[7,8]]) 	# 2 dimensional array

		for test_in in [A, B, C, D, E]:
			error = False
			try:
				DFT(test_in)
			except Exception as e:
				error = True 
				self.assertEqual(type(e), ValueError, "Incorrect input value")
			finally:
				if error == True:
					for error in A:
						msg = "Input is a list containing all strings"	
					for error in B:
						msg = "Input is a list containing a string"
					for error in C:
						msg = "Input is a tuple containing strings"
					for error in D:
						msg = "Input is an array containing strings"
					for error in E:
						msg = "Input is a multidomensional array"	
				self.assertEqual(error, True, msg)

	def test_random_numbers(self):
		# Compares the results of DFT to the values calculated by bumy.fft.fft, which 
		#		should match (be almost equal). Must do this for all values of N between
		#		2 and 20 (inclusive) using random complex numbers for the sequence. 
		# The random complex numbers can be generated using random.random and must be 
		#		in the square with side length 2 centered on the origin.

		for N in range(2,21):
			for t in range(0,10):
				x = []
				for r in range(0,N):
					x.append((random()-0.5)*2 + (random()-0.5)*2j)
					self.assertAlmostEqual(DFT(x), fft.fft(x), 6, "The DFT function does not return an eqivelant answer to the fft.")

	def tearDown(self):
		pass





