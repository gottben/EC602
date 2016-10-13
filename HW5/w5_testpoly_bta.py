# AUTHOR BrianAppleton appleton@bu.edu
import unittest
import sys
#import signal


authors=['appleton@bu.edu']

class PolynomialTestCase(unittest.TestCase):
	def setUp(self):
		#Do these things before every test
		#make some mixed polynomials of unequal lengths
		self.a_list=[4,5.98,-3,0,0,1+2j,7]
		self.b_list=[-1, 2.7, -3j+10]
		self.a = Polynomial([4,5.98,-3,0,0,1+2j,7])
		self.b = Polynomial([-1, 2.7, -3j+10])
		#make some integer polynomials of unequal lengths
		self.c_list=[5,0,4,5,645,6,0,63,7]
		self.d_list=[34,2,6,0,35,4,54]
		self.c = Polynomial([5,0,4,5,645,6,0,63,7])
		self.d = Polynomial([34,2,6,0,35,4,54])
		#we do not pass *_list to the constructor to avoid any chance of the constructor modifying the *_list variables
		#Most tests are flexible; the polynomials can be changed here and the tests will still function. Except where noted.
	
	def test_get_set_item(self):	
		#Test __getitem__ for pre-existing elements, positive and negative exponents
		
		#make sure each poly contains the coefficients that we stored in setUp
		for poly_list,poly in [[self.a_list,self.a],[self.b_list, self.b],[self.c_list, self.c],[self.d_list,self.d]]: 		
			for index,coeff in enumerate(poly_list):
				exp = len(poly_list) - index - 1	
				self.assertEqual(poly[exp],coeff)		

		#make sure we get a coefficient of zero for elements that do not exist, positive exponents
		for exp in range(len(self.a_list),100):
			self.assertEqual(self.a[exp],0)
		
		#make sure we get a coefficient of zero for elements that do not exist, negative exponents
		for exp in range(-100,0):
			self.assertEqual(self.a[exp],0)
	
		#test getitem for newly-created coefficients of negative exponents	
		poly_1 = Polynomial([])
				
		poly_1[-3]=1
		poly_1[-4]=1j
		poly_1[-5]=6.7
		self.assertEqual(poly_1[-3],1)
		self.assertEqual(poly_1[-4],1j)
		self.assertEqual(poly_1[-5],6.7)

		#test getitem for modified coefficients of negative exponents
		poly_1[-3]=2
		poly_1[-4]=2j
		poly_1[-5]=7.0
		self.assertEqual(poly_1[-3],2)
		self.assertEqual(poly_1[-4],2j)
		self.assertEqual(poly_1[-5],7.0)
		
		#test getitem for modified coefficients of positive exponents
		poly_1[0]=2
		poly_1[1600]=3.5
		poly_1[70]=7
		poly_1[0]=1+2j
		poly_1[1600]=7.9
		poly_1[70]=0 ####This nabs Poly_83
		self.assertEqual(poly_1[0],1+2j)
		self.assertEqual(poly_1[1600],7.9)
		self.assertEqual(poly_1[70],0) #### This nabs Poly_83

		#construct a polynomial entirely using setitem and compare to a poly created with the constructor
		poly_2 = Polynomial([])
		poly_2[10]=7
		poly_2[5] =1+4j
		poly_2[0] =2.0-6.5j
		self.assertEqual(poly_2,Polynomial([7,0,0,0,0,1+4j,0,0,0,0,2.0-6.5j]))
		self.assertEqual(Polynomial([7,0,0,0,0,1+4j,0,0,0,0,2.0-6.5j]),poly_2)
	
		#Poly19: Really interesting. Because (false==0), where false is a bool object, we also need to make sure that __getitem__ is not returning
			#an object of type bool
		poly_19 = Polynomial([])
		self.assertNotIsInstance(poly_19[1], bool)
			
		
	def test_input_arg_mod(self):
		#run a bunch of operations that should not modify their input arguments	
	
		for z,y in [[self.a,self.b],[self.a,self.c],[self.a,self.d],[self.b,self.c],[self.b,self.d],[self.c,self.d]]:		
			z*y
			y*z
			z==y
			y==z
			z-y
			y-z
			z+y
			y+z
			z[0]
			y[0]
			z[160]
			y[160]
			z.deriv()
			y.deriv()
		
		for x in range(-100,100):
			self.a[x]		

		self.assertEqual(self.a,Polynomial([4,5.98,-3,0,0,1+2j,7]))
		self.assertEqual(self.b,Polynomial([-1, 2.7, -3j+10]))
		self.assertEqual(self.c,Polynomial([5,0,4,5,645,6,0,63,7]))
		self.assertEqual(self.d,Polynomial([34,2,6,0,35,4,54]))
		self.assertEqual(Polynomial([4,5.98,-3,0,0,1+2j,7]), self.a)
		self.assertEqual(Polynomial([-1, 2.7, -3j+10]), self.b)
		self.assertEqual(Polynomial([5,0,4,5,645,6,0,63,7]), self.c)
		self.assertEqual(Polynomial([34,2,6,0,35,4,54]), self.d)
		
	def test_init(self):
		#make sure that we actually created an instance		
		self.assertIsInstance(self.a,Polynomial)
		self.assertIsInstance(self.b,Polynomial)
		self.assertIsInstance(self.c,Polynomial)
		self.assertIsInstance(self.d,Polynomial)

		#make sure that the constructor does not modify its argument
		construct_list = [0,2,3,0,4.7,5,6,-1j]
		construct_list_copy = construct_list.copy();
		Polynomial(construct_list)
		self.assertEqual(construct_list, construct_list_copy)
		
		#Poly35 and #Poly10: make sure that the constructor only takes one argument
		try:
			Polynomial([],{})
			raise Exception('Error01')

		except Exception as e:
			if str(e) == 'Error01':
				raise Exception('I shouldn\'t be allowed to give the constructor two arguments')
	
	def test_eq(self):
		
		#test whether == correctly returns true
			#this is already hit in test_input_arg_mod

		#test whether == correctly returns true for two equivalent polynomials, where one has a bunch of extra coefficients equal to zero
		self.assertEqual(self.a,Polynomial([0,0,0,0,0,0,0,0,0,0,4,5.98,-3,0,0,1+2j,7]))
		self.assertEqual(self.b,Polynomial([0,0,0,-1, 2.7, -3j+10]))
		self.assertEqual(self.c,Polynomial([0,0,5,0,4,5,645,6,0,63,7]))
		self.assertEqual(self.d,Polynomial([0,34,2,6,0,35,4,54]))

		#test whether == correctly returns false
		for z,y in [[self.a,self.b],[self.a,self.c],[self.a,self.d],[self.b,self.c],[self.b,self.d],[self.c,self.d]]:	
			self.assertNotEqual(z,y)

		#try to pick up whether eval() is being used to test equality. Two polys are equal iff their coefficients are equal
		#for example, with base 10, Polynomial([1,0])==Polynomial([0,10])
		for i in range(1,100):
			for j in range(1,10):
				self.assertNotEqual(Polynomial([j,0]),Polynomial([0,i]))
				self.assertNotEqual(Polynomial([0,i]),Polynomial([j,0]))
		
		#POLY36 - Need to catch error where higher order terms in the addend (the polynomial after the ==) are ignored
		Poly36_is_wrong    = Polynomial([10,9,8,7])
		Poly36_is_SO_WRONG = Polynomial([11,10,9,8,7])
		self.assertNotEqual(Poly36_is_wrong, Poly36_is_SO_WRONG)
		self.assertNotEqual(Poly36_is_SO_WRONG,Poly36_is_wrong)

		#POLY36 - For completeness, catch error where lower order terms are ignored
		Poly36_extra_neg_terms = Polynomial([10,9,8,7])
		Poly36_extra_neg_terms[-1] = 1
		self.assertNotEqual(Poly36_is_wrong, Poly36_extra_neg_terms)
		self.assertNotEqual(Poly36_extra_neg_terms, Poly36_is_wrong)
		
	def test_eval(self):				
		#for each of the 4 test polyomials		
		for poly_list,poly in [[self.a_list,self.a],[self.b_list, self.b],[self.c_list, self.c],[self.d_list,self.d]]:
			#pick a argument x for the eval() function			
			for x in [0,1,6.0,1+2j,1-2j,6]:
				#manually calculate the correct eval(x)				
				eval_sum = 0								
				for index, coeff in enumerate(poly_list):
					exp = len(poly_list) - index - 1
					eval_sum += coeff*x**exp
				#check it				
				self.assertEqual(poly.eval(x),eval_sum)

		#do some limited testing with negative exponents
		poly_1=Polynomial([4,1])
		poly_1[-1]=5
		self.assertEqual(poly_1.eval(10), 41.5)

	def test_add(self):
		#ran into some rounding/storage error issues when polynomials a and b are used. Sticking to integers.
		for poly_1,poly_2 in [[self.c,self.d]]:		
			for x in range(1,100):		
				self.assertEqual(poly_1.eval(x)+poly_2.eval(x),(poly_1+poly_2).eval(x))
				self.assertEqual(poly_1.eval(x)+poly_2.eval(x),(poly_2+poly_1).eval(x))

		#test some negative exponents
		poly_1=Polynomial([4,1])
		poly_2=Polynomial([])
		poly_2[-1]=5
		self.assertEqual((poly_1+poly_2).eval(10),41.5)
		self.assertEqual((poly_2+poly_1).eval(10),41.5)
	
	def test_sub(self):
		for poly_1,poly_2 in [[self.c,self.d]]:		
			for x in range(1,100):		
				self.assertEqual(poly_1.eval(x)-poly_2.eval(x),(poly_1-poly_2).eval(x))
				self.assertEqual(poly_2.eval(x)-poly_1.eval(x),(poly_2-poly_1).eval(x))

	def test_mul(self):
		for poly_1,poly_2 in [[self.c,self.d]]:		
			for x in range(1,100):		
				self.assertEqual(poly_1.eval(x)*poly_2.eval(x),(poly_1*poly_2).eval(x))
				self.assertEqual(poly_2.eval(x)*poly_1.eval(x),(poly_1*poly_2).eval(x))
	
	def test_deriv(self):
		#ran into some rounding/storage error issues when polynomials a and b are used. Sticking to integer polynomials c and d.		
		#NOTE: answers are hard-coded here. Need to update if polynomals in SetUp are changed
		self.assertEqual(self.c.deriv(),Polynomial([40,0,24,25,2580,18,0,63]))
		self.assertEqual(self.d.deriv(),Polynomial([204,10,24,0,70,4]))

		#test deriv when there are negative exponents
		self.c[-1]=5
		self.assertEqual(self.c.deriv()[-1],0)
		self.assertEqual(self.c.deriv()[-2],-5)
		
	def test_efficiency(self):
		#Poly92: exeuction time is great, but they are not storing their polynomial efficiently
		#sys.getsizeof() calls the object's __sizeof__ method, and in my experimentation on Polynomial objects, coudln't distinguish efficient storage from 
			#inefficient storage
		#instead, we're going to use getsize of on the Polynomial object's public contents, for which getsizeof is likely well defined
		
		#create a reference polynomial poly_small, and sparse polynomial poly_big that should be about the same size
		poly_small = Polynomial([1,1])
		poly_big   = Polynomial([1]+[0]*1000+[1])

		total_small_size = 0
		total_big_size = 0	

		#sum the sizes in bytes of all of the public variables in each Polynomial object
		for object in vars(poly_small):
			total_small_size += sys.getsizeof(getattr(poly_small,object))

		for object in vars(poly_big):
			total_big_size += sys.getsizeof(getattr(poly_big,object))

		#if your big poly is more than twice the size of the small poly, you're probably not storing efficiently.
		if total_big_size > 2*total_small_size:
			raise Exception("You're not storing sparse polynomials efficiently")

	def tearDown(self):
		#Do these things after every test
		pass

