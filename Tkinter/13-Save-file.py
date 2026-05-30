from tkinter import *
from tkinter import filedialog

def saveFile():
    file_path = filedialog.asksaveasfilename(
        initialdir="C:\\Code\\Python\\Python-Learnings\\Tkinter", # place where we wanna save file goes here
        defaultextension=".txt", 
        filetypes=[     # supported extensions
            ("Text File", "*.txt"),
            ("HTML File", "*.html"),
            ("All Files", "*.*")
        ]
    )

    if file_path:  # User didn't cancel
        with open(file_path, "w") as file:
            file.write(text.get("1.0", END))

window = Tk()

button = Button(window, text='save', command=saveFile)
button.pack()

text = Text()
text.pack()

window.mainloop()

# can also use this 
#    filetext = input("Enter some text I guess: ")
#    file.write(filetext)
#    file.close()
# instead of 
#    if file_path:  # User didn't cancel
#        with open(file_path, "w") as file:
#            file.write(text.get("1.0", END))
# if we wanna enter text from terminal rather than TEXT()