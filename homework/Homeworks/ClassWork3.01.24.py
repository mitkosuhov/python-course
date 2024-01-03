tasks = [['Почистване','Почистване на общи части'],['Преместване','Преместване на стари елементи'],['Сортиране','Сортиране на нови елементи']]

def menu():
    print('1)Въвеждане на задача :\n2)Преглед на задача:\n3)Промяна на задача:\n4)Изтриване на задача:\n5)Изход:\nИзбор:')
    
def valid_input(choice):
    if choice in ['1','2','3','4','5']:
        return True
    else :
        return False
def tasks_list():
    for index,i in enumerate(tasks):
        print(index +1,i)    

while True :
    menu()
    choice=input()
    while not valid_input(choice) :
        print(f'{choice} Грешен избор!')
        break
    if choice == '1':
        while True:
            tasks_list()
            q1 = input('Име на нова задача :')
            q2 = input('Описание на нова задача :')
            new_task = q1,q2
            tasks.append(new_task)
            tasks_list()
            q3 = input('Искате ли да продължите :')
            if q3 == 'да':
                continue
            if q3 == 'не':
                break
            else :
                print('Грешен избор !!!')
                break
    elif choice == '2':
        while True :
            tasks_list()
            q3 = input('Коя задача искта да промените')
            if isinstance(q3,int) :
                print(f'Грешен избор!!! изебрете от 1 до {len(tasks)} ')
            elif not isinstance (q3,int) :
                print(tasks[q3])
               

                


