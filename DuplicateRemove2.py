def removeDupli(lst):
	arr = []
	if (len(lst) != 0):
		for i in lst:
			if i not in arr:
				arr.append(i)
		return arr
	else:
		print("list does not contain anything.")

arr = removeDupli([1,1,2,2,5,7])
print(arr)