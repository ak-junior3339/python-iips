def mostFreq(arr) : 
	max_frequency = -1
	frequent_element = -1
	for i in arr:
		if(arr.count(i) > max_frequency):
			frequent_element = i
			max_frequency = arr.count(i)
		else : 
			continue	
	return [frequent_element,max_frequency]
result = mostFreq([1,1,1,1,4,4,4,6,7,9])
print(result)