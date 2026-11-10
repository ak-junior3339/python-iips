class employee : 
	def __init__(self) : 
		self.eid = int(input("Enter EMP ID - "))
		self.name = str(input("Enter Name :"))
		self.contact = str(input("Enter contact : "))
	def show(self):
		print("id :{self.eid} name : {self.name} Contact : {self.contact}")

class manager(employee) : 
	def __init__(self) : 
		super.__init__()
		self.department = str(input("Enter Department : "))
	def show(self):
		super.show()
		print("Departmnent : {self.department}")

.