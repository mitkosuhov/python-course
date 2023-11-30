days = int(input('How much days do you want to enter ?'))
days_add =[]
mon_count = days_add.count('Monday')
while days > 0 :
    days_enter = input(f'Enter {days} day of the week :')

    if days_enter in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        days_add.append(days_enter)
        days = days - 1
    else :
        print('Invalid day ')

print(days_add)
