class Fruit():
    def __init__(self,tipe,color,price,count):
        self.tipe = tipe
        self.color = color
        self.price = price
        self.count = count
        self.total = self.price *self.count

    def Eat(self):
        print('Fruit is eaten ')

    def Over(self):
        print('Fruit is Over ')


          