# #Задача 1 - първо реяение 
# num1 = int(input('Enter a number :'))
# num2 = int(input('Enter a second number :'))
# if num1 > num2 :
#     print(num1)
# else :
#     print(num2)   

# #Задача 1 - второ решение
# num1 = int(input('Enter a number :'))
# num2 = int(input('Enter a second number :'))
# print(max(num1,num2))

# # Задача 2
# def greething(name,age,sex):
#     if age < 16 and sex=='m':
#         print (f'Master {name}')
#     elif age < 16 and sex=='f':
#         print (f'Miss {name}')    
#     elif age >= 16 and sex=='m':
#         print (f'Mr.{name}')
#     else :
#         print (f'Ms.{name}') 

# name = input('Enter your name :')
# age = int(input('Enter your age :'))
# sex = input('Enter your sex (f/m):')

# if sex=='m' or sex=='f':
#     greething(name,age,sex)
# else:
#     print('Wrong sex stat !')

# # Задача 3 
# num = int(input('Enter a number :'))
# if num % 2 == 0:
#     print(f'{num} is even ')
# else :
#     print(f'{num} is odd')    
# # Задача 4

# ciname_day = (input('Hor what day do you want a ticket ?')) 
# if ciname_day in ['Monday','Thuesday','Friday'] :
#     print (f'You whant a ticket for {ciname_day} that will be 12$')
# elif ciname_day in ['Wednesday','Thursday',] :  
#     print (f'You whant a ticket for {ciname_day} that will be 14$')
# elif ciname_day in ['Saturday','Sunday'] :  
#     print (f'You whant a ticket for {ciname_day} that will be 16$')    
# else :
#     print('Invalid day ')    

# #Задача 5

# from collections import Counter
# days_num = int(input('How many days do you whant to enter:'))
# my_days = []

# while days_num > 0 :
#     day = input(f'Enter a {days_num} day :')
#     if day in ['Monday','Tuesday','Wednesday','Tursday','Friday','Saturday','Sunday']:
#         my_days.append(day)
#         days_num = days_num-1
#     else :
#         print('Invalid day ')

# print(Counter(my_days))
