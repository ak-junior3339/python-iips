counter = 0 
def incr_counter():
	global counter
	print(counter)
	counter += 1 
	print(counter)
incr_counter()