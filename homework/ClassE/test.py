from datetime import datetime 

date_add = input("Enter a data of income in format  'DD-MM-YYYY': ")
                
try:
    date_enter = datetime.strptime(date_add, '%d-%m-%Y').date()
    
                    
except ValueError:
     print(f'Wrong format')   

print(date_enter)     