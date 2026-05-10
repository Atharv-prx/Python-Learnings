import os

# Absolute File path
# file_path = "C:/Users/Yash verma/OneDrive/Desktop/Python/Python-Learnings/File-Handling/01-test.txt"

file_path = "File-Handling/01-test.txt"

if os.path.exists(file_path):#Exists methods return a boolean value
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path): #Checks if a file is a file and not a directory
        print("That is a file")
else:
    print("That location doesn't exists.")