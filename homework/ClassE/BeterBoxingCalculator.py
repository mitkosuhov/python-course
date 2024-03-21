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

fighter1 = input('Enter the name of first fighter :')
fighter2 = input('Enter the name of second fighter :')

class ScoreCard(Base):
    __tablename__ = 'Score Card'
    round = Column(Integer, primary_key=True)
    fighter1 = Column(String)
    fighter1_score = Column(Integer)
    fighter2_score = Column(Integer)
    fighter2 = Column(String)


Base.metadata.create_all(engine)

def add_names(x,y):
                # Добавяне на първо име
                session = Session()
                new_expense = ScoreCard(fighter1= x,fighter2 =y)
                session.add(new_expense)
                session.commit()








