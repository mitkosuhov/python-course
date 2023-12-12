import os
from pathlib import Path

desck_top_way = Path.home() / 'Desktop' / 'HomeWork.12.12'/ 'new' 

# Проверка и създаване на папката
if not desck_top_way.exists():
    desck_top_way.mkdir()
    print(f'New directory is created ')
else:
    print(f'This name all ready exist ')
file_path = desck_top_way / 'my_file2.txt'    
with open(file_path,'w') as file :
    pass
