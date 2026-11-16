workshops = {
	"Python Basics": 500,
	"Data Analytics": 800,
	"Generative AI": 1000,
	"Web Development": 750
}

class Person : 
	def __init__(self,name,email,phone):
		self.name = name,
		self.email = email,
		self.phone = phone 
	def contact_card(self):
		return f"{self.name} | {self.email} | {self.phone}"

class FeePayer:
	def calculate_fee(self,courses) :
		return sum(workshops[cource] for cource in courses)

class Participant (Person,FeePayer):
	def __init__(self,name,email,phone,courses,**details):
		super().__init__(name,email,phone)
		self.courses = list(courses)
		self.details = details

	def regestration_summary (self):
		total = self.calculate_fee(self.courses)
		return {
		"name": self.name,
		"courses": self.courses,
		"total_fee": total,
		"details": self.details
		}

participant = Participant(
	"Aarav Sharma",
	"aarav@example.com",
	"9876543210",
	["Python Basics", "Generative AI"],
	department="Computer Science",
	payment_mode="UPI"
	)
print(participant.contact_card())
print(participant.regestration_summary())
print("MRO:", [cls.__name__ for cls in Participant.mro()])
