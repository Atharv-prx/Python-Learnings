from tkinter import *
import os

def move_up(event):
   canvas.move(myimage,0,-10) # move the image 10 pixels up (0 in x direction, -10 in y direction)
def move_down(event):
   canvas.move(myimage,0,10) # move the image 10 pixels down (0 in x direction, 10 in y direction)
def move_left(event):
   canvas.move(myimage,-10,0) # move the image 10 pixels left (-10 in x direction, 0 in y direction)
def move_right(event):
   canvas.move(myimage,10,0) # move the image 10 pixels right (10 in x direction, 0 in y direction)

window = Tk()

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

canvas = Canvas(window,width=500,height=500)
canvas.pack()

current_dir = os.path.dirname(__file__)
image_path_1 = os.path.join(current_dir,"Images", "Legion-Logo.png")
legion_image = PhotoImage(file=image_path_1)

myimage = canvas.create_image(0,0,image=legion_image,anchor=NW) 

window.mainloop()
# anchor=NW means the image will be placed at the top-left corner of the canvas