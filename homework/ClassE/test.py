Sep = 30 
Oct = 31
Nov = 30 
Dec = 31
work = 0


for i in range(Sep):
    if work <= 1:
        print(f'{i+1} работен')  
        work +=1 
    elif work > 1:
        print(f'{i+1} почивен')
        work -= 1       