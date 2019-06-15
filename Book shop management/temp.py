import sqlite3 as sq
import psycopg2 as psq

conn1=psq.connect(database='book_store',user='piyu',password='1234',host='localhost')
curr1=conn1.cursor()
curr1.execute("SELECT * from books")
all=curr1.fetchall()



curr2.executemany('''INSERT INTO books VALUES (?,?,?,?);''',all)
conn2.commit()