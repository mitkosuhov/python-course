# #Задача 1
# class Calculator :

#     @staticmethod
#     def add(*args):
#         return sum(args)
    
#     @staticmethod
#     def multiply(*args):
#         x = 1
#         for i in args:
#             x *= i 
#             x = x 
#         return x        
#     @staticmethod
#     def divide(*args):
#         x = args[0]
#         for i in args[1:]:
#             x /= i
#             x = x
#         return x
#     @staticmethod
#     def subtract(*args):
#         x = args[0]
#         for i in args[1:]:
#             x -= i
#             x = x
#         return x

# print(Calculator.add(1,2,3,4))
# print(Calculator.multiply(1,2,3,4))
# print(Calculator.divide(60,2,5))
# print(Calculator.subtract(60,2,5))

# Задача 2 
# import roman 
# class Integer :
#     def __init__(self,int):
#         self.int = int

#     def from_float(float_value):
#         if isinstance(float_value,float):
#             return print('Value is float')
#         else :
#             return print("value is not a float")
        
#     def from_roman(value):
#         value1 = value.upper()
#         return roman.fromRoman(value1)
    
#     def from_string(value):
            
#             if isinstance(value,str):
#                 try:
#                     value = int(value)
#                     return print(value)
#                 except:
#                     return print('Wrong type ')
#             else:
#                 return print('Wrong type ')

# Integer.from_float(123.3)
# print(Integer.from_roman('iv'))
# Integer.from_string('15')


    
