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

# print(Calculator.add(5, 10, 4))
# print(Calculator.multiply(1, 2, 3, 5))
# print(Calculator.divide(100, 2))
# print(Calculator.subtract(90, 20, -50, 43, 7))

#Задача 2 
# import roman 
# class Integer :
#     def __init__(self,value):
#         self.value = value

#     def from_float(float_value):
#         if not isinstance(float_value, float):
#             return "value is not a float"

#     def from_roman(value):
#         value = roman.fromRoman(value)    
#         return value   
    
#     def from_string(value):
#         if  isinstance(value, str):
#             try:
#                 return int(value)
#             except ValueError:
#                 return "wrong type"
#         else:
#             return "wrong type"   

# first_num = Integer(10)
# print(first_num.value)
# second_num = Integer.from_roman("IV")
# print(second_num)
# print(Integer.from_float("2.6"))
# print(Integer.from_string(2.6))
    


# Задача 5 
# def make_bold(func) :
#     def wrapper(*args,**kwars):
#         result = func(*args,**kwars)
#         return f'<b>{result}</b>'
#     return wrapper

# def make_italic(func) :
#     def wrapper(*args,**kwars):
#         result = func(*args,**kwars)
#         return f'<i>{result}</i>'
#     return wrapper

# def make_underline(func) :
#     def wrapper(*args,**kwars):
#         result = func(*args,**kwars)
#         return f'<u>{result}</u>'
#     return wrapper

# @make_bold
# @make_italic
# @make_underline
# def greet(name):
#     return f"Hello, {name}"
# print(greet("Peter"))



# Задача 6
# def add_tag(tag_name):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             return f'<{tag_name}>{result}</{tag_name}>'
#         return wrapper
#     return decorator

# @add_tag("b")
# @add_tag("em")
# @add_tag("u")
# def greet(name):
#     return f"Hello, {name}"
# print(greet("Peter"))