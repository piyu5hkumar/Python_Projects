from back_end import *

curr.execute("SELECT * from books")
all=curr.fetchall()


win = t.Tk()  

def view_clicked(event ): 
    all=fetch_db()
    all_books.delete('0','end')
    for b in all:
        b=(','.join(map(lambda i:str(i),b))).title()
        all_books.insert(t.END,b)


def selected(event):
    a=all_books.get(t.ACTIVE)
    t_val.delete('1.0',t.END)
    y_val.delete('1.0',t.END)
    a_val.delete('1.0',t.END)
    I_val.delete('1.0',t.END)
    a=a.split(',')
    t_val.insert(t.END,a[0])
    a_val.insert(t.END,a[1])
    y_val.insert(t.END,a[2])
    I_val.insert(t.END,a[3])


def update_clicked():
    selected = all_books.get(t.ACTIVE)
    if(len(selected)>0):
        row_to_update=selected.split(',')
        update_data(row_to_update)  

def delete_clicked():
    isbn_to_del=(None,)
    selected = all_books.get(t.ACTIVE)
    if(len(selected)>0):
        isbn_to_del = (str(selected.split(',')[3]),)
        delete_data(isbn_to_del)
       
win.title('Bookstore')
all_books =t.Listbox(win,width=30)
all_books.bind('<Double-Button-1>',selected)
all_books.grid(row=2,columnspan=2,rowspan=5)


title=t.Label(win,text='Title')
title.grid(row=0,column=0,sticky=t.W)

year=t.Label(win,text='Year')
year.grid(row=1,column=0,sticky=t.W)

t_val=t.Text(win,height=1,width=15)
t_val.grid(row=0,column=1)

y_val=t.Text(win,height=1,width=15)
y_val.grid(row=1,column=1)

author=t.Label(win,text='Author')
author.grid(row=0,column=2,sticky=t.E)

ISBN=t.Label(win,text='ISBN')
ISBN.grid(row=1,column=2,sticky=t.E)

a_val=t.Text(win,height=1,width=15)
a_val.grid(row=0,column=3)

I_val=t.Text(win,height=1,width=15)
I_val.grid(row=1,column=3)

view_all=t.Button(win,text='View All',width=15)
view_all.bind("<Button-1>",view_clicked)
view_all.grid(row=2,column=3)
 
search_entry=t.Button(win,text='Search Entry',width=15,command=search_clicked)
search_entry.grid(row=3,column=3)

add_entry=t.Button(win,text='Add entry',width=15,command=add_clicked)
add_entry.grid(row=4,column=3)

update=t.Button(win,text='Update selected',width=15,command=update_clicked)
update.grid(row=5,column=3)

delete =t.Button(win,text='Delete selected',width=15,command=delete_clicked)
delete.grid(row=6,column=3)

win.mainloop()

