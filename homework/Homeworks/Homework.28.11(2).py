# Задача 2
def greething(name,age,sex):
    if age < 16 and sex=='m':
        print (f'Master {name}')
    elif age < 16 and sex=='f':
        print (f'Miss {name}')    
    elif age >= 16 and sex=='m':
        print (f'Mr.{name}')
    else :
        print (f'Ms.{name}') 

name = input('Enter your name :')
age = int(input('Enter your age :'))
sex = input('Enter your sex (f/m):')

if sex=='m' or sex=='f':
    greething(name,age,sex)
else:
    print('Wrong sex stat !')