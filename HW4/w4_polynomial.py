# AUTHOR AlexBennett gottbenn@bu.edu




class Polynomial():
	"Polynomial(coeff, key(exp)) -> a polynomial array"

	def __init__(self, coeff=[]):
		exp = len(coeff) - 1 
		poly = []
		expon = []
		self.poly = poly
		self.expon = expon
		i = exp
		while i > -1:
			self.poly += [coeff[exp - i]]
			self.expon += [i]
			i -= 1 
		self.sparse()

	def list_duplicates(self, array,value):
		start_at = -1
		locs = []
		while True:
			try:
				loc = array.index(value,start_at+1)	
			except:
				break
			locs += [loc]
			start_at = loc
		return locs

	def __getitem__(self,key):
		"Get the value from the key"
		try:
			ind_self = self.expon.index(key)
			return self.poly[ind_self]
		except:
			return 0


	def __setitem__(self,key,value):
		"Set the coefficient to a specific key"
		if key in self.expon:
			ind_self = self.expon.index(key)
			self.poly[ind_self] = value
			self.sparse()
		else:
			self.expon += [key]
			self.poly += [value]
			self.sparse()

	def __len__(self):
		try:
			return len(self.poly)
		except:
			return 0


	def __add__(self,value):
		"Return self+coeff"
		#print(value[1],value[-3],value[5])
		F = Polynomial()
		F.poly += self.poly
		F.expon += self.expon
		for expo in value.expon:
			ind_value = value.expon.index(expo)
			#print(expo,F.expon)
			if expo in F.expon:
				ind_self = F.expon.index(expo)
				F.poly[ind_self] +=  value.poly[ind_value]
				#print(expo,F.poly[ind_self],F.expon[ind_self])
			else: 
				F.expon +=  [expo]
				F.poly +=  [value.poly[ind_value]]
		return F.sparse()

	def __sub__(self,value):
		"Return self-coeff"
		F = Polynomial()
		F.poly += self.poly
		F.expon += self.expon
		for expo in value.expon:
			ind_value = value.expon.index(expo)
			if expo in F.expon:
				ind_self = F.expon.index(expo)
				F.poly[ind_self] -= value.poly[ind_value]
			else: 
				F.expon += [expo]
				F.poly += [-(value.poly[ind_value])]
		return F.sparse()


	def __mul__(self,value):
		"return s*v"
		F = Polynomial()
		F.poly += self.poly
		F.expon += self.expon
		exponents = []
		coefficients = []
		expon = []
		if len(value.poly) == 0:
			return F
		for expon in value.expon:
			exponents += [x+expon for x in F.expon]
		set_exp = set(exponents)
		for coeff in value.poly:
			coefficients += [y*coeff for y in F.poly]
		poly_coeff = []
		for exp in set_exp:
			l_of_duplicates = F.list_duplicates(exponents,exp)
			poly = []
			for index in l_of_duplicates:
				poly += [coefficients[index]]
			poly_coeff += [sum(poly)]
		F.expon = list(set_exp)
		F.poly = poly_coeff
		return F
							

	def __eq__(self,value):
		"return if values are equal"
		# print(set(self.expon),set(value.expon))
		# print(set(self.poly),set(value.poly))
		if set(self.expon)== set(value.expon):
			for expon in self.expon:
				self_index = self.expon.index(expon)
				value_index = value.expon.index(expon)
				if self.poly[self_index] != value.poly[value_index]:
					return False	
			return True
		else:
			return False
	

	def eval(self, value):
		"return evalutated polynomial"
		total = 0
		for expon in self.expon:
			ind_self = self.expon.index(expon)
			total += (value**expon)*self.poly[ind_self]
		return total

	def deriv(self):
		"return the derivative of self"
		F = Polynomial()
		F.poly += self.poly
		F.expon += self.expon
		for expon in F.expon: 
			ind_self = F.expon.index(expon)
			F.poly[ind_self] = F.poly[ind_self]*expon
		F.expon[:] = [expon - 1 for expon in F.expon]
		F.sparse()
		return F


	def sparse(self):
		"return a sparse version of the polynomial"
		for coeff in self.poly:
			if coeff == 0:
				ind_self_c = self.poly.index(coeff)
				len_self = len(self.poly)
				self.poly = self.poly[0:ind_self_c] + self.poly[ind_self_c+1:len_self]
				self.expon = self.expon[0:ind_self_c] + self.expon[ind_self_c+1:len_self]
		return self

def main():
	pass

if __name__=="__main__":
	main()

