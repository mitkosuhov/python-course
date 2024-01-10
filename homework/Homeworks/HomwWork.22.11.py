# #задача 1 
# side1 = float(input('Въведете една страна на правоъгълника (см.):'))
# side2 = float(input('Въведете другата страна на правоъгълника (см.):'))
# face = side1 * side2
# if side1 != side2 :
#     if side1 > side2:
#         print('Лицето на правоъгълника е с площ ',face,'кв.см.')
#         print('      ',side1,'     ')
#         print(' ____________________')
#         print('|                    |')
#         print('|        ',face,'     |',side2)
#         print('|____________________|')
#         print('Лицето на правоъгълника е с площ ',face,'кв.см.')
#     if side1 < side2 :
#         print('Лицето на правоъгълника е с площ ',face,'кв.см.')
#         print('      ',side2,'     ')
#         print(' ____________________')
#         print('|                    |')
#         print('|        ',face,'    |',side1)
#         print('|____________________|')
#         print('Лицето на правоъгълника е с площ ',face,'кв.см.')
        
    
# else :
#     print('Имате квадрат с лице ',face,'кв.см.')
#     print(' ',side1,'')
#     print(' _________')
#     print('|         |')
#     print('|',face,'  |',side2)
#     print('|_________|')

# #задача 2 и 3


# name  = input('Hi , whats your name ?')
# last_name = input('And you last name ?')
# age = input('How old are you ')
# home_town =input('And where are you from ?')
# print ('Ýour name is '+ name +" "+  last_name + ' you are ' + age + ' years old , and you came from '+ home_town)
 


# #задача 4
# import datetime

# today = datetime.date.today()
# year_one = today + datetime.timedelta(days=365)
# print(today)
# print(year_one)

# #задача 5
# num1 = int(input('Give me one number '))
# num2 = int(input('Give me a second number '))
# num3 = int(input('And a thurd '))
# sum_of = [num1,num2,num3]
# print('The sum of three is :',sum(sum_of))
# print('Bigest number is :',max(sum_of))
# print('Smallest number is :',min(sum_of))


#задача 6  
num_list = [] # Списък в който ще поставяме въведените числа от конзолата 

while True :   # Създаваме повтарящ се цикъл който да приема числа под формата на str .
    nums = input("Give me a number :") 
    
    if nums == 'sum': # Създаваме дума с който да прекратим цикала и да принтираме сумата от числата 
        print('Your numbers are ',num_list ,'and they sum is ', sum(num_list))
        break
    if nums != 'sum': # Проверяваме дали str. може да бъде променен в float , ако не бива нулиран 
        try:
            nums = float(nums)
            num_list.append(nums)
        except :
            nums = 0