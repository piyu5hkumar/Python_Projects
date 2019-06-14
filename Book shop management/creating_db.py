import psycopg2 as sq
try:
    conn= sq.connect(database='book_store',user='piyu',password='1234',host='localhost')
    cur=conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS BOOKS
    (
        title VARCHAR,
        authors VARCHAR,
        year INTEGER,
        isbn INTEGER PRIMARY KEY
    )
    ''')
    print('database created')
    conn.commit()
    conn.close()
except:
    print('some error occured')