# from datetime import datetime

# print (datetime.now())

# year = datetime.now().year
# month =datetime.now().month
# day = datetime.now().day
# hour = datetime.now().hour
# minute = datetime.now().minute
# second = datetime.now().second

# print(f'{year}')
# print(month)
# print(day)
# print(hour)
# print(minute)
# print(second)

# format = datetime.now().strftime('-%m-%d-%Y')
# print(format)

# date_st = datetime(2025, 1, 1, 12, 0, 0)
# print(date_st)

# def date_chek(x):
#     if x < datetime.now():
#         print('Минало')
#     else:
#         print('Бъдеще ')

# date_chek(date_st)


# import os 

# print(os.getcwd())
# print(f'Curent directory is  {os.getcwd()}')

# # directory_path = r'C:\Users\Mitko\Desktop\python2023\homework\ClassE'
# # files = os.listdir(directory_path)
# # for file in files:
# #     print(file)

# # path = r'C:\Users\Mitko\Desktop\python2023\homework\ClassE\test.py'  
# # new_file_name = 'new_test.py'
# # new_file_path = r'C:\Users\Mitko\Desktop\python2023\homework\ClassE'
# # new_path = os.path.join(new_file_path, new_file_name)
# # os.rename(path, new_path)

# # directory_path = r'C:\Users\Mitko\Desktop\python2023\homework\ClassE'
# # files = os.listdir(directory_path)
# # for file in files:
# #     print(file)


# # path = r'C:\Users\Mitko\Desktop\python2023\homework\ClassE\new_tst.py'

# # if os.path.exists(path):
# #     print(f'{path} съществува.')
# # else:
# #     print(f'{path} не съществува.')


# # new_file_path = r'C:\Users\Mitko\Desktop\python2023\homework\ClassE\new_file.py'

# # with open(new_file_path, 'w') as new_file: 
# #     pass

# file_to_delete = r'C:\Users\Mitko\Desktop\python2023\homework\ClassE\new_file.py'

# os.remove(file_to_delete)

# import sys
# print(sys.version)

# print(sys.platform)

# try:
#     import sys
#     print("Is Ready")
# except ImportError:
#     print("Is not Ready ")

# print(sys.path)

# import pandas

# file = r'C:\Users\Mitko\Desktop\HomeWork.12.12\New.csv'

# print(pandas.read_csv(file))
# data = pandas.read_csv(file)
# print(data.info())
# print(data.describe())

import numpy as np

lista = [0,1,2,3,4]
ar_1 = np.array(lista)

lista2 = [[0,1,2,3,4],[5,6,7,8,9]]
ar_2 = np.array(lista2)

# print(ar_1)
# print(ar_2)
# result = ar_1 + ar_2
# print(result)
print(ar_1[2])

print(np.mean(ar_1))
print(np.max(ar_1))


