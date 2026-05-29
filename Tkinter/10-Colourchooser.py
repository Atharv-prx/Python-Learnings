from tkinter import *
from tkinter import colorchooser

def click():
    colour = colorchooser.askcolor()
    colourhex = colour[1]

    print(colourhex)
    window.config(bg=colourhex)

window = Tk()

window.geometry("420x420")

button = Button (text='click me', command=click)
button.pack()

window.mainloop()