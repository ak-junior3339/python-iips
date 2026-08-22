def printN(n):
	i = 0
	if(n == 0):
		return arr
	else :
		arr[i] = n
		return printN(n-1)


arr = printN(10)
print(arr[::-1])
