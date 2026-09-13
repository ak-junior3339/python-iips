num = int(input("Enter the Number : "))
bin = []
while (num!=0) : 
	bin.append(num%8)
	num = num // 8

print(bin[::-1])
