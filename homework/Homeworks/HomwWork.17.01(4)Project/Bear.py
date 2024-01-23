from Mammal import Mammal

class Bear(Mammal):
    def __init__(self,name):
        self.name = name
        super().__init__(name)

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].
__name__)
print(mammal.name)
