from tkinter import *

def doSomething(event):
    #print("You pressed: " + event.keysym) event.keysym shows the name of the key that was pressed
    label.config(text=event.keysym) # displays symbol of key we press

window = Tk()

window.bind("<Key>",doSomething)

label = Label(window,font=("Helvetica",100))
label.pack()

window.mainloop()