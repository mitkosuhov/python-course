tasks = [['Почистване','Почистване на общи части'],['Преместване','Преместване на стари елементи'],['Сортиране','Сортиране на нови елементи']]

while True :
    action1 = input('1)Въведи задача:\n2)Преглед на задачи:\n3)Редактиране на задача:\n4)Изтриване на задача:\nИзход:\nИзбор:...')
    if action1 == '1' :
        while True :
            q1 = input('Име на задача?')
            if q1 != 'stop':
                q2 = input('Описание на задача?')
                task = [q1,q2]
                tasks.append(task)
                q3 =input('Искате ли да въведете още задачи ,ако не (stop):')
                if q3 == 'stop':                   
                    break
                elif q3 == 'искам' or q3 == 'да':
                    continue    
                else :
                    print('Грешна команда')
                    break
            elif q1 == 'stop':
                break  
    elif action1 == '2' : 
        while True:
            for i in tasks:
                    print(i[0])
            q4 = input('Коя задача искате да прегледате ?')
            if q4 != 'stop':       
                for i in tasks :
                    if q4 in i :
                        print(i)
            elif q4 == 'stop':
                break            
                    
                
                    

