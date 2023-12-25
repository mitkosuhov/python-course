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
                q5 =input('Искате ли да прегледате още задачи ,ако не (stop):')
                if q5 == 'stop':                   
                        break
                elif q5 == 'искам' or q5 == 'да':
                        continue    
                else :
                        print('Грешна команда')
                        break    
            elif q4 == 'stop':
                break            
    elif action1 == '3':
         while True :
              for i in enumerate(tasks) :
                   print(i)                     
              q7 =int(input('Коя задача искате да промените :')) 
              if q7 <= len(tasks):
                   print(tasks[q7])
                   q8 = input('Избери 0 за промяна на заглавието и 1 за промяна на задачата :')
                   if q8 == '0' :
                        q9 = input('Изберете ново заглавие :')
                        tasks[q7][0] = q9
                        print(tasks[q7])
                   elif q8 == '1':
                        q10 = input('Изберете ново описание :')
                        tasks[q7][1] = q10
                        print(tasks[q7])
                   else :
                        print('Грешен избор !!!')  
              else :
                   print('Греен избор !!!')
                               


                    
                
         
                
                   
                
                    

