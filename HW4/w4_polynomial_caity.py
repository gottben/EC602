# AUTHOR Cathryn Callahan cathcal@bu.edu
#
# w4_polynomial.py
#
#
# [X] Implement a constructor which takes a sequence and assigns the coefficients 
# 		in the natural (descending) order. So Polynomial([4,-9,5.6]) should make
#		4x^2 - 9x + 5.6
# [X] Implement addition and subtraction of polynomials using + and -
# [X] Implement multiplication of polynomials using *
# [X] Implement testing for equaluty of polynomials using ==
# [X] Implement an effective mechanism for handling sparse polynomials 
# [ ] Implement negative powers in the polynomials, ie you should be able to handle p(x)=x^-1
# [X] Implement evaluation of the polynomial using a eval method, like this" p.eval(2.1)
# [X] Implement accessing and modifying the coefficients usint []. So p[2] should be the coeff
#		of x^2 and p[8] = 12 should set the coefficient of x^8 to 12. 
# [X] Implement a derivative method p.deriv() which returns the derivative of the polynomial



class Polynomial():

	# Constructor used to initalize an instance at creation time
	def __init__ (self,coef=[]):
		self.poly = {}		# Creating an empty dictionary for the polynomial
		expon = len(coef)-1 	# Set length of exponent key to length of coef 
		for i in coef:
			if i != 0:			# Will get rid of exponents with coef of zero
				self.poly[expon] = i
			expon -= 1
			
	def __str__(self):
		# Method for Printing Polynomial
		"Prints nice version of Polynomial"
		ans = ""
		for expon, coef in self.poly.items():
			#if coef != 0: # Another way to get rid of exponents with coef of zero
				ans += str(coef) + "x^" + str(expon) + " + "
			#else:	
			#	del expon
		return ans[0:len(ans)-3] 	# Will print string characters from 0 to the length of
									# the poly minus the last + sign and spaces

	def __repr__(self):
		"Prints dictionary of poly"
		return str(self.poly)


	def __setitem__(self, expon, coef):
		# Method for setting coeff ie. p[2] = 12 will give 12x^2
		"Used to set a[i] = v, Assign new coef, v, to exponent, i"
		# Will not return anything
		if coef != 0:
			self.poly[expon] = coef

		else:
		# get rid of term, since the coef is now zero
			del self[expon] 

	def __getitem__(self, expon):
		# Method for getting coef for given expon ie p[2] = coef of x^2
		"Used to get a[i] and return 0 if expon is not present"
		if expon in self.poly:
			return self.poly[expon]
		else:
			return 0

	def __delitem__(self, expon):
		# Method for deleting an item in self.poly
		"Delete exponent"
		if expon in self.poly:
			self.poly.pop(expon) 

	def __len__(self):
		# Methof for gettin the length of the polynomial
		"Give length of polynomial"
		return len(self.poly)


	def __add__ (self, add):
		# Method for adding polynomials
		"Return self+add"
		ans = Polynomial([])
		ans.poly = self.poly.copy()

		for expon, coef in add.poly.items():
			if expon in ans.poly:	
				ans[expon] += coef  # Changed from ans.poly[expon]
				if ans.poly[expon] == 0:
					del expon 	# Changed from ans[expon]
				else:
					pass
			else:
				ans[expon] = coef # Changed from ans.poly[expon]
		return ans

	def __sub__(self, sub):
		# Method for subtracting polynomials
		"Return self-sub"
		ans = Polynomial([])
		ans.poly = self.poly.copy()

		for expon, coef in sub.poly.items():
			if expon in ans.poly:
				ans[expon] -= coef 	# Changed from ans.poly[expon]
				if ans.poly[expon] == 0:
					del ans[expon]
				else:
					pass
			else:
				ans[expon] = coef # Changed from ans.poly[expon]
		return ans

	def __mul__(self,mult):
		# Method for multiplying polynomials
		"Retun self*mult"
		ans = Polynomial([])
		#ans.poly = self.poly.copy()

		for exponA, coefA in self.poly.items():
			for exponB, coefB in mult.poly.items(): 	
				if (exponA+exponB) in ans.poly:
					ans.poly[exponA+exponB] += coefA*coefB
				else:
					ans.poly[exponA+exponB] = coefA*coefB
		return ans
					

	def __eq__(self,eq):
		# Method to test equality of polynomials
		"Return value is 'True' or 'False'"
		#ans = Polynomial([])
		#ans.poly = self.poly.copy()
		#ans = self.poly.copy()
		#return self.poly.items() == eq.poly.items()

		if len(self.poly) > len(eq.poly):
			return False
		elif len(eq.poly) > len(self.poly):
			return False
		else:
			for exponA, coefA in self.poly.items():
				for exponB, coefB in eq.poly.items(): 
					if (exponA == exponB and coefA == coefB):
						return True
					else:
						return False
		

	def eval(self, value):
		# Method for evaluating polynomial at given x value ie. p.eval(5)
		number = 0
		for expon, coef in self.poly.items():
			number += coef * value**expon
		return number


	def deriv(self):
		ans = Polynomial([])
		for expon, coef in self.poly.items():
			ans[expon-1] += coef*expon 

		return ans

