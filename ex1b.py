import math
a=int(input("coef.of x^2:"))
b=int(input("coef.of x:"))
c=int(input("constanat:"))
d=(b*b)-(4*a*c)
if(d==0):
    e=-b/(2*a)
    print("real and equal root:",e)
elif(d>0):
    e=(-b+math.sqrt(d))/(2*a)
    f=(-b-math.sqrt(d))/(2*a)
    print("real and distinct roots:",e,",",f)
else:
    e=-b/(2*a)
    f=(math.sqrt(-d))/(2*a)
    print("complex roots:")
    print(e,"+j",f)
    print(e,"-j",f)
