A = []
list1=[]
for B in range(1, 31):
    A.append(B**2)
for x in A:
    if x % 2 == 0:
        list1.append(x)

print("List:", list1)
print("First 5:", list1[:5])
print("Last 5:", list1[-5:])
