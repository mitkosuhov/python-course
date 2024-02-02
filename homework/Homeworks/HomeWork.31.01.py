# Задача 1 

# def fibo(x):
#     if x <= 1 :
#         return x
#     else:
#         return fibo(x-1)+fibo(x-2)

# print(fibo(3))    

# Задача 2 
# def num_sum(x):
#     if x <= 0 :
#         return x
#     else :
#         return x + num_sum(x-1)
 
# print(num_sum(4))

# Задача 3

def revers(x):
    return revers(x[::-1])

word = 'mitko'
print(revers(word))


# Задача 4 
# def palidrome_chek(x):
#     if len(x) > 1 :
#         if x[0] == x[-1]:
#               return palidrome_chek(x[1:-1])              
#         else:
#             return  'Is  not a  palidron '
#     else:
#          return 'Is palidrome'    
        
    
# print(palidrome_chek('12344321'))
