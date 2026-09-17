def missing_number(arr):
	n = len(arr)
	total_sum = (n * (n+1))//2
	return total_sum -  sum(arr)

missing = missing_number([3,0,1])
print(missing)