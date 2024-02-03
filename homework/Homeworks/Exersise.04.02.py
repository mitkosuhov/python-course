# Task 1
import numpy as np 

# matrix1 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
# matrix2 = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])

# print(matrix1 + matrix2)

# Task 2

# matrix = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])

# print(np.transpose(matrix))

#Task 3

# matrix = np.array([[5,7,1],[3,4,6],[9,3,2]])

# print(matrix*5)

#Task 4

# matrix = np.array([[14,12,3],[5,11,6],[7,6,1]])

# print(np.linalg.det(matrix))

#Task 5

# matrix_random1 = np.random.randint(9,size=(3,3))
# matrix_random2 = np.random.randint(9,size=(3,3))

# print(f'Първа произвилна матрица \n{matrix_random1}')
# print(f'Втора произволна матрица \n{matrix_random2}')
# print(f'Простите числа \n{matrix_random1*matrix_random2}')

# Task 6

# array1 = np.random.randint(100,size=5)
# print(array1)
# print(np.mean(array1))

# Task 7 

# array1 = np.random.randint(10,size=5)
# array2 = np.random.randint(10,size=5)
# print(array1)
# print(array2)
# array3 =array1*array2
# print(f'{array3}Поелементно умножаване')

# Task 8

# array = np.random.randint(100,size=10)
# print(array)
# print(np.max(array))

# Task 9

# array = np.random.randint(100,size=10)
# print(array)
# print(np.min(array))

# Task 10

import pandas as pd

# file_path = (r'C:\Users\Mitko\Desktop\python2023\homework\Homeworks\bfd-2023.csv')

# df = pd.read_csv(file_path)

# print(df.head())

# Task 11

file_path = (r'C:\Users\Mitko\Desktop\python2023\homework\Homeworks\New.csv')
file = pd.read_csv(file_path)
colum= 'Age'
print(file[colum].mean())



