num = int(input('Enter a number: '))
# result = bo15
if num > 0 :
    print('Can be bool ')
    num = bool(num)
    result = True
    num = bool(num)
else :
    print('Can not be bool ')
if num % 3 == 0 and num % 5 == 0 :
    print(f'{num} can be dev to 3 and 5 ')
else :
    print('Can not be dev to 3 and 5 ')    
if result == True :
    num = bool(num)
    print(type(num))


