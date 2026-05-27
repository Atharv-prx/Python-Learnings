from tkinter import *
import os

count = 0

def click():
    global count
    count += 1
    print(f"{count} clicks")

window = Tk()

current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "Legion.png")
photo = PhotoImage(file=image_path)

button = Button(window, text = "Click this!!")
button.config(command=click, # Perfoms callback of function
                font=('Ink Free', 50, 'bold'),
                bg = '#e16032',
                fg = '#f8ff00',
                activebackground= '#ff0000', # Shows this colour of background upon clicking 
                activeforeground= "#0703f8", # Shows this colour of foreground upon clicking
                image= photo,
                compound= 'top' ) # Places image on top
# button.config(state = DISABLED) --> Disables button

button.pack()

window.mainloop()