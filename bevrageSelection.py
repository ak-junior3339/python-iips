# write a python script to select the bevrage based on the given temperature is the 
# temperature is between 20 - 30  -- > tea if greater than 30 then cold coffee if temperature 
# is less than 20 then hot choclate

temp = float(input("Enter the Temperature in Celsius : "))
print("Drink water if no money! or else drink \n")
if (temp >=20 and temp <=30):
	print("Drink yeowle ki chai")
elif (temp > 30):
	print("cold coffe")
elif(temp < 20 ):
	print("hot choclate")


