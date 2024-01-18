# Задача 7
# my_word='mitkoplamenovsuhov'

# def Index_check(x):
#     try :
#         print(x[18])
#     except IndexError as a :
#         print(f'Incorect , the error {a}')    

# Index_check(my_word)
# Задача 8 

# num = input('Enter a number:')

# def num_chek(x):
#     try :
#         x = int(x)
#         print(f'{x} is integer number ')
#     except ValueError as a :
#         print(f'{x} is not integer number ')    

# num_chek(num)        

# Задача 9 

# def words_conc():
#     try:
#         result = 10 + '15'
#         print(result)
#     except TypeError as a :
#         print(f' and  are {a}')

# words_conc()

# Задача 10

# pass_word = input('Enter a password :')


# def PassWord_chek(x):
#     if len(x) < 8 :
#         print('The password is to short !')
#     if not any (i.isdigit() for i in x ):
#         print('The pasword dosent have digits Leter !') 
#     if not any (i.isuper() for i in x ):
#         print('Pasword dosent have upers !')   


# try:
#     PassWord_chek(pass_word)
#     print('Pasword is GOOD ')

# except:
#     print('Error')    

# Задача 11

num1 = int(input('Enter first number :'))
num2 = int(input('Enter a second number :'))

def del_fun(x,y):
    try:
        result = x/y
        print(result)
    except ValueError as a :
        print(f'{a} this ')

del_fun(num1,num2)