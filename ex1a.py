import math
n=int(input("enter the number of parameters:"))
if(n==2):
    a=float(input("height:"))
    b=float(input("base:"))
    c=0.5*a*b
    print("area=",c)
else:
    a=float(input("side 1:"))
    b=float(input("side 2:"))
    c=float(input("side 3:"))
    s=(a+b+c)/2
    d=(s*(s-a)*(s-b)*(s-c))
    print("area=",math.sqrt(d))
        
