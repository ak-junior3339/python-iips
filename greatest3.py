# write a python script to identify greatest of 3 user defined integers
# a = int(input("Enter The first Number: "))
# b = int(input("Enter The Second Number: "))
# c =int(input("Enter The third Number: "))
### LOGIC - 01 SMALL AND SWEET
# print(a,"is greater") if ((a > b) and (a > c)) else print(b,"is greater") if ((b > a) and (b > c)) else print(c,"is greater")

### LOGIC -02 LONG AND CAUSES ERROR FOR EQUAL NUMBERS 
# if (a > b):
# 	if (a > c):
# 		print(a,"is greater")
# 	elif(c > b):
# 		print(c,"is gretest")
# 		return 
# elif(b>a):
# 	if(b > c):
# 		print(b,"is greater")
# else:
# 	print(c,"is greater")


### LOGIC - 03 EXCELLENT AS PER ME : 
def greatest(a,b,c):
	if (a > b):
		if (a > c):
			return a 
		else:
			return c
	else :
		if(b > c) :
			return b 
		else :
			return c



print(greatest(4,7,1))
print(greatest(7,3,6))
print(greatest(1,5,9))
print(greatest(5,5,7))
print(greatest(5,5,1))