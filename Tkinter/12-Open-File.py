from tkinter import *
from tkinter import filedialog

def openFile():
    file_path = filedialog.askopenfilename(initialdir="C:\\Code\\Python\\Python-Learnings\\File-Handling\\02-output.csv")
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)

window = Tk()

button = Button(window, text='open', command=openFile)
button.pack()

window.mainloop()

# filedialog.askopenfilename() returns a string which is a file path 