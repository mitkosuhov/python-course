lista = (3,6,9)
i = list(lista)
i[1] = 7 # разопаковаме листа 
print(tuple(i))



name = {1:'Blue',2:'Red',3: {1:'name',2:'age',3:{1:'Place',2:'Gas',3:'Tree'}}}
print(name[3][3][2])


song = "Let it be , let it be , let it be , let it be "

print(song.replace('let it be ','dont let it be ',2))