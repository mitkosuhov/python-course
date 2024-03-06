from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime , func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import matplotlib.pyplot as plt

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

def add_expense(x,y,z):
                # Добавяне на разход
                session = Session()
                new_expense = Expense(amount=x , description=y , date =z)
                session.add(new_expense)
                session.commit()
def add_income(x,y,z):
            # Добавяне на приход
                session = Session()
                new_income = Income(amount=x, source=y , date =z)
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
def visualize_income_expense():
    session = Session()
    incomes = session.query(Income.date, func.sum(Income.amount)).group_by(Income.date).all()
    expenses = session.query(Expense.date, func.sum(Expense.amount)).group_by(Expense.date).all()

    income_dates, income_amounts = zip(*incomes)
    expense_dates, expense_amounts = zip(*expenses)

    plt.figure(figsize=(10, 5))

    # Приходи
    plt.subplot(1, 2, 1)
    plt.bar(income_dates, income_amounts, color='blue')
    plt.title('Приходи по дата')
    plt.xlabel('Дата')
    plt.ylabel('Сума')

    # Разходи
    plt.subplot(1, 2, 2)
    plt.bar(expense_dates, expense_amounts, color='red')
    plt.title('Разходи по дата')
    plt.xlabel('Дата')
    plt.ylabel('Сума')

    plt.tight_layout()
    plt.show()
def find_expense_count_daily(x):
    session = Session()
    total_income = session.query(func.sum(Income.amount)).scalar() or 0
    total_expense = session.query(func.sum(Expense.amount)).scalar() or 0
    balance = total_income - total_expense
    days_left = balance // x
    print(f"Вашия биджет {x} ще стигне за {days_left} дена")
    session.commit()



if __name__ == "__main__":
    while True :
        menu_direction = input('Menu : \n 1)Check ballans \n 2)Add income \n 3)Add expense \n 4)Graphics of your wallet \n 5)Calculate \n 9)Exit')
        if menu_direction == '1':
                 balance()
        elif menu_direction =='2':
                amount_add = float(input('Enter amount of income:'))
                source_add = input('Enter a source of income :') 
                date_add = input("Въведете дата във формат 'YYYY-MM-DD': ")
                date = datetime.strptime(date_add, '%Y-%m-%d')    
                if isinstance(amount_add, float) and isinstance(source_add, str) :
                        add_income(amount_add,source_add,date)
                else : 
                            print('Error!!!')    
        elif menu_direction =='3':
                amount_add = float(input('Enter amount of income:')) 
                source_add = input('Enter a source of income :') 
                date_add = input("Въведете дата във формат 'YYYY-MM-DD': ")
                date = datetime.strptime(date_add, '%Y-%m-%d') 
                if isinstance(amount_add, float) and isinstance(source_add, str):
                    add_expense(amount_add,source_add,date)        
                else :
                        print('Error!!!')
        elif menu_direction == '4':
                visualize_income_expense()
        elif menu_direction =='5':
                daily_expence = float(input('Add daily expence'))
                find_expense_count_daily(daily_expence)


        elif menu_direction == '9':
                break        
                
        
            
            
        