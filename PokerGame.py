import random 

num = ['Каро 2','Каро 3','Каро 4','Каро 5', 'Каро 6','Каро 7','Каро 8','Каро 9','Каро 10','Каро J','Каро Q','Каро K','Каро A' ,
       'Купа 2','Купа 3','Купа 4','Купа 5', 'Купа 6','Купа 7','Купа 8','Купа 9','Купа 10','Купа J','Купа Q','Купа K','Купа A',
       'Спатия 2','Спатия 3','Спатия 4','Спатия 5', 'Спатия 6','Спатия 7','Спатия 8','Спатия 9','Спатия 10','Спатия J','Спатия Q','Спатия K','Спатия A',
       'Пика 2','Пика 3','Пика 4','Пика 5', 'Пика 6','Пика 7','Пика 8','Пика 9','Пика 10','Пика J','Пика Q','Пика K','Пика A']
hand = []
i = 0
while i < 5:
    card = random.sample(num,1)
    hand.append(card)
    i += 1

print('Your hand is ' , hand )
print(len(num))

   






