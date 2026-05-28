from tkinter import *

def submit():
    print("The tempt is : " + str(celsius_scale.get()) + " degree C") # celsius_scale.get() returns integer so we convert it to srting

window = Tk()

celsius_scale = Scale(window, from_=100, to=0)
celsius_scale.pack()

button = Button(window, text='submit', command=submit)
button.pack()

window.mainloop()