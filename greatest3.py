# write a python script to identify greatest of 3 user defined integers
a = int(input("Enter The first Number: "))
b = int(input("Enter The Second Number: "))
c =int(input("Enter The third Number: "))
print(a,"is greater") if ((a > b) and (a > c)) else print(b,"is greater") if ((b > a) and (b > c)) else print(c,"is greater")