import math
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
if(a == 0):
    print("Not a Quadratic Equation")
    if(b == 0): 
        print("invalid equation")
    else:
        x = ((-c) / b)
        print(x)
else : 
    d = (b*b) - (4*a*c)
    if(d > 0):
        print("Roots are real and distinct")
        r1 = ((-b) + math.sqrt(d)) / (2*a)
        r2 = ((-b) - math.sqrt(d)) / (2*a)
        print(r1,r2)
    else :
        if(d == 0): 
            print("real and equal roots")
            r1 = r2 = (-b) / (2*a)
            print(r1,r2)
        else:
            print("Roots are complex")
            rreal =  (-b) / (2*a)
            rimg = (math.sqrt(abs(d))) / 2*a
            print(rreal," + ",rimg,"i ")
            print(rreal," - ",rimg,"i ")