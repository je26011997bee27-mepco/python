A = [1, 2, 3, 4, 5, 6, 7, 8]
B = int(input("Enter start index: "))
C = int(input("Enter end index: "))

A = A[B:C]

A = [i for i in A if i % 2 == 0] + [i for i in A if i % 2 != 0]

print("Result:", A)
