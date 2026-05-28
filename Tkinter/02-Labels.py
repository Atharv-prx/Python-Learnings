# label = an area widget that holds text and/or an image within a window

from tkinter import *
import os

window = Tk()

current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir,"Images", "Legion.png")
photo = PhotoImage(file=image_path)

label = Label(window,
              text="Legion Faction",
              font=('Arial',20,'bold'), 
              fg= "Pink",    # foreground colour (font colour)
              bg='black',    # background colour
              relief=RAISED, # border style
              bd=10,         # border thickness
              padx=20,       # adds some space between the x axis of text between border
              pady=20,       # adds some space between the y axis of text between border
              image=photo,   
              compound='bottom') # we set deirection of where image should be place with respect to text
label.pack()
#label.place(x=0,y=0)

window.mainloop()