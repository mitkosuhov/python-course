tasks = [['Почистване','Почистване на общи части'],['Преместване','Преместване на стари елементи'],['Сортиране','Сортиране на нови елементи']]

while True :
    action1 = input('1)Въведи задача:\n2)Преглед на задачи:\n3)Редактиране на задача:\n4)Изтриване на задача:\n5)Изход:\nИзбор:...')
    
    if action1 == '1' :
        while True :
            q1 = input('Име на задача?')
            if q1 != 'стоп':
                q2 = input('Описание на задача?')
                task = [q1,q2]
                tasks.append(task)
                q3 =input('Искате ли да въведете още задачи (да , искам) ,ако не (стоп):')
                if q3 == 'стоп':                   
                    break
                elif q3 == 'искам' or q3 == 'да':
                    continue    
                else :
                    print('Грешна команда')
                    break
            elif q1 == 'стоп':
                break  
            else:
                 print('Грешка !!!')
    elif action1 == '2' : 
        while True:
             for i in enumerate(tasks,start=1) :
                  print(i)
             q4 = input('Как изкате да прегледате (индекс) , стоп за изход: ')     
             if q4 == 'стоп':
                  break
             elif q4.isdigit():
                  q4=int(q4) 
                  q4 -= 1
                  if q4 <= (len(tasks)-1):
                         print(tasks[q4])
                         q5 = input('Желаете ли да продължите (да) ,(стоп0 за изход :')
                         if q5 == 'да':
                              continue
                         elif q5== 'стоп':
                              break
                         else:
                              print('Грешка !!!')
                  else :
                       print('Грешка !!!')  
                       continue        
             else:   
                  print('Грешка !!!')  
                            
                                           
    elif action1 == '3':
         while True :
              for i in enumerate(tasks,start=1) :
                   print(i)                     
              q7 =input('Коя задача искате да промените , за изход напишете (стоп):')
              if q7 == 'стоп':
                   break
              elif q7.isdigit():
                   q7=int(q7) 
                   q7 -= 1
                   if q7 <= (len(tasks)-1):
                         print(tasks[q7])
                         q8 = input('Избери 0 за промяна на заглавието , 1 за промяна на описанието 2 за промяна на позицията на задачите:')
                         if q8 == '0' :
                              q9 = input('Изберете ново заглавие :')
                              tasks[q7][0] = q9
                              print(tasks[q7])
                         elif q8 == '1':
                              q10 = input('Изберете ново описание :')
                              tasks[q7][1] = q10
                              print(tasks[q7])
                         elif q8 == '2':
                              q10 = int(input(f'С коя задача искате да смените позията на {tasks[q7]} '))
                              q10 -= 1
                              if q10 <= (len(tasks)-1):
                              
                                   tasks[q7],tasks[q10] = tasks[q10], tasks[q7]
                              else :
                                   print('Грешен избор !!!')   
                         else :
                              print('Грешен избор !!!')  
                                                           
                   else :
                              print('Грешн избор !!!')
    elif action1 == '4':
         while True:
               for i in enumerate(tasks,start=1) :
                    print(i)   
               q15 = input('По име или индекс искате да изтриете задачата (1 за индекс 2 за име ) , стоп за изход :')     
               if q15 == '1':
                q11 = input('Коя задача искате да изтриете/ за изход (стоп) :')
                if q11 == 'стоп':
                    break
                elif q11.isdigit():                   
                    q11 = int(q11) 
                    q11 -= 1  
                    if q11 <= ((len(tasks))-1) :
                         tasks.pop(q11)       
                    
                    else :
                         print('Грешен избор !!!')   
                else :
                    print('Грешен избор !!!')          

                for i in tasks :
                        print(i)    
                q12 = input('Желаете ли да продалжите (да) за изход (стоп)')     
                if q12 == 'да':
                        continue
                elif q12 == 'стоп':
                        break
                else:
                        print('Грешен избор')   
               elif q15 == 'стоп':
                    break    
               elif q15 == '2':
                    for i in tasks:
                         print(i[0])       
                    q16 = input('Коя задача искате да изтриете :') 
                    found = False
                    for inner_list in tasks:

                            if q16 in inner_list:
                                 
                                tasks.remove(inner_list)
                                found = True
                                break
                            if not found:
                             print('Името не е намерено в списъка.')  
                             break                           
               else:
                    print('Грешен избор !!!')          

    elif action1 == '5':
         break
    else:
         print('Грешен избор !!!')