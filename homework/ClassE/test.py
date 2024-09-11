n = 5

for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for h in range(n-i):
        print('*',end='')  
    for z in range(n-i):
        print('*',end='')
    print()