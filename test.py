lista = (3,6,9)
i = list(lista)
i[1] = 7 # разопаковаме листа 
print(tuple(i))



name = {1:'Blue',2:'Red',3: {1:'name',2:'age',3:{1:'Place',2:'Gas',3:'Tree'}}}
print(name[3][3][2])


song = "Let it be , let it be , let it be , let it be "

print(song.replace('let it be ','dont let it be ',2))

nums = [1,3,5,6,8,10.12]
filter_nums = [i for i in nums if i > 4 and i % 2 == 0 ] # Филтър 
print(filter_nums)



#Подобрена домашна 
str1 = 'Homeworksandotherstuffihavetoputtinthistext'
len_str1= int((len(str1))/2)
print(str1[0::len_str1])