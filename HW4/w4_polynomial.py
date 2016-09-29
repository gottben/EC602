# AUTHOR BrianAppleton appleton@bu.edu
# AUTHOR AlexBennett gottbenn@bu.edu
# AUTHOR CathrynCallahan cathcal@bu.edu
# AUTHOR PreranaHaridoss preranah@bu.edu

'''
PYTHON POLYNOMIAL CLASS

---- Functionality checklist ----
[x] initialize with constructor, efficient storage
[x] evaluate polynomials using syntax like p.eval(10) where 10=x
[x] implement str() and repr() **Not required but will be used by checker**
[x] access and modify the coefficients using []. p[8] should set coeff of x^8 to 12. Make sure coefficients of 0 aren't stored.
[x] add polynomials using +, forward implementation only. Make sure that the expression x+y doesn't change the values of x or y.
[x] subtract polynomials using -, forward implementation only. Make sure that the expression x-y doesn't change the values of x or y.
[x] multiply polynomials using *. Make sure that the expression x*y doesn't change the values of x or y.
[x] test for equality using ==
[x] implement p.deriv() method
[x] ensure negative powers work
[x] ensure int, float, and complex coefficients work
[x] ensure int, float, and complex x works
[x] make sure that polynomials are stored efficiently


---- Helpful references ----
Python dictionaries:  https://docs.python.org/3/tutorial/datastructures.html#dictionaries
Python magic methods: http://www.rafekettler.com/magicmethods.html

'''

class Polynomial():
	def __init__(self, p_input=[]):
		"""		
		The last element in p_input list is the coefficient of x^0
		Create a dictionary p_dict to represent the input polynomial. It will use the exponents as the keys.
		Efficient storage is partially implemented here. Coefficients of 0 will not be stored.	
		"""		
		self.p_dict = {}
		exp = len(p_input)-1
		for coeff in p_input:
			if coeff!=0:			
				self.p_dict[exp] = coeff
			exp=exp-1
	def eval(self,x):
		result = 0 #defaults to an int container	
		for exp, coeff in self.p_dict.items():
			result += coeff*x**exp
		return result
	def __str__(self):
		"""
		Return nicely-formatted string showing polynomial
		This seems to matter less
		"""		
		result = ""		
		for exp, coeff in self.p_dict.items():
			result += "(" + str(coeff) + ")" + "x^" + str(exp) + " + "
		return result[0:len(result)-2]	
	def __repr__(self):
		"""
		Return dictionary representation of polynomial
		"""
		return(str(self.p_dict))
	def __setitem__(self, exp, coeff):
		"""
		Required by mutable container protocol
		Usage: p[x] = y
		This is functional for pre-existing or non-existent exp		
		"""		
		if coeff != 0:		
			self.p_dict[exp] = coeff
	def __len__(self):
		"""
		Required by mutable container protocol
		Usage: len(p)
		"""
		return len(self.p_dict)
	def __getitem__(self, exp):
		"""
		Required by mutable container protocol
		Usage: p[x]
		Return 0 for missing exponents
		"""		
		if exp in self.p_dict:
			return self.p_dict[exp]
		else:
			return 0
	def __delitem__(self, exp):
		"""
		Required by mutable container protocol
		"""
		self.p_dict.pop(exp)
	def __add__(self,p_add):
		"""
		Arguments are polynomials
		Argument.p_dict gets the dictionary
		"""		
		#Create a copy of self
		p_result = Polynomial()
		p_result.p_dict = self.p_dict.copy()
				
		#Loop through p_add and modify terms of p_result
		for exp, coeff in p_add.p_dict.items():		
			if exp in p_result.p_dict:
				p_result.p_dict[exp] += coeff
				#Delete the term if its coefficient is now zero. Uses __delitem__.
				if p_result.p_dict[exp] == 0:
					del p_result[exp]
			else:
				p_result.p_dict[exp] = coeff	
		return p_result
	def __sub__(self,p_sub):
		"""
		Subtract p_sub from self and return result
		Usage: -
		"""
		#Create a copy of self
		p_result = Polynomial()
		p_result.p_dict = self.p_dict.copy()
		
		#Loop through p_sub and modify terms of p_result
		for exp, coeff in p_sub.p_dict.items():		
			if exp in p_result.p_dict:
				p_result.p_dict[exp] -= coeff
				#Delete the term if its coefficient is now zero. Uses __delitem__.
				if p_result.p_dict[exp] == 0:
					del p_result[exp]
			else:
				p_result.p_dict[exp] = -1*coeff	
		return p_result
	def __mul__(self, p_mul):
		"""
		Multiply two polynomials and return a Polynomial
		Usage: *
		"""		
		
		p_result = Polynomial()
		
		for exp_a, coeff_a in self.p_dict.items():
			for exp_b, coeff_b in p_mul.p_dict.items():
				if (exp_a+exp_b) in p_result.p_dict:					
					p_result.p_dict[exp_a+exp_b] += coeff_a*coeff_b	
					#print("Case 1: ", exp_a+exp_b, p_result.p_dict[exp_a+exp_b])		
				else:
					p_result.p_dict[exp_a+exp_b] =  coeff_a*coeff_b
					#print("Case 2: ", exp_a+exp_b, p_result.p_dict[exp_a+exp_b])
		
		return p_result
	def __eq__(self, p_eq):
		"""
		Test for equality
		The only way that two polynomials are surely equal is if all of their coefficients and exponents match
		Given a base, there could be instances where the coefficients/exponents are not equal, but the polynomials evaluate to the same value
		Usage: ==
		"""
		return self.p_dict==p_eq.p_dict
	def deriv(self):
		"""
		Take derivative of the polynomial with respect to its base x
		"""
		result = Polynomial()
		for exp, coeff in self.p_dict.items():
			result[exp-1]=coeff*exp
		return result

def main():
	"""	
	x = Polynomial([0,0,5j,2,1])
	y = Polynomial([0,0,0,4,3])
	z = Polynomial()
	z[1] = 4
	z[10] = 8 

	print(str(y))
	print(str(y.deriv()))
	print(str(z))
	print(str(z.deriv()))

	print(repr(z))

	"""
    
if __name__=="__main__":
    main()
