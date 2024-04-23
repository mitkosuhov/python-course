nums = [2,4,6,4,3,1,5,7,9,6,4,2,1,1,8,0,5,4,3]
num1 = 3


def del_chek(x,y):
    ansers = []
    for i in x :
        if i%y == 0  :
            ansers.append(i) 
    return ansers        
        
               



print(del_chek(nums,num1))


