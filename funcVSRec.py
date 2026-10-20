import time as t
def fact_R(n):
	if ((n==0) or (n==1)):
		return 1 
	else : 
		return n * fact_R(n-1)

def fact_I(n):
	fact = 1
	for i in range(1,n+1):
		fact= fact * i
	return fact
for n in range(1,900) : 
	start = t.time()
	f = fact_R(n)
	end = t.time()
	start_f = t.time()
	ff = fact_I(n)
	end_f = t.time()
