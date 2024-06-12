numbers = [1,2,3,4,5,6,7]
number = 10 

def chek_number(x,y):
    x_len = len(x)
    for i in x :
        for j in range(x_len+1):
            if i+j==y:
                print(i,j)
            else:
                continue    
chek_number(numbers,number)            

