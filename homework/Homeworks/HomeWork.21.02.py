from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///Cars.db')

# Дефиниране на базов клас за декларативно дефиниране на таблиците
Base = declarative_base()

# Дефиниране на модела за таблицата
class Car(Base):
    __tablename__ = 'Cars'

    id = Column(Integer, primary_key=True)
    model = Column(String)
    price = Column(Integer)
    

# Създаване на таблиците в базата данни
Base.metadata.create_all(engine)

# Създаване на сесия за взаимодействие с базата данни
Session = sessionmaker(bind=engine)
session = Session()

cars =[Car(model = 'Mercedes' , price =100000),Car(model = 'BMW' , price =150000),
       Car(model = 'Opel' , price =80000),Car(model = 'Nissan' , price =49000),
       Car(model = 'Alfa Romeo' , price =60000),Car(model = 'FIAT' , price =5000),
       Car(model = 'KIA' , price =12000),Car(model = 'VW' , price =90000),
       Car(model = 'Honda' , price =13000),Car(model = 'AUDI' , price =18000)]

# Добавяне на обекти към сесията
session.add_all(cars)

# Потвърждаване на промените
session.commit()

cars = session.query(Car).all()

# Изпечатване на данните
print(f'Задача 1 ')
for car in cars:
    print(f"Model: {car.model}, Price: {car.price}")

cars = session.query(Car).filter(Car.price >= 50000).all()
print(f'Задача 1.2')
for car in cars:
    print(f"Model: {car.model}, Price: {car.price}")

# Филтриране на записите, които искаш да изтриеш
cars_to_delete = session.query(Car).filter(Car.price <= 30000).all()

# Изтриване на филтрираните записи
for car in cars_to_delete:
    session.delete(car)

session.commit()

updated_cars = session.query(Car).all()

# Изпечатване на актуализираните данни
print(f'Задача 2 ')
for car in updated_cars:
    print(f"Model: {car.model}, Price: {car.price}")

# Създаване на нов обект 
new_car = Car(model='Tesla', price=175000)

# Добавяне на новия обект към сесията
session.add(new_car)

session.commit()    

updated_cars = session.query(Car).all()


print(f'Задача 3 ')
for car in updated_cars:
    print(f"Model: {car.model}, Price: {car.price}")

cars_sort = session.query(Car).filter(Car.price >= 100000).order_by(Car.price).all()
print(f'Задача 4')
for car in cars_sort:
    print(f"Model: {car.model}, Price: {car.price}")    

# Затваряне на сесията
session.close()