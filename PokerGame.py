import random 

boi = ['Каро','Купа','Спатия','Пика']
num = ['2','3','4','5', '6','7','8','9','10','J','Q','K','A']
hand = []
i = 0
while i < 5:
    card = random.choice(boi)+random.choice(num)
    hand.append(card)
    
    i += 1

print('Your hand is ' , hand )


