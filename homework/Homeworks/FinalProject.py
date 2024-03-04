from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Създаване на връзка към базата данни SQLite
engine = create_engine('sqlite:///finance.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Дефиниране на модел за разходи
class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    date = Column(DateTime, default=datetime.now)
    description = Column(String)

# Дефиниране на модел за приходи
class Income(Base):
    __tablename__ = 'incomes'
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    date = Column(DateTime, default=datetime.now)
    source = Column(String)

# Създаване на таблиците в базата данни
Base.metadata.create_all(engine)


while True :
    menu_direction = input('Menu : \n 1)Check ballans \n 2)add income \n 3)add expense')
    # Примери за използване на моделите
    if __name__ == "__main__":
        def add_expense(x,y):
            # Добавяне на разход
            session = Session()
            new_expense = Expense(amount=x , description=y)
            session.add(new_expense)
            session.commit()
        
        # Добавяне на приход
        new_income = Income(amount=500, source='Salary')
        session.add(new_income)
        session.commit()
        
        # Преглед на всички разходи
        expenses = session.query(Expense).all()
        for expense in expenses:
            print(f"Expense: {expense.description}, Amount: {expense.amount}, Date: {expense.date}")
        
        # Преглед на всички приходи
        incomes = session.query(Income).all()
        for income in incomes:
            print(f"Income: {income.source}, Amount: {income.amount}, Date: {income.date}")