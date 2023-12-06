#Задача 5
from collections import Counter
days_num = int(input('How many days do you whant to enter:'))
my_days = []

while days_num > 0 :
    day = input(f'Enter a {days_num} day :')
    if day in ['Monday','Tuesday','Wednesday','Tursday','Friday','Saturday','Sunday']:
        my_days.append(day)
        days_num = days_num-1
    else :
        print('Invalid day ')

print(Counter(my_days))