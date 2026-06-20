from tkinter import *
import os

def openFile():
    print("File has been opened!")
def saveFile():
    print("File has been saved!")
def cut():
    print("You cut some text!")
def copy():
    print("You copied some text!")
def paste():
    print("You pasted some text!")

window = Tk()

current_dir = os.path.dirname(__file__)

image_path_1 = os.path.join(current_dir,"Images", "Cpp-Logo.png")
cpp_image = PhotoImage(file=image_path_1)

image_path_2 = os.path.join(current_dir,"Images", "Java-Logo.png")
java_image = PhotoImage(file=image_path_2)

image_path_3 = os.path.join(current_dir,"Images", "Python-Logo.png")
python_image = PhotoImage(file=image_path_3)

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="File",menu=fileMenu) # This will have a dropdown like effect
fileMenu.add_command(label="Open",command=openFile,image=cpp_image,compound='left')
fileMenu.add_command(label="Save",command=saveFile,image=java_image,compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit,image=python_image,compound='left')

editMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)

window.mainloop()