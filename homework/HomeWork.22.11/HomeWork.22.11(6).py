#задача 6  
num_list = [] # Списък в който ще поставяме въведените числа от конзолата 

while True :   # Създаваме повтарящ се цикъл който да приема чусла под формата на str .
    nums = input("Give me a number :") 
    
    if nums == 'sum': # Създаваме дума с който да прекратим цикала и да принтираме сумата от числата 
        print('Your numbers are ',num_list ,'and they sum is ', sum(num_list))
        break
    if nums != 'sum': # Проверяваме дали str. може да бъде променен в float , ако не бива нулиран 
        try:
            nums = float(nums)
            num_list.append(nums)
        except :
            nums = 0