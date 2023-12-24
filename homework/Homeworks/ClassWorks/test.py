# lista = (3,6,9)
# i = list(lista)
# i[1] = 7 # разопаковаме листа 
# print(tuple(i))



# name = {1:'Blue',2:'Red',3: {1:'name',2:'age',3:{1:'Place',2:'Gas',3:'Tree'}}}
# print(name[3][3][2])


# song = "Let it be , let it be , let it be , let it be "

# print(song.replace('let it be ','dont let it be ',2))

# nums = [1,3,5,6,8,10.12]
# filter_nums = [i for i in nums if i > 4 and i % 2 == 0 ] # Филтър 
# print(filter_nums)



# #Подобрена домашна 
# str1 = 'Homeworksandotherstuffihavetoputtinthistext'
# len_str1= int((len(str1))/2)
# print(str1[0::len_str1])

# # ФизБъз задача
# for fizzbuzz in range(51):   
#     if fizzbuzz % 3 ==0 and fizzbuzz % 5 == 0 :
#         print('FIzzbuzz')
#     elif fizzbuzz % 3 ==0 :
#         print('Fizz')
#     elif fizzbuzz % 5== 0 :
#         print('Buzz')   
#     else :
#         print(fizzbuzz)    


#  # Drug primer 
#  # list_nums = []
# for nums in range(1500,2701):
#     if nums % 5 == 0 and nums % 7 == 0 :
#         nums=str(nums)
#         list_nums.append(nums)

# print(list_nums)
# print('/'.join(list_nums))
       
tasks = [['Почистване', 'Почистване на общи части'], ['Преместване', 'Преместване на стари елементи'], ['Сортиране', 'Сортиране на нови елементи']]

q1 = input('Задача: ')

for index, task in enumerate(tasks):
    if q1 in task:
        print(f'Задачата {q1} е на позиция {index}')
        print(task)  # Ако искаш да изведеш самата задача
