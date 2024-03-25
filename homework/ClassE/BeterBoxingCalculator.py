from sqlalchemy import create_engine, Column, Integer, String, func 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import matplotlib.pyplot as plt
import numpy as np
from sqlalchemy import desc


engine = create_engine('sqlite:///BoxingMach.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)


class ScoreCard(Base):
    __tablename__ = 'ScoreCard'
    round = Column(Integer, primary_key=True)
    fighter1 = Column(String)
    fighter1_score = Column(Integer)
    fighter2_score = Column(Integer)
    fighter2 = Column(String)


Base.metadata.create_all(engine)

def add_points(x,y,s,d):
                # Добавяне на първо име
                session = Session()
                new_expense = ScoreCard(fighter1_score= x,fighter2_score =y,fighter1=s,fighter2=d)
                session.add(new_expense)
                session.commit()

def calculate_scores_sum():
    session = Session()

    # Изчисляване на сумата на числата в колоната fighter1_score
    fighter1_score_sum = session.query(func.sum(ScoreCard.fighter1_score)).scalar()

    # Изчисляване на сумата на числата в колоната fighter2_score
    fighter2_score_sum = session.query(func.sum(ScoreCard.fighter2_score)).scalar()

    session.close()

    return fighter1_score_sum, fighter2_score_sum

count = 1
fighter1 = input('Enter the name of the first fighter: ')
fighter2 = input('Enter the name of the second fighter: ')

while count <= 12 :
        print(f'Round {count} :')
        f1s = int(input(f"{fighter1} score :"))
        f2s = int(input(f"{fighter2} score :"))
        add_points(f1s,f2s,fighter1,fighter2)
        fighter1_sum, fighter2_sum = calculate_scores_sum()

        print(f"Score for {fighter1} is: {fighter1_sum}")
        print(f"Score for {fighter2} is: {fighter2_sum}")
        
        count += 1
        




