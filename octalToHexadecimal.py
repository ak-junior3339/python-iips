# ...
def OctalToHexa(num):
	if(num == '0'):	
		print("Zero entered")
		return
	dec = convertDecimal(num)
	hex_chars = "0123456789ABCDEF"
	hexa = ""
	while dec > 0 :
		remainder = dec%16
		hexa=hex_chars[remainder] + hexa
		dec= dec // 16

	print(hexa)


def convertDecimal(num):
	arr = [1,8,64,512,4096]
	num = num[::-1]
	dec = 0
	for i in range(len(num)):
		# print(int(num[i]))
		dec = dec + int(num[i]) * arr[i]
	return (dec)

input = str(input("Enter A Number : "))
OctalToHexa(input)
 