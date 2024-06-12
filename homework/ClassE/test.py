numbers  = [1,3,2,5,4,8,7,9,12,1,3,5,7,11,14,9,8,8]



def buble(x):
    for i in x :
        if x[i]>x[i+1]:
            x[i] , x[i+1] = x[i+1] , x[i]
        else :
            continue    
    return x 

print(buble(numbers))