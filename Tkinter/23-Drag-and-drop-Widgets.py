from tkinter import *

def drag_start(event):
    widget = event.widget # the widget that triggered the event
    widget.startX = event.x # the x coordinate of the mouse
    widget.startY = event.y # the y coordinate of the mouse

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x # winfo gets top left x coordinate of our label relative to window that we are in, then we subtract the startX to get the distance we have moved the mouse, and then we add the current x coordinate of the mouse to get the new x coordinate of the label
    y = widget.winfo_y() - widget.startY + event.y # winfo gets top left y coordinate of our label relative to window that we are in, then we subtract the startY to get the distance we have moved the mouse, and then we add the current y coordinate of the mouse to get the new y coordinate of the label
    widget.place(x=x,y=y) # the place method is used to move the widget to the new coordinates

window = Tk()

label = Label(window,bg="red",width=10,height=5)
label.place(x=0,y=0)

label2 = Label(window,bg="blue",width=10,height=5)
label2.place(x=100,y=100)

label.bind("<Button-1>",drag_start) # if we click the left mouse button on the label, it will call the drag_start function
label.bind("<B1-Motion>",drag_motion) # if we click the left mouse button and move the mouse, it will call the drag_motion function

label2.bind("<Button-1>",drag_start) # if we click the left mouse button on the label2, it will call the drag_start function
label2.bind("<B1-Motion>",drag_motion) # if we click the left mouse button and move the mouse, it will call the drag_motion function

window.mainloop()