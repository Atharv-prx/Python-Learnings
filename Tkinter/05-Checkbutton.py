from tkinter import *
import os

def display():
    if (x.get() == 1)&(y.get()==0):
        print("I like Python")
    
    elif(x.get()==0)&(y.get()==1):
        print("I like java")
    
    elif(x.get()==1)&(y.get()==1):
        print("I like both")
    
    else:
        print("Both suck lmao")

window = Tk()

x = IntVar()
y = IntVar()

current_dir = os.path.dirname(__file__)
image_path_1 = os.path.join(current_dir, "Python-Logo.png")
photo_1 = PhotoImage(file=image_path_1)

current_dir = os.path.dirname(__file__)
image_path_2 = os.path.join(current_dir, "Java-Logo.png")
photo_2 = PhotoImage(file=image_path_2)

checkbox_1 = Checkbutton(window, text= 'Python', variable=x, onvalue=1, offvalue=0, command=display)
checkbox_1.pack()

checkbox_1.config(font= ('Arial', 20),
                fg= '#00FF00',
                bg= '#000000',
                activeforeground= '#0000FF',
                activebackground= '#000000',
                image= photo_1, compound= 'left',
                padx= 25, pady= 10, width= 200, height= 50,
                anchor= 'w') #anchors widget to relative cardinal direction

checkbox_2 = Checkbutton(window, text= 'Java', variable= y, onvalue=1, offvalue=0, command= display)
checkbox_2.pack()

checkbox_2.config(font= ('Arial', 20),
                  fg='#0000FF',
                  bg='#000000',
                  activeforeground='#0000FF',
                  activebackground='#000000',
                  image= photo_2, compound= 'left',
                  padx=25,pady=10,width=200,height=50,
                  anchor='w')

window.mainloop()