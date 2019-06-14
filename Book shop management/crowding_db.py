import psycopg2 as sq

conn=sq.connect(database='book_store',user='piyu',password='1234',host='localhost')
cur=conn.cursor()

some_books=[
            ('harry potter','j.k rowling',2000,45367),
            ('norwegian wood','murakami',1996,50152),
            ('kafka on the beach','murakami',2000,51565),
            ('fault in our star','john green',2001,78942),
            ('your name','makoto shinkai',2005,69542)
            ]

cur.executemany('''INSERT INTO books VALUES (%s,%s,%s,%s);''',some_books)
conn.commit()
print('done')
