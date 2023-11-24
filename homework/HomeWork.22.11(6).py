#задача 6  
num_list = []

while True :
    nums = input("Give me a number :")
    
    if nums == 'sum':
        print('Your numbers are ',num_list ,'and they sum is ', sum(num_list))
        break
    if nums != 'sum':
        nums = float(nums)
        num_list.append(nums)
