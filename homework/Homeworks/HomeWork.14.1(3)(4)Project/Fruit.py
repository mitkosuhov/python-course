from Food import Food
class Fruit(Food):
    def __init__(self,name,exp_date):
        super().__init__(exp_date)
        self.name = name

        