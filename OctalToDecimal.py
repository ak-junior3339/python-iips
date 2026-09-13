# dict = {'0':1,'1':2,'2':4,'3':8,'4':16,'5':32,'6':64,'7':128,'8':256}
arr = [1,8,64]
num = input("enter the Ocatal Number  : ")
num = num[::-1]
dec = 0
for i in range(len(num)):
	dec = dec + int(num[i]) * arr[i]

print(dec)