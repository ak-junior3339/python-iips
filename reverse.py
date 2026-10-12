# # to find reverse of integer
string = input("Enter a string : ")
n = len(string)-1
temp = " "
# for i in range(n,-1,-1):
# 	temp = temp + (string[i])

# print(temp)
for i in string: 
	temp = i + temp 
print(temp)


# [::-1]