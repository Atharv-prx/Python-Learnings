# entry widget = textbox that accepts a single line of user input

from tkinter import *

def submit():
    username = entry.get()
    print("Hello " + username)

def delete():
    entry.delete(0,END) # This deletes the line of text

def backspace():
    entry.delete(len(entry.get())-1,END) # Deletes last character
window = Tk()

submit_button = Button(window, text='Submit', command=submit)
submit_button.pack(side= LEFT)

delete_button = Button(window, text= 'Delete', command= delete)
delete_button.pack(side= RIGHT)

backspace_button = Button(window, text='Backspace', command = backspace)
backspace_button.pack()

entry = Entry()
entry.config(font= ('Ink Free', 50),
             bg= "#000000",
             fg= '#FFFFFF',
             width=10,
             show='*')

entry.pack()

window.mainloop()