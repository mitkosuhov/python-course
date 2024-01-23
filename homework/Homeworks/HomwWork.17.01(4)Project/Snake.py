from Reptile import Reptile

class Snake( Reptile):
    def __init__(self,name):
        self.name = name
        super().__init__(name)
        

lizard = Snake("Lili")
print(lizard.__class__.__bases__[0].
__name__)
print(lizard.name)