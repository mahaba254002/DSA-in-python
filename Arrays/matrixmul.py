a = [[1, 1, 1],
     [2, 2, 2],
     [0, 0, 0]]

b = [[2, 1],
     [2, 1],
     [2, 1]]

result = [[0, 0],
          [0, 0],
          [0, 0]]

print(len(a))
print(len(b[0]))
#product:col 1st matrix=row 2nd matrix
if len(a[0]) != len(b):
    print("Error: The number of columns in matrix a must be equal to the number of rows in matrix b.")
else:
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
                #no of row 1st matrix,column 2nd matrix

    # Print the result
for row in result:
    print(row)