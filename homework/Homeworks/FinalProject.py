from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime , func
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

def add_expense(x,y):
                # Добавяне на разход
                session = Session()
                new_expense = Expense(amount=x , description=y)
                session.add(new_expense)
                session.commit()
def add_income(x,y):
            # Добавяне на приход
                session = Session()
                new_income = Income(amount=x, source=y)
                session.add(new_income)
                session.commit()
def show_expense():
            # Преглед на всички разходи
                session = Session()
                expenses = session.query(Expense).all()
                for expense in expenses:
                    print(f"Expense: {expense.description}, Amount: {expense.amount}, Date: {expense.date}")
def show_income():
            # Преглед на всички приходи
                session = Session()
                incomes = session.query(Income).all()
                for income in incomes:
                    print(f"Income: {income.source}, Amount: {income.amount}, Date: {income.date}")
def balance():
            session = Session()
            total_income = session.query(func.sum(Income.amount)).scalar() or 0
            total_expense = session.query(func.sum(Expense.amount)).scalar() or 0
            balance = total_income - total_expense
            print(f"Balance: {balance}")
            session.commit()

if __name__ == "__main__":
    while True :
        menu_direction = input('Menu : \n 1)Check ballans \n 2)add income \n 3)add expense')
        if menu_direction == '1':
                 balance()
        elif menu_direction =='2':
                amount_add = input('Enter amount of income:')  
                source_add = input('Enter a source of income :') 
                add_income(amount_add,source_add)
        elif menu_direction =='3':
                amount_add = input('Enter amount of income:')  
                source_add = input('Enter a source of income :') 
                add_expense(amount_add,source_add)        

        
            
            
        