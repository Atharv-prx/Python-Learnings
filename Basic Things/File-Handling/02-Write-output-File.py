# Python writing files (.txt, .json, .csv)

# -------txt file writing-------- (txt = text)

txt_data = "Some theory about file writing in python.\nAlso I like watching anime."

file_path1 = ("File-Handling/02-output.txt")

try:
    with open(file_path1, "w") as file:
        file.write(txt_data)
        print(f"txt file '{file_path1}' has been created and data has been written to it.")

    with open(file_path1, "a") as file:
        file.write(
            "\n\nwith is a keyword used to wrap a block of code.\n"
            "The open() function is used to open a file.\n"
            "'w' mode writes to a file and overwrites the file if it already exists.\n"
            "'a' mode appends to the file, if file doesn't exist, it will be created.\n"
            "'x' mode creates a new file and raises an error if it already exists.\n"
            "'r' mode reads a file, if file doesn't exist, it will raise an error.\n"
        )

        print(f"Data has been appended to the txt file '{file_path1}'.")

except Exception as e:
    print(e)    

# Can also use this, works everytime, but it is a bit more complex than the above method.
# current_dir = os.path.dirname(__file__)
# file_path = os.path.join(current_dir, "02-atest.txt")

# -------json file writing-------- (json = JavaScript Object Notation)
import json

employee = {
   "name": "Spongebob",
   "age": 30,
   "job": "Cook"
}

file_path2 = "File-Handling/02-output.json"

try:
    with open(file_path2, 'w') as file:
        json.dump(employee, file, indent=4)

        # indent parameter is used to format the json string in a more readable way, it adds indentation to the json string.
        # dump method will convert our dictionary to json string to output it to the file.

    print(f"JSON file '{file_path2}' has been created successfully")
    
except FileExistsError:
    print("That file already exists!")

# -------csv file writing-------- (csv = comma separated values)
import csv

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path = "File-Handling/02-output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)

        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")

except FileExistsError:
    print("That file already exists!")