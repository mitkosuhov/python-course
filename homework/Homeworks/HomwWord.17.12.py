#Задача 1 
# num = int(input('Enter a number:'))

# for i in range(1,num+1,3):
#     print(i)

#Задача 2 

# num = int(input('Enter a number:'))

# if num > 1 :
#     for i in range(1,num+1):
#         print(num)
#         num -= 1
# else :
#     print('Wrong number')

#Задача 3 
# word = input('Enter a word:')
# for i in word :
#     print(i)

#Задача 4 
# for i in range(1,1000):
#     if i % 10 == 7:
#         print(i)

#Задача 5 
nums =[]

while True :
    num = input('Enter a number:')
    if num.isdigit():
        nums.append(int(num))
    elif num == 'end':
        break
    else:
        print('Wrong number')
        num== 0 
        
even_num = nums[1::2] 
not_even = nums[0::2]
print(f'The sum of the even numbers is {sum(not_even)}')
print(f'The sum of not even nubers is {sum(even_num)}')
if even_num == not_even:
    print('The sums are even')
else:
    print('They are not even')