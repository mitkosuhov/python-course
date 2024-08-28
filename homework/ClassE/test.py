import numpy as np

# Създаване на матрици с NumPy
matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[2, 2, 2], [3, 3, 3], [4, 4, 4]])

# Извършване на матрично умножение
result = np.dot(matrix1, matrix2)

# Отпечатване на резултата
print(result)
