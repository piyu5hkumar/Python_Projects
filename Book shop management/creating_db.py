import sqlite3 as sq
try:
    conn=sq.connect('book_store')
    curr=conn.cursor()
    curr.execute('''
    CREATE TABLE IF NOT EXISTS BOOKS
    (
        title TEXT,
        authors TEXT,
        year INTEGER,
        isbn INTEGER PRIMARY KEY
    )
    ''')

    print('database created')
    conn.commit()
    conn.close()
except:
    print('some error occured')