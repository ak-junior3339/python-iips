# print table using while
flag = True
while(flag):
	n = int(input("Enter the number : "))
	fact = 1
	while(n!=0):
		fact = fact * n 
		n-=1

	print(fact)

	ch=input("Enter 0 to exit or else press button")
	if(ch=='0'):
		flag=False