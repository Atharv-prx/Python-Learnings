# listbox = A listing of selectable text items within it's own container

from tkinter import *

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

window.mainloop()