# internal questions 
data = [4,7,0,12,-3,9,15]
i=0
total = 0
count = 0
while True:
	value = data[i]
	i+=1
	if value==0 or value<0:
		continue
	if value > 10 and count >=2:
		break
	total+=value
	count+=1
	if i>= len(data):
		break
print(i,count,total)