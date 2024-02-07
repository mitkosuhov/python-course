def num(x):
    if x == 0 :
        return 0
    elif x==1 :
        return 1
    else:
        return num(x-1) + num(x-2)

print(num(19))    