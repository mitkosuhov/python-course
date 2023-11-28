#задача 4
import datetime

today = datetime.date.today()
year_one = today + datetime.timedelta(days=365)
print(today)
print(year_one)

#задача 5
num1 = int(input('Give me one number '))
num2 = int(input('Give me a second number '))
num3 = int(input('And a thurd '))
sum_of = [num1,num2,num3]
print('The sum of three is :',sum(sum_of))
print('Bigest number is :',max(sum_of))
print('Smallest number is :',min(sum_of))