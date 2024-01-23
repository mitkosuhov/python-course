from Animal import Animal

class Mammal(Animal):
    def __init__(self,name):
        self.name = name
        super().__init__(name)


