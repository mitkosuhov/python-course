# Задача 1
# class Person():
#     def __init__(self,name,age):
#         self.__name = name 
#         self.__age = age

#     def get_name(self):
#         print(self.__name)    
#     def get_age(self):
#         print(self.__age)    

# persone1 = Person('Иван Иванов',28)
# persone1.get_name()
# persone1.get_age()

# Задача 2 
# class Mammal():
#     def __init__(self,name,type,sound):
#         self.name = name
#         self.type = type
#         self.sound = sound
#         self.kingdom = 'Animals'

#     def make_sound(self):
#         print(f'{self.name} make the sound {self.sound}')

#     def kingdomm(self):
#         print(self.kingdom)    

#     def info(self):
#         print(f'{self.name} is {self.type} type of animals ')   

# cat = Mammal('Cat','Home ','Meow')
# cat.make_sound()
# cat.kingdomm()
# cat.info()

# Задача 5

# class Vehicle():
#     def __init__(self,mileage,max_speed=150,):
#         self.max_speed = max_speed
#         self.mileage = mileage
#         self.gadgets =[]

#     def app_gadgets(self,a):
#         self.gadgets.append(a)    

# car1=Vehicle(20)
# car1.app_gadgets('any')
# print(car1.gadgets)
# print(car1.max_speed)
# print(car1.mileage)

# Задача 6

class Circle():
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def get_area(self):
        return self.pi*(self.radius**2)
    def get_circumference(self):
        return (self.pi*2)*self.radius
    def ger_radius(self,r):
        self.radius = r
fig=Circle(10)
fig.ger_radius(10)
print(fig.get_area())
print(fig.get_circumference())
        