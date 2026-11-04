class complex():
	def __init__(self,*args):
		if len(args) == 0 : 
			self.real = int(input("Enter the real part : "))
			self.imagnary = int(input("Enter the imaginary part"))
		elif len(args)==2: 
			self.real = args[0]
			self.imagnary = args[1]

	def show(self):
		print(f"{self.real} + {self.imagnary}i")

	def __add__(self,other):
		x = self.real + other.real
		y = self.imagnary + other.imagnary
		return complex(*(x,y))

c1 = complex()
c2 = complex()
c3 = c1.__add__(c2)
c3.show()