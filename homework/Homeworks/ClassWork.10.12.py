# side1 = float(input('Ener a side of tiangle :'))
# side2 = float(input('Ener a side of tiangle :'))
# side3 = float(input('Ener a side of tiangle:'))
# triangle = bool

# if (side1 + side2) > side3 or (side3 + side2) > side1 or (side1 + side3) > side2 :
#     print('It can be triangle ')
#     triangle = True
# else:
#     print('It cant be triangle ')

# if triangle == True :
#     sids = [side1,side2,side3]  

#     hip = max(sids)
#     s1 = min(sids)
#     sids.remove(hip)
#     sids.remove(s1)
#     print(f'Hip is {hip} and the small sited is {s1} and the mid is {sids[0]}')

#     if hip**2 == s1**2 + sids[0]**2:
#         print('Може да бъде правоъгален ')
#     else :
#         print('Не може да бъде ')    

# proc = float(input("Enter your grade in procent :"))
# if proc >= 90 and proc <= 100 :
#     print('Отличен')
# elif proc >= 75 and proc <= 89 :
#     print('Мн.добър')
# elif proc >= 60 and proc <= 74 :
#     print('Добър')
# elif proc >= 45 and proc <= 59 :
#     print('Среден')        
# elif proc >= 0 and proc <= 44 :
#     print('Слаб')        

# import datetime
# year_of  = int (input('Въведете вашета възраст :'))
# x = datetime.datetime.now()
# age = x.year - year_of
# if age >= 18 :
#     print('Пълнолетен')
# else :
#     print('Не пълнолетен ')    
# sym = input('Въведи буква от азбуката ')
# glasni = ['а','ъ','о','у','е','и']
# if sym in glasni :
#     print(f'{sym} е гласна')
# else :
#     print('Е съгласна ')    
# mass = float(input('Въведете вашето тегло :'))
# heit = float(input('Въведете вашета височина :'))
# bmi = mass/heit**2
# if bmi < 16 :
#     print('Недохранен ')
# elif bmi <= 24 and bmi >= 16 :
#     print('Нормално тегло ')    
# elif bmi <= 30 and bmi >= 25 :
#     print('Наднормено тегло ')     

# value = float(input('Въведете вашия доход :'))
# if value <= 10000 :
#     print(f'Данъка е {value*0.1}') 
# elif value >10000 and value<= 20000 :
#     print(f'Данъка е {value*0.15}')
# else :
#     print(f'Данъка е {value*0.2}')

# num1 = float (input ('Enter a number :'))
# num2 = float (input ('Enter a number :'))
# num3 = float (input ('Enter a number :'))
# med  = [num1,num2,num3]
# med.sort()
# print(med[1])

# choice = input('Въведете температурате в гардуси или целзии ').lower()
# if choice == 'f' :
#     temp= float (input('Въведи температурата в целзии:'))
#     print((temp*1.8)+32)
# elif choice == 'c' :
#     tempa= float (input('Въведи температурата в фаренфаин:'))
#     print((tempa - 32)/1.8)   
# num = int(input('Въведете число :'))
# front = []
# for x in range(num,0,-1) :
#     front.append(x)
# fact =1
# for x in list(front):
#     fact *= x  
#     print(fact)

# print(fact) 
data_day =int(input('Enter a date:'))
date_mount =int(input('Enter a mount:'))
date_year =int(input('Enter a year:'))
if date_mount != 2 :
    if data_day >= 30 or data_day ==31 :
        if date_year > 0 and date_year < 10000 :
            print('This is legit date ')
        else:
            print('Is wrong date')    
    else :
        print('Is wrong date ')        
elif date_mount == 2 :
    if data_day == 28 or data_day == 29 :
        if date_year > 0 and date_year < 10000 :
            print('This is legit date ')
        else:
            print('Is wrong date')
    
    
    
    