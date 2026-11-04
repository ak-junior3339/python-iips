# Method 01..
def area(x,y=None) : 
	if (y == None):
		return x * 3.14 * x 
	else : 
		return x * y
print("area = ",area(2))
print("area 2 = ",area(3,4))