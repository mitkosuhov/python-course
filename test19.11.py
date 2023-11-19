import random 

boi = ['Каро ','Купа','Спатия','Пика']
num = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

i = 0
while i < 5:
    print(random.choice(boi)+random.choice(num))
    i += 1


