# dict = {'0':1,'1':2,'2':4,'3':8,'4':16,'5':32,'6':64,'7':128,'8':256}
# binary to decimal 
arr = [1,2,4,8,16,32,64,128,256]
num = input("enter the binary code : ")
num = num[::-1]
dec = 0
for i in range(len(num)):
	print(int(num[i]))
	dec = dec + int(num[i]) * arr[i]

print(dec)