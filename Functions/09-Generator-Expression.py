# Generator Expression = Similar to a list comprehension but uses () instead of []
#                        Creates a generator (iterator) that yields values one at a time
#                        No need to define a function or use yield
#                        Less flexible than a gen func and not reusable

number = int(input("Enter a number to count upto: "))
x = (value for value in range(1, number + 1)) # Gnerator expression

for n in x:
    print(n)

num = int(input("Enter a number to square upto: "))
y = (value ** 2 for value in range(1, num + 1)) # Can also add a if condition--> 
                                                # value ** 2 for value in range(1, num + 1) if value % 2 == 0 --> to get only even squares
for n in y:
    print(n)

#----- File reading with generator expression -----
file_path = "Python-Learnings/Functions/08-Text.txt"
with open(file_path, "r") as file:
    lines = (line.strip() for line in file) # Generator expression to read lines from a file
    for line in lines:
        print(line)