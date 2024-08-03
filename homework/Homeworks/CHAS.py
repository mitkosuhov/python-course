import time
kids = {}

while True :
    menu_directory = input(f' 1)Добави дете :\n 2)Проверка на клиенти :\n 3)Изкарай дете :\n 4)Изход')
    if menu_directory == '4':
        break
    elif menu_directory == '1':
        name_of_the_kid = input(f'Как се казва детето :')
        time_of_the_kid = input(f'Въведете час на влизане : ')
        kids[name_of_the_kid] = time_of_the_kid
        continue
    elif menu_directory == '2':
        print(kids)
        continue
    elif menu_directory == '3':
        print(kids)
        exit_the_kid = input(f'Име на детево :')
        exit_time_kid = input(f'Време на напускане :')
        
