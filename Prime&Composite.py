# write a pythin script to indentify a given number is prime or composite
# RG droomy how to solve it by computer
n = int(input("Enter the Number To check : "))
flag = False
for i in range(2,(n//2)+1):
	if (n%i) == 0 :
		print("Not a prime Number")
		print(f"It is divisible by {i} other than 1 and itself.")
		flag = True
if (flag==False):
	print("Prime numbers")