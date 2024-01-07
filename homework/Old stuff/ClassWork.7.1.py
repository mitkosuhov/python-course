# x = int(input('num:'))
y = 5
c = [1,2,3,3,3,3,3,3,4,4,4,44,]
# uper_ = 0
# low_ = 0
# def sum_of(x):
#     global uper_ , low_
#     for i in x :
        
#         if i.isupper():
#              uper_ += 1
#         elif i.islower():
#              low_ +=  1
#         else:
#              pass     
#     return print(f'Uper {uper_}, Low {low_}')                
# sum_of(y)      

# sum_of = lambda x: x + 10
# print(sum_of(y))
# rev = lambda y : y[::-1]
# print(rev(c))
unic = []
def off(x):
    for i in x :
        if i not in unic:
            unic.append(i)
        else:
            pass  
    print(unic)     
print(off(c))
           