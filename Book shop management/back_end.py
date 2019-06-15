import time
import tkinter as t
import sqlite3 as sq
# from front_end import *


conn=sq.connect('book_store')
curr=conn.cursor()
curr.execute("SELECT * from books")
all=curr.fetchall()

# print(all)



def add_clicked():
    def add():
        message.delete('1.0',t.END)
        try:
            row=(t_val.get(),a_val.get(),int(y_val.get()),int(I_val.get()))
            curr.execute('INSERT INTO books VALUES (?,?,?,?)',row)
            conn.commit()
            message.insert(t.END,"succesfully added")
#             time.sleep(1.5)
            popinsert.destroy()
        except:
            message.insert(t.END,"some error occured")
        
    
    popinsert=t.Tk()
    popinsert.title('Enter new details')
    
    title=t.Label(popinsert,text='Title')
    title.grid(row=0,column=0,sticky=t.W)

    year=t.Label(popinsert,text='Year')
    year.grid(row=1,column=0,sticky=t.W)
    
    t_val=t.Entry(popinsert)
    t_val.grid(row=0,column=1)
    
    y_val=t.Entry(popinsert)
    y_val.grid(row=1,column=1)
    
    author=t.Label(popinsert,text='Author')
    author.grid(row=0,column=2,sticky=t.W)
    
    ISBN=t.Label(popinsert,text='ISBN')
    ISBN.grid(row=1,column=2,sticky=t.W)
    
    a_val=t.Entry(popinsert)
    a_val.grid(row=0,column=3)
    
    I_val=t.Entry(popinsert)
    I_val.grid(row=1,column=3)
    
    final=t.Button(popinsert,text="ADD",command=add)
    final.grid(row=3,columnspan=4)
    
    message=t.Text(popinsert,width=10,height=1)
    message.grid(row=4,columnspan=4)
    popinsert.mainloop()
 