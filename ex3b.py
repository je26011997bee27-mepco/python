a=int(input("enter the vale of a "))
l=0
n=a
for x in range(1,a+1):
    l=l+1
    for y in range(a-l):
        print (" ",end="")
    for z in range(1,l+1):
        print ("* ",end="")
    print ()
    
for i in range(a-1,0,-1):
    n=n+1
    for j in range(a-i):
        print (" ",end="")
    for k in range(1,i+1):
        print ("* ",end="")
    print ()
