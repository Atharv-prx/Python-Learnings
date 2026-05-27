from tkinter import *
import os

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widge    

window = Tk() # instantiate an instance of windows

window.geometry("420x420") # (width x height)

window.title("First GUI") # Changes Title

# Replacing feather icon, we need to convert photo into "photo image" cuz that's the format that tkinter understands
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "Legion.png")

icon = PhotoImage(file = image_path)

window.iconphoto(True, icon)

window.config(background = "black")# Changes window colour
window.mainloop() # Place window on computer screen, listen fo events