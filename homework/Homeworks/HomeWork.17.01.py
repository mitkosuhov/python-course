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
import roman 
class Integer :
    def __init__(self,int_value):
        self.int_value = int_value

    
    def from_float(float_value):
        if isinstance(float_value,float):
            return print('Value is float')
        else :
            return print("value is not a float")
        
    def from_roman(value):
        value1 = value.upper()
        return roman.fromRoman(value1)
    
    def from_string(value):
            
            if isinstance(value,str):
                try:
                    value = int(value)
                    return print(value)
                except:
                    return print('Wrong type ')
            else:
                return print('Wrong type ')

first_num = Integer(10)
print(first_num.int_value)
second_num = Integer.from_roman("IV")
# print(second_num.value1)
print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))


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