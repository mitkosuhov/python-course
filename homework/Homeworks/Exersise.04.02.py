# Task 1
import numpy as np 

matrix1 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
matrix2 = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])

print(matrix1 + matrix2)

# Task 2

matrix = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])

print(np.transpose(matrix))

#Task 3

matrix = np.array([[5,7,1],[3,4,6],[9,3,2]])

print(matrix*5)

#Task 4

matrix = np.array([[14,12,3],[5,11,6],[7,6,1]])

print(np.linalg.det(matrix))

#Task 5

matrix_random1 = np.random.randint(9,size=(3,3))
matrix_random2 = np.random.randint(9,size=(3,3))

print(f'Първа произвилна матрица \n{matrix_random1}')
print(f'Втора произволна матрица \n{matrix_random2}')
print(f'Простите числа \n{matrix_random1*matrix_random2}')

# Task 6

array1 = np.random.randint(100,size=5)
print(array1)
print(np.mean(array1))

# Task 7 

array1 = np.random.randint(10,size=5)
array2 = np.random.randint(10,size=5)
print(array1)
print(array2)
array3 =array1*array2
print(f'{array3}Поелементно умножаване')

# Task 8

array = np.random.randint(100,size=10)
print(array)
print(np.max(array))

# Task 9

array = np.random.randint(100,size=10)
print(array)
print(np.min(array))

# Task 10

import pandas as pd

file_path = (r'C:\Users\Mitko\Desktop\python2023\homework\Homeworks\bfd-2023.csv')

df = pd.read_csv(file_path)

print(df.head())

# Task 11
# Изполвам готов DataFrame който ChatGPT ми написа 
data = {
    'Име': ['Иван', 'Мария', 'Петър', 'Анна', 'Георги', 'Даниел', 'Стефани', 'Борис', 'Елена', 'Николай'],
    'Години': [25, 30, 22, 28, 35, 28, 24, 29, 31, 26],
    'Град': ['София', 'Пловдив', 'Варна', 'София', 'Бургас', 'София', 'Варна', 'Пловдив', 'София', 'Бургас'],
    'Заетост': ['Специалист', 'Мениджър', 'Студент', 'Инженер', 'Мениджър', 'Програмист', 'Архитект', 'Мениджър', 'Специалист', 'Преподавател'],
    'Заплата': [50000, 70000, 0, 55000, 80000, 60000, 75000, 72000, 55000, 65000]
}

names = pd.DataFrame(data)
print(names['Години'].mean())

# Task 12
# Използвам DataFrame от предишната задача 
sofia_names = names[names['Град'] == 'София']
print(sofia_names)

# Task 13 
# Използвам DataFrame от предишната задача
names['Увеличена заплата']=names['Заплата']*1.2
print(names)

# Task 14

grouped_data_city = names.groupby('Град')
grouped_data_duty = names.groupby('Заетост')

print(grouped_data_city['Години'].mean())
print(grouped_data_duty['Заплата'].mean())

# Task 15 

class Stack :
    def __init__(self):
        self.items = []

    def Push(self,x):
        self.items.append(x)

    def Pop(self):
        self.items.pop()
    
    def revers(self):
        return self.items[::-1]
   

stack = Stack()

stack.Push(2)
stack.Push(5)
stack.Push(7)
stack.Push(9)
stack.Pop()
print(stack.items)
# Task 16
print(stack.revers())
# Task 17 
class queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)
    
qe = queue()
qe.enqueue(4)
qe.enqueue(2)
qe.enqueue(7)

print( qe.items)

dequeued_item = qe.dequeue()
print(dequeued_item)
print(qe.items)

# Task 18

class tree:
    def __init__(self, base):
        self.base = base
        self.left = None
        self.right = None

    def dfs_recursive(self,x):
        if x:
            print(x.base, end=' ')
            x.dfs_recursive(x.left)
            x.dfs_recursive(x.right)    


root = tree(1)
root.left = tree(2)
root.right = tree(3)
root.left.left = tree(4)
root.left.right = tree(5)
root.right.left = tree(6)
root.right.right = tree(7)

root.dfs_recursive(root)

# Task 19
import networkx as nx

import matplotlib.pyplot as plt

Gar = nx.DiGraph()

Gar.add_nodes_from([1, 2, 3, 4, 5 , 6])

Gar.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1),(5 ,2) , (6 , 4)])

nx.draw(Gar,  with_labels=True, arrows=True)
plt.show()

