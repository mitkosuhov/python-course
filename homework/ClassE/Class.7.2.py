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

# Задача 2 
def binary(x,y):
    min_index = 0
    max_idex = len(x) - 1 
    mid_index = (min_index + max_idex) // 2
    if x[mid_index] == y :
        return True 
    elif x[mid_index] > y :
        

