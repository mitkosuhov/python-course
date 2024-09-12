matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print("Оригинална матрица:")
for row in matrix:
    print(row)
transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("\nТранспонирана матрица:")

for i in transposed_matrix:
    print(i)
