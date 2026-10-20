# dict = {'0':1,'1':2,'2':4,'3':8,'4':16,'5':32,'6':64,'7':128,'8':256}
# binary to decimal...
def convertDecimal(num):
	arr = [1,2,4,8,16,32,64,128,256]
	num = num[::-1]
	dec = 0
	for i in range(len(num)):
		# print(int(num[i]))
		dec = dec + int(num[i]) * arr[i]
	print(dec)

num = input("enter the binary code : ")
flag = True
for c in num:
	if (c not in "01"):
		print("Invalid Input")
		flag = False
		break
if(flag):
	convertDecimal(num)
else:
	print("Please Continue with another valid number like 0101 etc. " )
