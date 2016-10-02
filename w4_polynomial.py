class Polynomial():
	"Polynomial([parray1]) -> a polynomial array"

	def __init__(self, parray1=[]):
		self.parray1 = []
		exp = len(self.parray1) - 1
		for i in self.parray1:
			if(exp > 0):
				print(i,'x^',exp,'+',end=' ')
				exp -= 1
			else:
				print(i,'x^',exp)

	def __add__(self,parray2):
		k = 0
		if(len(parray2) <= len(self.parray1)):
			for i in parray2:
				self.parray1[k] += i 
				k += 1
			return(Polynomial(self.parray1))
		else:
			for i in self.parray1:
				parray2[k+len(parray2)-len(self.parray1)] += i
				k += 1
			return(Polynomial(parray2))

	def __mul__(self,p):
		"return s*v"
		x = [0 for i in range(len(self.parray1)+len(p) - 1)]
		#print(x)
		for i in range(0,len(self.parray1)):
			for j in range(0,len(p)):
				#print(i,j)
				#print(self.parray1[i],p[j])
				x[j+i] += self.parray1[i]*p[j]
		return(Polynomial(x))

	def __eq__(self,p):
		"return if values are equal"
		if(len(self.parray1) == len(p)):
			for i in range(0,len(self.parray1)):
				if (self.parray1[i] == p[i]):
					i = i
				else: 
					print("FALSE")
					return 0
			print("TRUE")
			return 1
		else: 
			print("FALSE")
			return 0

	def __setitem__(self,key,value):
		"allows values to be assigned (Question)"
		p = [None for k in range(abs(key) +1)]
		print(p)
		self.parray1 = self.parray1 + p

		print(self.parray1)
		self.parray1[key] = value

	def __getitem__(self,key):
		"Get the value from the key"
		return self.parray1[key]










def main():
	pass

if __name__=="__main__":
	main()

