# For Else Loop
n = int(input("Enter Value : "))
for i in range(2,n):
	if(n%i)==0:
		print("Composite")
		break
else:
	print("Prime")