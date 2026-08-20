# pythn script to check whether a number is even or odd
var_num = int(input("Enter a Integer Number : "))
# print("You entered Zero") if var_num ==0 else print("Number Even") if (var_num % 2 == 0) else print("Not even")
if (var_num == 0):
	print("You entered zero")
elif (var_num % 2==0):
	print("Even Number")
else:
	print("Odd number")