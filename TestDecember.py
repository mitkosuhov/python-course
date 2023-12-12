import os
from pathlib import Path
import random

path_to = Path.home() / 'Desktop' / 'HomeWork.12.12'

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
    if not direc.exists():
        direc.mkdir()
    
