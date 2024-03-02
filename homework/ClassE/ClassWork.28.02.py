import sqlite3
import bcrypt

conn = sqlite3.connect('ClassWork.28.02.sqlite')

cur = conn.cursor()
columns = []
types = []

table_name = input('Name of the table :')
while True :
    
    colum = input('Enter a colum :')
    columns.append(colum)
    type_of = input('Enter a type :')
    types.append(type_of)    
    question_table= input('Do you want to add more ? y/n :')
    if question_table == 'y':
        continue
    else:
        break

create_table_query = f"CREATE TABLE {table_name} (PersonID INTEGER PRIMARY KEY AUTOINCREMENT"

# Преминаваме през всички въведени колони и типове и ги добавяме към заявката
for i in range(len(columns)):
    create_table_query += f", {columns[i]} {types[i]}"

create_table_query += ")"

#Изпълнение на заявката за създаване на таблицата
cur.execute(create_table_query)
conn.commit()




while True :
    data_input = input("Enter data for all columns (separated by space): ")
    data_for_columns = data_input.split()

    if "password" in columns:
        password_index = columns.index("password")
        data_for_columns[password_index] = bcrypt.hashpw(data_for_columns[password_index].encode('utf-8'), bcrypt.gensalt())

    placeholders = ', '.join(['?'] * len(data_for_columns))
    insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"

    cur.execute(insert_query, data_for_columns)
    conn.commit()
    print("Данните бяха успешно вмъкнати в базата данни.")
    ask2 = input('Do you what to add more :')
    if ask2=='y':
        continue
    else:
        break


select_query = f"SELECT * FROM {table_name}"

# Изпълнение на заявката и вземане на резултатите
cur.execute(select_query)
rows = cur.fetchall()

# Принтиране на резултатите
for row in rows:
    print(row)


conn.close()
