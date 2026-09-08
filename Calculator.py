# write a pythin script to make a cli calculator with following functionalities: 
# it should perform arithemetic operaions
# it must not stop working until user allow it
# make a smart convertion if value generated has zero after decimal point it must be type casted to integer


flag = True
while(flag):
	n1 = int(input("Enter First Number : "))
	n2 = int(input("Enter Second Number : "))
	op = input("Enter Operator ( enter 0 to exit ): ")
	match op:
		case '+' :
			print(n1 + n2)
		case '-' :
			print(n1-n2)
		case '*' : 
			print(n1*n2)
		case '/' : 
			print(n1/n2)
		case '0' : 
			flag = False
