from tkinter import *
from tkinter import filedialog

def openFile():
    file_path = filedialog.askopenfilename(initialdir="C:\\Code\\Python\\Python-Learnings\\File-Handling",
                                           title='Opened File alr ?'
                                           )
    file = open(file_path, 'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(window, text='open', command=openFile)
button.pack()

window.mainloop()

# filedialog.askopenfilename() returns a string which is a file path 