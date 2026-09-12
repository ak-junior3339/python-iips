arr = [1,2,3,4,5]
pos = 2
item = 69
for i in range(len(arr)-1,pos-1,-1):
	if(i == len(arr)-1):
		arr.append(arr[i])
	else:
		arr[i+1] = arr[i]
arr[pos] = item

print(arr)