# # Задача 1 
# num = float(input('Enter a number betwen -100 and 100 : '))

# if (num >= -100 and num < 0 ) or (num <= 100 and num >0):
#     print(f'{num} Yes')
# else :
#     print(f'{num} No')    
# # Задача 2 
# year = int(input('Enter a year :'))

# if year % 4 ==0 or year % 100 == 0 :
#     print(f'{year} е високосна година')
# else :
#     print(f'{year} не е високосна година ')       
# Задача 3 
# hour = int(input('Enter a houre for visit : '))
# day = input('Enter a day of the week ').lower()
# Work_hours = [x for x in range(10,19)]  
# work_days = ['monday','thuesday','wednesday','thursday','friday','saturday']

# if hour in Work_hours and day in work_days :
#     print(f'On{ day} at {hour}a clock the shop is OPEN')
# else :
#     print(f'On {day} at {hour}a clock the shop is CLOSE')
#Задача 4 
# temp = float(input('Enter a temperatur in C:'))

# if temp < 0 :
#     print('Its COOLD')
# elif temp >= 0 and temp <=25 :
#     print('Its WARM')
# else :
#     print('Is HOT')        
       
 #Задача 5 
sum = float(input('What aount of mony do you want to send :'))
country = input('Enter a country for delivery :').lower()
eu = ["албания","андора","армения","австрия","азербайджан","беларус","белгия","босна и херцеговина","българия","хърватия","кипър","чехия","дания","естония","финландия","франция","грузия","германия","гърция","унгария","исландия","ирландия","италия","казахстан","косово","латвия","литва","лихтенщайн","люксембург","македония (северна)","малта","молдова","монако","черна гора","нидерландия","норвегия","полша","португалия","румъния","русия","сан марино","сърбия","словакия","словения","испания","швеция","швейцария","турция"
      ,"украйна","великобритания","ватикана","косово"]

match country :
    case 'българия':
        print(f'You whant to send {sum} the tax for that will be {sum*0.02}')
    case c if c in eu :
        print(f'You whant to send {sum} the tax for that will be {sum*0.05}')    
    case _:
        print(f'You whant to send {sum} the tax for that will be {sum*0.1}')
   
        