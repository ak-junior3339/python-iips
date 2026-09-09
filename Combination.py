# python script to find cobination where n and r are user defined
def fact(n):
	fact = 1
	for i in range(n,0,-1):
		fact = fact * i
	return fact

n = int(input("Enter n : "))
r = int(input("enter r : "))
p = fact(n)/(fact((n-r)) * fact(r))

print("Combination (P) =", int(p))
