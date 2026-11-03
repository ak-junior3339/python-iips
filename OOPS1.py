
class Student : 
	def __init__(self) : 
		self.name = str(input("Enter Name : "))
		self.city = str(input("Enter City : "))
		self.roll = str(input("Enter Roll Number : "))
	def show(self) : 
		print(f"Name: {self.name}")
		print(f"City: {self.city}")
		print(f"Roll Number: {self.roll}")

s1 = Student()
s1.show()