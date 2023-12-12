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
