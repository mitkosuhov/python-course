# def step(x,y):
#     return x**y
    
# num1 = int(input('num1:'))
# num2 = int(input('num2:'))
# print(step(num1,num2))

def chet(x):
    chetni = []
    for i in x :
        if i % 2 ==0 :
            chetni.append(i)
    return chetni        

nums = [1,2,33,1231,323,23,32,42,12,54,76,637,444,97600,5677,122,3345,880]            
print(chet(nums))