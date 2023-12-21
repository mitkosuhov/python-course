tasks = {}
count = 1

while True:
    action1 = input('Добавяне на задача:(1) \nПреглеждане на задача:(2)\nРедактиране на задача:(3)\nИзтриване на задача:(4)\nИзход:(5)')
    if action1 == '1':
        task_name = input('Добавете задача :')
        tasks[count]= task_name
        task_text = input('Въведеи описание на задачата ')
        
        count +=1

    elif action1 == '2':
        print(tasks)   
        q1 = int(input('Коя задача искате да прегледате :'))
        print(tasks[1])




    
            