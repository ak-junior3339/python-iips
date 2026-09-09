# write a pythin script to make a cli calculator with following functionalities: 
# it should perform arithemetic operaions
# it must not stop working until user allow it
# make a smart convertion if value generated has zero after decimal point it must be type casted to integer
# add functions 
import re

def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b
flag = True
while(flag):
	res = 0
	pattern = r"\d+\."
	n1 = int(input("Enter First Number : "))
	n2 = int(input("Enter Second Number : "))
	op = input("Enter Operator ( enter 0 to exit ): ")
	match op:
		case '+' :
			res = add(n1,n2)
		case '-' :
			res = sub(n1,n2)
		case '*' : 
			res = mul(n1,n2)
		case '/' : 
			res = div(n1,n2)
		case '0' : 
			flag = False

	if re.match(r"^\d+\.0$",str(res)):
		print(int(res))
	else:
		print(res)

