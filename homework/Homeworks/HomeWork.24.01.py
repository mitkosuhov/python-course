Задача 1
import requests

s = requests.get("https://pypi.org/project/requests/")

print(s.text)

# Задача 2
# from math import sqrt

# num = sqrt(49)
# print(num)

#Задача 3 

# class Calculator :

#     def add(self,x,y):
#         return x+y
    
#     def subtract(self,x,y):
#         return x-y
    
#     def multi(self,x,y):
#         return x*y
    
#     def divide(self,x,y):
#         if y != 0 :
#             return x/y 
#         else:
#             return 'Не се дели на нула '

# result = Calculator()

# print(result.add(3,6))
# print(result.subtract(9,7))
# print(result.multi(4,4))
# print(result.divide(94,4))



#Задача 4

# import datetime as dt

# print(dt.datetime.now())
#Задача 5
# import os 

# print(os.getcwd())
# os.chdir(r'C:\Users\Mitko\Desktop\HomeWork.12.12')
# print(os.getcwd())
# os.chdir(r"C:\Users\Mitko\Desktop\python2023")
# print(os.getcwd())

#Задача 6

# import random

# for i in range(5):
#     print(random.choice(range(1,10)))

