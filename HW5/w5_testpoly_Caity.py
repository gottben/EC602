# AUTHOR Cathryn Callahan cathcal@bu.edu
#
# w5_testpoly.py
#
#
# SHOULD BE TESTING THE FOLLOWING:
# [X] Test constructor which takes a sequence and assigns the coefficients in the
#		natural (descending order). So Polynomial([4,-9,5.6]) should make 4x^2 -9x + 5.6
# [X] Test addition and subtraction of polynomials using + and -
# [X] Test multiplication of polynomials using *
# [X] Test testing for equality of polynomials using ==
# [X] Test an efficient mechanism for handling sparse polynomials
# [ ] Test negative powers in the polynomial, ie. p[x] = x^-1
# [X] Test evaluation of the polynomial using an eval method like p.eval(2.1)
# [X] Test accessing and modifying the coefficients using [ ]. So p[2] should
#		be the coefficient of x^2 and p[8]=12 should set the coefficient of x^8 to 12
# [X] Test a derivative method p.deriv() which returns the derivative of the polynomial

import unittest
import importlib
import glob
import sys

from w4_polynomial import Polynomial

# The tester includes the author list as part of the JSON file output
authors = ['cathcal@bu.edu']	

class PolynomialTestCase(unittest.TestCase):

	# setUp method is called prior to each test method
	# Initialize data structures before carrying out a test
	def setUp(self):
		# Poly with only integer components
		self.A = Polynomial([2, 4, 6, 8, 0, 10])
		# Poly with integer and complex components
		self.B = Polynomial([3, 2+5j, -1, -4-7j])
		# Poly with float componetns
		self.C = Polynomial([2.004, -3.345, 4.125, 6.000002, 0, 3.000256])

		self.D = Polynomial([1,2,3,4])

		test = self.A + self.C
		test = self.C + self.A
		test = self.A * self.D
		test = self.D * self.A
		test = self.A.eval(2)
		test = self.B - self.D
		test = self.A.deriv()
		test = self.D.deriv()
		test = self.B[2] + self.B[3]

	
	def test_init(self):
		# Test that object is an instance of the Polynomial class
		self.assertIsInstance(self.A, Polynomial,"Object is in Class")
		self.assertIsInstance(self.B, Polynomial,"Object is in Class")
		self.assertIsInstance(self.C, Polynomial,"Object is in Class")
		try:
			Polynomial([],{})
			raise Exception('Error')
		except Exception as e:
			if str(e) == 'Error':
				raise Exception('Too many arguments for input')
			

	def test_setitem(self):
		# Test to see if polynomial created with constructor is equal to poly created with set value
		poly1 = Polynomial([])
		for i in range(0,4):
			poly1[i] = 4-i
		self.assertEqual(self.D, poly1, "Polys are Equal")
			 
		self.A[0] = 0
		self.B[1] = -1+2j
		self.assertEqual(self.A[0], 0, "Items are equal")
		self.assertEqual(self.B[1], -1+2j, "Items are equal")

	def test_getitem(self):
		self.assertEqual(self.A[2], 8)
		self.assertEqual(self.A[1500], 0)
		self.assertEqual(self.B[2], 2+5j)
		# something for negative exponents

	def test_eval(self):
		# Add a for loop?
		self.assertEqual(self.A.eval(2), 218)
		self.assertEqual(self.B.eval(1), -2j)
		self.assertEqual(self.D.eval(2), 26) 


	def test_add(self):
		for x in range(0,50):
			self.assertEqual((self.A+self.D).eval(x), (self.A.eval(x)+self.D.eval(x)))
			self.assertEqual((self.B+self.D).eval(x), (self.B.eval(x)+self.D.eval(x)))
		# Test to make sure it is handling 0 correctly by removing exponents with coeff of zero
		poly = Polynomial([-1, -2, -3, -4])
		d = self.D + poly
		self.assertEqual(d, Polynomial([]))
		#Same as
			#self.assertEqual((self.A+self.D).eval(2), 244)
			#self.assertEqual((self.B+self.D).eval(2), 52+13j)
		#Same as
			#self.assertEqual((self.A+self.D).eval(2), (self.A.eval(2)+self.D.eval(2)))
			#self.assertEqual((self.B+self.D).eval(2), (self.B.eval(2)+self.D.eval(2)))

	def test_sub(self):
		for x in range(0,50):
			self.assertEqual((self.B-self.D).eval(x), (self.B.eval(x)-self.D.eval(x)))
			#self.assertEqual((self.C-self.D).eval(x), (self.C.eval(x)-self.D.eval(x)))
		#Figure out this subtraction!
		#self.assertEqual((self.D-self.C).eval(2), (self.D.eval(2)-self.C.eval(2)))
		#self.assertEqual((self.B-self.D).eval(2), (self.B.eval(2)-self.D.eval(2)))
		
		# Test to make sure it is handling 0 correctly by removing exponents with coeff of zero
		poly = Polynomial([1, 2, 3, 4])
		d = self.D - poly
		self.assertEqual(d, Polynomial([]))

	def test_mul(self):
		for x in range(0,50):
			self.assertEqual((self.A*self.D).eval(x), (self.A.eval(x)*self.D.eval(x)))
			self.assertEqual((self.D*self.A).eval(x), (self.D.eval(x)*self.A.eval(x)))
	
	def test_eq(self):
		# Test to see if equality is handled
		poly = Polynomial([1, 2, 3, 4])
		poly1 = Polynomial([10])
		poly1[5] = 2
		poly1[4] = 4
		poly1[3] = 6
		poly1[2] = 8

		if self.A == poly and poly1 == self.D:	
			self.assertEqual(1,1)
		elif self.A == poly and poly1 != self.D:
			self.assertEqual(1,0)
		elif self.A != poly and poly1 == self.D:
			self.assertEqual(0,1)
		else:
			self.assertEqual(0,0)

		# Test to see if NotEqual is handled properly
		poly1 = Polynomial([5, 6, 7, 8, 9, 10])
		poly2 = Polynomial([4, 5, 6, 7, 8, 9, 10, 11])
		self.assertNotEqual(poly1, poly2)  
		self.assertNotEqual(poly2, poly1)

		#self.A = Polynomial([2, 4, 6, 8, 0, 10])
		#self.D = Polynomial([1,2,3,4])
		#self.assertEqual(self.A, Polynomial([0, 0, 0, 0, 2, 4, 6, 8, 0, 10]))
		#self.assertEqual(self.B, Polynomial([0, 0, 0, 3, 2+5j, -1, -4-7j]))
		#self.assertEqual(self.C, Polynomial([0, 0, 0, 2.004, -3.345, 4.125, 6.000002, 0, 3.000256]))
		#self.assertEqual(self.D, Polynomial([0, 0, 1,2,3,4]))

	def test_deriv(self):
		# for positive exponents
		x = self.D.deriv()
		y = Polynomial([3, 4, 3])
		self.assertEqual(x, y)

		# for negative exponents
		# ie. 3/x => -3/x^2
		self.D[-1] = 3
		self.assertEqual(self.D.deriv()[-1],0)
		self.assertEqual(self.D.deriv()[-2], -3)

	def test_neg_powers(self):
		self.D[-1] = 2
		self.assertEqual(self.D.eval(10), 1234.2)

		self.D[-2] = 4
		self.A[-1] = 4
		self.assertEqual((self.D+self.A).eval(10), 248044.64)
	
	def test_boolean(self):
		poly = Polynomial([])
		self.assertNotIsInstnace(poly[1], bool)

	def test_sparse_zeros(self):
		n = 10000
		p = Polynomial([0]*n)
		q = Polynomial()
		
		p_size =sum(sys.getsizeof(getattr(p,x)) for x in vars(p))
		q_size =sum(sys.getsizeof(getattr(q,x)) for x in vars(q))        
		factor_increase = p_size/q_size
		self.assertEqual(p,q)
		self.assertLess(factor_increase,10,msg='Implementation not sparse, init with {} zeros'.format(n))



	# Done after every test, if setUp succeeds
	def tearDown(self):
		"tear down"
		pass

if __name__ == '__main__':
	unittest.main()
