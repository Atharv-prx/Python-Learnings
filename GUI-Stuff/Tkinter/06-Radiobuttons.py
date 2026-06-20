# radio buttons - similar to checkbox, but you can only select one from a group
from tkinter import *
import os

language = ["python", "java", "c++"]

def like():
    if (p.get() == 0):
        print("You like python ")
    
    elif (p.get()==1):
        print("You like Java")

    elif (p.get()==2):
        print("You like c++")
    
    else:
        print("what?")
        
window = Tk()

current_dir = os.path.dirname(__file__)

image_path_1 = os.path.join(current_dir,"Images", "Python-Logo.png")
photo_1 = PhotoImage(file=image_path_1)

image_path_2 = os.path.join(current_dir,"Images", "Java-Logo.png")
photo_2 = PhotoImage(file=image_path_2)

image_path_3 = os.path.join(current_dir,"Images", "Cpp-Logo.png")
photo_3 = PhotoImage(file=image_path_3)

language_images = [photo_1, photo_2, photo_3]

p = IntVar()

for x in range(len(language)):
    radiobutton = Radiobutton(window, 
                              text = language[x],         # Adds text to radio buttons
                              variable=p,                 # Groups radiobuttons
                              value=x,                    # asssigns each radiobutton a different value
                              padx= 25,
                              font=('Imapct',50),
                              image = language_images[x], # Adds image to radiobutton
                              compound= 'left',           # Adds image and text
                              indicatoron=0,              # Eliminates circle indicators
                              width=375,                  # Sets width of radiobuttons
                              command=like)        

    radiobutton.pack(anchor='w')

window.mainloop()