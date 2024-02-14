import sqlite3

conn = sqlite3.connect('test.sqlite')

cur = conn.cursor()

cur.execute("create table test_table(ID int , Name text)")

conn.commit()
cur.execute("incerte into test_table values (1 , 'Mitko')")




