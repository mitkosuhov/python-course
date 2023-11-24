#задача 1 
side1 = float(input('Въведете една страна на правоъгълника (см.):'))
side2 = float(input('Въведете другата страна на правоъгълника (см.):'))
face = side1 * side2
if side1 != side2 :
    if side1 > side2:
        print('Лицето на правоъгълника е с площ ',face,'кв.см.')
        print('      ',side1,'     ')
        print(' ____________________')
        print('|                    |')
        print('|        ',face,'     |',side2)
        print('|____________________|')
        print('Лицето на правоъгълника е с площ ',face,'кв.см.')
    if side1 < side2 :
        print('Лицето на правоъгълника е с площ ',face,'кв.см.')
        print('      ',side2,'     ')
        print(' ____________________')
        print('|                    |')
        print('|        ',face,'     |',side1)
        print('|____________________|')
        print('Лицето на правоъгълника е с площ ',face,'кв.см.')
        
    
else :
    print('Имате квадрат с лице ',face,'кв.см.')
    print(' ',side1,'')
    print(' _________')
    print('|         |')
    print('|',face,'  |',side2)
    print('|_________|')

#задача 2 и 3


name  = input('Hi , whats your name ?')
last_name = input('And you last name ?')
age = input('How old are you ')
home_town =input('And where are you from ?')
print ('Ýour name is '+ name +" "+  last_name + ' you are ' + age + ' years old , and you came from '+ home_town)
 