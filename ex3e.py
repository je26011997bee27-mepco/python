n=input("enter the list of binary numbers")
delim=','
a=n.split(delim)
list1=[]
for x in a:
    if(int(x,2)%5==0):
        list1.append(x)
print (list1)
