# import time
# def Decorator(function):
#     def wrapper(*args,**kwargs):

#         start_time = time.time()
#         result = function(*args,**kwargs)
#         end_time = time.time()
#         time_result = end_time - start_time

#         print(f'{time_result}')
#         print(function.__name__)

#         return result 
    
#     return wrapper
# @Decorator
# def func(x):
#     count = 1
#     for i in x :
#         count *= i 
#     return print(count)
# lista = [1,2,3,4,5,6,7,89,4,5,5,5,10000,251,446]
# func(lista)

# class Tempcalculator:
#     faren = 'F'
#     celsi = 'C'

#     @staticmethod
#     def Celsi_to_Faren(x):
#         return 9*x/5 + 32

#     @staticmethod
#     def Faren_to_Celsix(x):
#         return x *9/5 + 32
    
#     @staticmethod
#     def Format( x , y ):
#         if y == Tempcalculator.faren :
#              return (f'{x} F')           
#         if y == Tempcalculator.celsi:                         
#              return (f'{x} C')
    
# print(Tempcalculator.Format(Tempcalculator.Faren_to_Celsix(35),Tempcalculator.faren))
# print(Tempcalculator.Format(Tempcalculator.Celsi_to_Faren(50),Tempcalculator.celsi))

# class TeamMember :
#     def __init__(self,name,userID):
#         self.name = name
#         self.userIT = userID
        
# class Worker :
#     def __init__(self,pay,jobtitle):
#         self.pay = pay
#         self.jobtitle = jobtitle
        
# class TeamLeader(TeamMember,Worker):
#     def __init__(self, name, userID,pay,jobtitle,ex):
#         TeamMember.__init__(self,name, userID)
#         Worker.__init__(self,pay,jobtitle)     
#         self.ex = ex
#         print(f'The name is {name}, hes ID is {userID} he gets {pay} at {jobtitle} whit expi of {ex} years')


# Mitko = TeamLeader('Jake',15461,250000,'tech',5)


# def sqrt(x):
#     if x < 0 :
#         raise ValueError('Its negativ numnber ')
#     else:
#         return x**x

# try:
#     sqrt(-4)
# except ValueError as a :
#     print(f'An error , {a}')

    
