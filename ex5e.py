A = [[1, 2, 3],
     [4, 5, 6]]

B = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

print("Transpose:")
for C in B:
    print(C)
