from w4_polynomial_2 import Polynomial

A = Polynomial([1,2,0,3,4,0])
# B = Polynomial([5,4,3,0,0])

F = Polynomial([4,3,2])
G = Polynomial([8,3])

F.deriv()

print("F.poly=",F.poly)
print("F.expon=",F.expon)
print("G.poly=",G.poly)
print("G.expon=",G.expon)

if F == G:
	print("Yes they are the same!")


print(A.poly)


C = -54084618265980114655315496906950370566146574296955485864
D = -54084618265980114655315496906950370566146574296955485864

if C == D:
	print("True")
# if A == B:
# 	print("True")