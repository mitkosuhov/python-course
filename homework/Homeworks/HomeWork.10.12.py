import os
from pathlib import Path
import random
import shutil

path_to = Path.home() / 'Desktop' / 'HomeWork.12.12'
folders = []
for x in range(100):
    while True :
        ran = str(random.randint(1,200))
        file_path = path_to / (ran +'.txt')
        if not file_path.exists():

            with open(file_path,'w') as file :
                break

for num in range(1,10):
    num = str(num)
    direc = path_to / num
    folders.append(direc)
    if not direc.exists():
        direc.mkdir()
    
for n in range (10):

    path_for_every = [file for file in path_to.iterdir() if file.is_file() and file.name.startswith(f'{str(n)}')] 

    for file in path_for_every:
    
        shutil.move(file, folders[n-1] / file.name)

         

def print_directory_structure(folder_path, indent=''):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            print(indent + '- ' + item)
        elif os.path.isdir(item_path):
            print(indent + '|+ ' + item)
            print_directory_structure(item_path, indent + '|  ')

path_to1 = os.path.join(os.path.expanduser('~'), 'Desktop', 'HomeWork.12.12')

# Генериране на файловете и папките тук...

print("Структура на файловете и папките след създаването:")
print_directory_structure(path_to1)


for folder in path_to.iterdir():
    if folder.is_dir():
        for file in folder.iterdir():
            if file.is_file():
                file.unlink()  # Изтриване на всички файлове в папката
        shutil.rmtree(folder)