
import os
current_dir = os.path.dirname(__file__)

# -------txt file reading-------- 

file_path1 = os.path.join(current_dir, "02-output.txt")

try:
    with open(file_path1, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("The file was not found.")
except PermissionError:
    print("You do not have permission to read the file.")

# -------txt file reading--------
import json

file_path2 = os.path.join(current_dir, "02-output.json")

try:
    with open(file_path2, "r") as file:
        content = json.load(file)
        print(content)
        # We can also access our content by it's key of name
        print(content["name"])
        print(content["age"])
        print(content["job"])
        print()

except FileNotFoundError:
    print("The file was not found.")
except PermissionError:
    print("You do not have permission to read the file.")

# -------csv file reading--------
import csv

file_path3 = os.path.join(current_dir, "02-output.csv")

try:
    with open(file_path3, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
        # only using print(content) would give memory address so we need to itterate over 
        # to access a particular line we can use --> print(line[index]) instead of print(line)
except FileNotFoundError:
    print("The file was not found.")
except PermissionError:
    print("You do not have permission to read the file.") 