import sqlite3

conn = sqlite3.connect('HomeWork.14.02.sqlite')

cur = conn.cursor()

cur.execute("create table Products(Name text,Price int)")
conn.commit()

products = [('Coca Cola', 50),('Pepsi', 150),('Fanta', 120),('Mineral Water', 40),('Vodka', 250),
            ('Jin', 180),('Oringe juce', 30),('Tequila', 100),('Sprait', 110),('Rum', 350)]

cur.executemany("insert into Products values (?,?)",products)
conn.commit()

print('Задача 1 / Създаване на таблица ')
cur.execute("SELECT * FROM Products")
rows = cur.fetchall()
for row in rows:
    print(row)


cur.execute("select Name, Price from Products where price > 100")
rows = cur.fetchall()

print('Задача 1.2/ Извеждане на продукти с цена над 100 лева ')
# Извеждане на резултатите в терминала 
for row in rows:
    print(row)

cur.execute("insert into Products values ('Banana juce' , 70)")    
conn.commit()

cur.execute("SELECT * FROM Products")
rows = cur.fetchall()

print('Задача 2/Добавяне на продукт ')
for row in rows:
    print(row)

cur.execute("DELETE FROM Products WHERE Price <= 70")
conn.commit()

cur.execute("SELECT * FROM Products")
rows = cur.fetchall()

print('Задача 3/Изтриване на продукт ')
for row in rows:
    print(row)

print('Задача 4/Сортирване и извеждане на продукти  ')

cur.execute("select Name , Price from Products where Price > 100 ORDER BY Price DESC")
rows = cur.fetchall()

for row in rows:
    print(row)





