from Animal import Animal
class Dog(Animal):
    def bark(self):
        return 'barking...'
dog=Dog()
print(dog.bark())
print(dog.eating())    