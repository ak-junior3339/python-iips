def removeDupli(lst):
	arr = []
	if (len(lst) != 0):
		for i in lst:
			if i not in arr:
				arr.append(i)
			else:
				print("Duplicate Element  : ",i)
	else:
		print("list does not contain anything.")

removeDupli([1,1,2,2,5,7])
