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

cars = session.query(Car).filter(Car.price >= 50000 ).all()
print(f'Задача 1.2')
for car in cars:
    print(f"Model: {car.model}, Price: {car.price}")


# Затваряне на сесията
session.close()