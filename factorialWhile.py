# print table using while
n = int(input("Enter the number : "))
fact = 1
while(n!=0):
	fact = fact * n 
	n-=1

print(fact)