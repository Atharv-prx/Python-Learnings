from tkinter import *
import os

def submit():
    print("The tempt is : " + str(celsius_scale.get()) + " degree C") # celsius_scale.get() returns integer so we convert it to srting

window = Tk()

celsius_scale = Scale(window, 
                      from_=100, 
                      to=0,
                      length= 500,
                      orient=VERTICAL,
                      font= ('Consolas',20),
                      tickinterval=10, # adds numeric indicators for value
#                     showvalue=0, # hide current value besides slider
                      troughcolor= '#69EAFF',
                      fg = '#FF1C00',
                      bg = '#111111'
                      )
celsius_scale.set(((celsius_scale['from']-celsius_scale['to'])/2) +celsius_scale['to'])
celsius_scale.pack()

button = Button(window, text='submit', command=submit)
button.pack()

window.mainloop()