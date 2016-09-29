from w4_polynomial import Polynomial

'''
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
'''

'''
NOTE: This testing code requires that __repr__ is defined as follows in the Polynomial class:
	def __repr__(self):
		"""
		Return dictionary representation of polynomial
		"""
		return(str(self.p_dict))
'''


'''
Set up test Polynomials
Dictionary contents retreived with repr():
x={0: 4, -4: (1+1j), -5: 2, 4: 3}
y={0: (10-3j), 1: 2.7, 2: -1, 5: 17.9}
'''
x = Polynomial([3,0,0,0,4])
y = Polynomial([-1, 2.7, -3j+10])
z = Polynomial([1,2,5,6,7,0,1])
w = Polynomial([0,0,3,2,0])

x[-5] = 2
x[-4] = 1j+1
y[5]  = 17.9

'''
Test str() and repr()
'''
if 'object' in repr(x):
	print("WARNING: repr() function is not defined for Polynomial")
if 'object' in str(x):
	print("WARNING: str() function is not defined for Polynomial")

'''
Test initialization,  ==, and assignment
'''
if y == Polynomial([17.9, 0, 0, -1, 2.7, 10-3j]):
	print("PASS: __init__, __eq__, and __setitem__ are functional")
else:
	print("FAIL: ", repr(Polynomial([17.9, 0, 0, -1, 2.7, 10-3j])), " does not match y = ", repr(y))

'''
Test not equal to
'''
if (y == Polynomial([17.9, 0, 0, -1, 2.8, 10-3j])) == False:
	print("PASS: __eq__ not equals is functional")
else:
	print("FAIL: __eq__ not equals is not functional")


'''
Make sure all Polynomial methods except __setitem__ do not modify input args. Use z as test case
'''

junk = z+w
junk = w+z
junk = z*w
junk = w*z
junk = z.eval(3)
junk = z-w
junk = w-z
junk = z.deriv()
junk = z[1500]
junk = z[2] + z[1]
junk = z[1]==0

if z == Polynomial([1,2,5,6,7,0,1]):
	print("PASS: no methods modify their arguments")
else:
	print("FAIL: one or more methods modify their input arguments")

'''
Test eval
'''
if y.eval(3j) == (19+4354.8j) and x.eval(-3) == (247.00411522633746+0.012345679012345678j) and z.eval(0) == 1:
	print("PASS: eval() is functional")
else:
	print("PASS: eval() not functional")

'''
Test __getitem__
'''
if (x[-5] == 2 and y[0] == (10-3j) and x[50000] == 0):
	print("PASS: __getitem__ is functional")
else:
	print("FAIL: __getitem__ is not functional")

'''
Test __add__
'''

if ((z+w).eval(10)) == (z.eval(10) + w.eval(10)):
	print("PASS: __add__ is functional")
else:
	print("FAIL: __add__ is not functional, expected ", z.eval(10) + w.eval(10), " to equal " , (z+w).eval(10))

'''
Test __sub__
'''
if ((z-w).eval(10)) == (z.eval(10) - w.eval(10)):
	print("PASS: __sub__ is functional")
else:
	print("FAIL: __sub__ is not functional, expected ", z.eval(10) - w.eval(10), " to equal " , (z-w).eval(10))

'''
Test __mul__
'''
if ((z*w).eval(10)) == (z.eval(10) * w.eval(10)):
	print("PASS: __mul__ is functional")
else:
	print("FAIL: __mul__ is not functional, expected ", z.eval(10) * w.eval(10), " to equal " , (z*w).eval(10))

'''
Test deriv()
'''
if repr(x.deriv()) == '{3: 12, -6: -10, -5: (-4-4j)}':
	print("PASS: deriv() is functional")
else:
	print("FAIL: deriv() is not functional or repr() is not defined as needed for this script.")

'''
Test whether subtraction returns a polynomial with a coefficient of zero
'''
if (Polynomial([6,0,0])==w-Polynomial([0,0,-3,2,0]))==True:
	print("PASS: __sub__ clears terms with coefficients of zero")
else:
	print("FAIL: __sub__ retains terms with a coefficient of zero. Result of subtraction: ", repr(w-Polynomial([0,0,-3,2,0])))

'''
Test whether addition returns a polynomial with a coefficient of zero
'''
if (Polynomial([0,4,0])==w+Polynomial([0,0,-3,2,0]))==True:
	print("PASS: __add__ clears terms with coefficients of zero")
else:
	print("FAIL: __add__ retains terms with a coefficient of zero. Result of addition: ", repr(w+Polynomial([0,0,-3,2,0])))


'''
Test whether deriv() returns a polynomial with a coefficient of zero
'''
if Polynomial([4,3,2]).deriv()==Polynomial([8,3]):
	print("PASS: deriv() clears terms with coefficients of zero")
else:
	print("FAIL: deriv() retains terms with a coefficient of zero. Result of deriv(): ", repr(Polynomial([4,3,2]).deriv()))




