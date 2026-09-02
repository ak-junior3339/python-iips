#pythin script to calculate average of n user defied integers
n = int(input("Enter a Number : "))
sum = 0
for i in range(n):
	num = int(input("Enter the number: "))
	sum +=num
print(float(sum/n))

