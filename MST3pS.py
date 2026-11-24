import re
workshops = {
	"Python Basics": 500,
	"Data Analytics": 800,
	"Generative AI": 1000,
	"Web Development": 750
}
# print("Available workshops:")
# for title, fee in workshops.items():
# 	print(f"{title:20} ₹{fee}").

sorted_workshops = sorted(workshops.items(),key=lambda item : item[1],reverse=True)
for title, fee in sorted_workshops:
	print(f"{title:20} ₹{fee}")

def show_reg(name,*cources,**details):
	print("Participant:", name)
	print("Selected workshops:", cources)
	print("Additional details:", details)

show_reg(
	"Aarav Sharma",
	"Python Basics",
	"Generative AI",
	department="Computer Science",
	designation="Assistant Professor",
	payment_mode="UPI"
)

EMAIL_PATTERN = r"^[\w.%-]+@[\w.-]+\.[A-Za-z]{2,}$"
PHONE_PATTERN = r"^[6-9]\d{9}$"

def valid_email(email):
	return re.fullmatch(EMAIL_PATTERN, email) is not None
def valid_phone(phone):
	return re.fullmatch(PHONE_PATTERN, phone) is not None


class RegestrationError(Exception):
	pass

def validate_participant(name,email,phone,courses):
	if not name.strip():
		raise RegestrationError("Name cannot be empty.")
	if not valid_email(email):
		raise RegestrationError("Invalid Email")
	if not valid_phone(phone):
		raise RegestrationError("Phone must be a valid 10-digit Indian mobile number.")
	if not courses:
		raise RegestrationError("Select at least one workshop.")
	unknown = [course for course in courses if course not in workshops]
	if unknown:
		raise RegestrationError(f"Unknown workshop(s): {unknown}")
	return True

try :
	validate_participant(
	"Aishwarya", "aarav@example.com", "9876543210",
	["Python Basics", "Generative AI","Power BI"]
	)
	print("Validation successful!")
except RegestrationError as error:
	print("Registration rejected:", error)














