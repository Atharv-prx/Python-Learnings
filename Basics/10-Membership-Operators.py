# Membership operators = Used to test whether a variable or value is found within a sequence
#                        (String, List, Set or Dictionary)
#                        1. in
#                        2. not in

# Example-1
word = "apple"
letter = input("Guess the letter in secret word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")

# Example-2
students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter the name of a student: ")

if student in students:
   print(f"{student} is in this class")
else:
   print(f"{student} is NOT in this class")

#Example-3
grades = {"Sandy": 'A' , "Squidward": 'B', "Spongebob": 'C', "Patrick": 'D'}

student = input("Enter the name of a student: ")

if student in grades:
   print(f"{student}'s grade is {grades[student]}.")
else:
   print(f"{student} is not in the dictionary")