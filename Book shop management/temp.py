import time
import tkinter as t
import tkinter.messagebox as message
import sqlite3 as sq

conn=sq.connect('book_store' )
curr=conn.cursor()

curr.execute('select * from books where authors like "%murakami%"')

print(curr.fetchall())