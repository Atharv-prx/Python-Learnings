from tkinter import *
import os

def submit():
    print("The tempt is : " + str(celsius_scale.get()) + " degree C") # celsius_scale.get() returns integer so we convert it to srting

window = Tk()

current_dir = os.path.dirname(__file__)
image_path_1 = os.path.join(current_dir,"Images", "fire.png")
fire_image = PhotoImage(file=image_path_1)

fire_label = Label(image=fire_image)
fire_label.pack()

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

image_path_2 = os.path.join(current_dir,"Images", "snowflake.png")
cold_image = PhotoImage(file=image_path_2)

cold_label = Label(image=cold_image)
cold_label.pack()

button = Button(window, text='submit', command=submit)
button.pack()

window.mainloop()