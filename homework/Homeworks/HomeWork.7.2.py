# Задача 1 

# def bubble(x):
#     index_of_list = len(x)-1
#     corect = True 
#     while corect :
#         corect = False
#         for i in range(0,index_of_list):
#             if x[i] > x[i+1]:
#                 x[i],x[i+1] = x[i+1],x[i]
#                 corect = True 
            
#     return x             
# nums = [9,7,3,2,4,1,6,5,8]

# print(bubble(nums))

# Задача2 

# def select(x):
#     for i in range(len(x)):
#         min_index = i
#         for j in range(i+1,len(x)):
#             if x[j] < x[min_index]:
#                 min_index = j
#         x[i],x[min_index] = x[min_index],x[i]
#     return x    

# nums = [9,7,3,2,4,1,6,5,8,11,13,15,10,12]
# print(select(nums))

# Задачи 3

# def insertion(x):
#     for i in range(1,len(x)):
#         j = x[i]
#         while x[i-1] > j and i > 0 :
#             x[i],x[i-1] = x[i-1],x[i]
#             i -= 1 
#     return x 
        
# nums = [9,7,3,2,4,1,6,5,8,11,13,15,10,12]
# print(insertion(nums))

# Задача 4
import random

def binary(x,y):
    min_index = 0
    max_index = len(x) - 1
    while min_index <= max_index:
        mid_index = (min_index + max_index)//2
        mid_value = x[mid_index]
        if mid_value == y:
            return mid_value
        elif mid_value > y :
            max_index = mid_index -1
        else:
            min_index = mid_index +1 
    return f'Нямя това число '   
      
lista = random.sample(range(1, 101), 100) 

print(binary(lista,23))
print(lista)
 
        

