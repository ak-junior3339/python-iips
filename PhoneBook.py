# python script to make a phone book where 
# CRUD
contact = []
def Create():
	name = input("Enter Name : ")
	number = input("Enter Number : ")
	address = input("Enter the address : ")
	email = input("Enter the email address : ")
	contact.append(dict({'Name' : name , 'Number' : number,'Address':address,'Email':email}))
	print("✅")
def update():
	n = input("Enter The Name to search : ")
	for i in contact:
		# print(i)
		if i['Name'].lower() in n.lower():
			print("Record Found")
			print("Please Update the record now.....")
			name = input("Enter Name : ")
			i['Name'] = name
			number = input("Enter Number : ")
			i['Number'] = number
			address = input("Enter the address : ")
			i['Address'] = address
			email = input("Enter the email address : ")
			i['Email'] = email
			print("✅ Update Succesfull")
			break
		else:
			continue

def delete():
	n = input("Enter The Name to search : ")
	for i in range(len(contact)):
		if n.lower() == contact[i]['Name'].lower():
			print("Record Found")
			print("Deleting.....")
			contact.pop(i)
			print('✅ Delete Succesfull')
			break
		else:
			continue
			
def search():
	n = input("Enter The Name to search : ")
	for i in contact:
		if i['Name'].lower() == n.lower():
			print("Record Found")
			print("Name : ",i['Name'])
			print("Phone Number : ",i['Number'])
			print("Address : ",i['Address'])
			print("Email: ",i['Email'])
			break	
		else:
			continue

def printAll():
	for i in contact:
		print("Record Found")
		print("Name : ",i['Name'])
		print("Phone Number : ",i['Number'])
		print("Address : ",i['Address'])
		print("Email: ",i['Email'])

print("Welcome to PhoneBook")
while (True):
	print("Happy to Help : ")
	print("1-Create an Entry")
	print("2-Update an Entry")
	print("3-Delete an Entry")
	print("4-Search for an Entry")
	print("5-See each and every Entry")
	print("6- EXIT")
	op = input("How May we Help you : ")
	match op:
		case "1" : 
			Create()
		case "2":
			update()
		case "3":
			delete()
		case "4":
			search()
		case "5":
			printAll()
		case "6":
			print("Nice meeting you! See you soon")
			break
		case _ :
			print("Seems like you entered an option out of my capablities")

