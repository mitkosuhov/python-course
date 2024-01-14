class Car():
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def display_info(self):
        print(self.brand)
        print(self.model)
        print(self.year)
        print(self.mileage)

class Electric_Car(Car):
    def __init__(self,brand, model, year, mileage,battery_capacity):
        super().__init__(brand, model, year, mileage)
        self.battery_capacity = battery_capacity
    def display_info(self):
        super().display_info()
        print(self.battery_capacity)
    


car1 = Electric_Car('Tesla','Noa',2020,15000,5.45)

car1.display_info()
