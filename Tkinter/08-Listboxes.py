# listbox = A listing of selectable text items within it's own container

from tkinter import *

def submit():
    print("You have ordered: ")
    print(list_box.get(list_box.curselection()))

def add():
    list_box.insert(list_box.size(), entry_box.get())     # list_box.size()--> gives current position of index we are currently on
    list_box.config(height=list_box.size())

def delete():
    list_box.delete(list_box.curselection())
    list_box.config(height=list_box.size())
    
window = Tk()

list_box = Listbox(window,
                   bg='#f7ffDE',
                   font=('Constantia',35),
                   width=12,
                   )

list_box.pack()

list_box.insert(1, "pizza")
list_box.insert(2,"pasta")
list_box.insert(3,"garlic bread")
list_box.insert(4,"soup")
list_box.insert(5,"salad")

list_box.config(height=list_box.size()) # Adjusts size dynamically

entry_box = Entry(window)
entry_box.pack()

submit_button = Button(window, text='Submit', command=submit )
submit_button.pack()

add_button = Button(window, text='Add', command=add)
add_button.pack()

delete_button = Button(window, text='Delete', command=delete)
delete_button.pack()

window.mainloop()