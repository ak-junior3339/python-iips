import time as t
def fact(n):
	if ((n==0) or (n==1)):
		return 1 
	else : 
		return n * fact(n-1)

n = int(input("Enter a number : "))
start = t.time()
f = fact(n)
end = t.time()
print("total time = ",(end - start))
print(f)