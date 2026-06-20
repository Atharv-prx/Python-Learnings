from tkinter import *
import os

def move_up(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()-10)

def move_down(event):
   label.place(x=label.winfo_x(), y=label.winfo_y()+10)

def move_left(event):
   label.place(x=label.winfo_x()-10, y=label.winfo_y())

def move_right(event):
   label.place(x=label.winfo_x()+10, y=label.winfo_y())

window = Tk()

window.geometry("500x500")
window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

current_dir = os.path.dirname(__file__)
image_path_1 = os.path.join(current_dir,"Images", "Legion-Logo.png")
legion_image = PhotoImage(file=image_path_1)

label = Label(window, image=legion_image,bg= "white")
label.place(x=0,y=0)


window.mainloop()