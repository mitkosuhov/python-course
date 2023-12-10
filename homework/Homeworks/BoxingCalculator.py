name_1 = input('Name of the first boxer :')
name_2 = input('Name of the second boxer :')
score_1 = []
score_2 = []
rounds = 13
boxer1 = 0
boxer2 = 0
for x in range (1,rounds) :
    print(f'{x} round :')
    score = input('Who wont the round ?')
    if score == '1' :
        boxer1 = boxer1 + 10 
        boxer2 = boxer2 + 9
        score_1.append(10)
        score_2.append(9)
    elif score == '1kd' :
        kd_count = int(input('How muck kockdowns ? '))
        boxer1 = boxer1 + 10
        boxer2 = boxer2 + (9-kd_count)
        score_1.append(10)
        score_2.append(9-kd_count)
    elif score == '2kd':
        kd_count2 = int(input('How muck kockdowns ? '))
        boxer2 = boxer2 + 10
        boxer1 = boxer1 + (9-kd_count2)
        score_2.append(10)
        score_1.append(9-kd_count2)
    else :
        boxer2 = boxer2 +10
        boxer1 = boxer1 +9
        score_2.append(10)
        score_1.append(9)
    print(f'{name_1}:{boxer1}point / {name_2}:{boxer2}point')    
print(score_1)
print(score_2)