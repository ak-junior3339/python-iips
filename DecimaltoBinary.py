# decimal to binary
num = int(input("Enter the Number : "))
bin = []
while (num!=0) : 
	bin.append(num%2)
	num = num // 2

print(bin[::-1])
