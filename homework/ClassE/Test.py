def odd(x):
    odd = 0
    no_odd = 0
    for i in x :
        if i % 2 == 0:
            odd += 1 
        elif i % 2 == 1:
            no_odd += 1 
        else:
            pass        
    return f"четните са {odd} , нечетните са  {no_odd}"


            

    


nums = [2,3,4,5,6,7,8,9,11,12,14,116,4]
print(odd(nums))

