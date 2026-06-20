# This is Python's error handling mechanism
#Code runs inside try block
#         │
#         ├── No error? → Continue normally
#         │
#         └── Error occurs? → Jump to except block

#Example --->
while True:
    try:
        n = int(input("How many Chocolates do you want? "))
        if n>0:
            break
        else:
            print("Enter a number greater than 0")
    except ValueError:
        print("Invalid input, Please enter a number")

#This code checks
#         │
#         ├── No error? → Continue normally
#         │
#         ├── If user enters negative number or 0 → returns "Enter a number greater than 0" and then ask again
#         │
#         └── If user enters anything other than number or a floating point value then → returns "Invalid input, Please enter a number" and then ask again