nums = 7000000000


def coltdown(x):
    counter = 0 
    while x > 1 :
        x = x//2
        print(f'Run is {counter} : {x}')
        counter += 1

print(coltdown(nums))
