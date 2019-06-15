import time
import tkinter as t
import sqlite3 as sq

conn=sq.connect('book_store')
curr=conn.cursor()

# print(all)
def fetch_db():
    curr.execute("SELECT * from books")
    all=curr.fetchall()
    return all


def add_clicked():
    def insert_data():
        message.delete('1.0',t.END)
        try:
            row=(t_val.get(),a_val.get(),int(y_val.get()),int(I_val.get()))
            curr.execute('INSERT INTO books VALUES (?,?,?,?)',row)
            conn.commit()
            message.insert(t.END,"succesfully added")
#             time.sleep(1.5)
            popinsert.destroy()
        except:
            message.grid(row=4,columnspan=4)
            message.configure(bg='red')
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
    
    final=t.Button(popinsert,text="ADD",command=insert_data)
    final.grid(row=3,columnspan=4)
    
    message=t.Text(popinsert,width=10,height=1)
    popinsert.mainloop()
 

def update_data(selected):
    def update_db():
        try:
            new_vals=(t_val.get(),a_val.get(),int(y_val.get()),int(i_val.get()),old_isbn)
            curr.execute('''UPDATE books
                    SET title = ?,
                    authors = ?,
                    year = ?,
                    isbn = ?
                    WHERE isbn = ?
                ''',new_vals)
            pop_update.destroy()
        except:
            message.grid(row=3,columnspan=4)
            message.configure(bg='red')
            message.delete('1.0',t.END)
            message.insert('end','UPDATE ERROR')
        
    old_isbn=selected[3]
    
    pop_update=t.Tk()
    pop_update.title('Edit your data')
    print('here')
    title=t.Label(pop_update,text='TITLE')
    title.grid(row = 0,column=0)
    
    author=t.Label(pop_update,text='AUTHOR')
    author.grid(row=0,column=1)
    
    year=t.Label(pop_update,text='YEAR')
    year.grid(row=0,column=2)
    
    isbn=t.Label(pop_update,text='ISBN')
    isbn.grid(row=0,column=3)
    
    t_val=t.Entry(pop_update)
    t_val.insert(t.END, selected[0])
    t_val.grid(row=1,column=0)
    
    
    a_val=t.Entry(pop_update)
    a_val.insert(t.END, selected[1])
    a_val.grid(row=1,column=1)
    
    y_val=t.Entry(pop_update)
    y_val.insert(t.END, selected[2])
    y_val.grid(row=1,column=2)
    
    i_val=t.Entry(pop_update)
    i_val.insert(t.END, selected[3])
    i_val.grid(row=1,column=3)
    
    update_val=t.Button(pop_update,text='UPDATE',command=update_db)
    update_val.grid(row=2,columnspan=4)
    
    message=t.Text(pop_update,width=15,height=1)
    
    
    pop_update.mainloop()
    conn.commit()


def delete_data(isbn):
    conn.execute('DELETE FROM books WHERE ISBN = ?',isbn)
    conn.commit()