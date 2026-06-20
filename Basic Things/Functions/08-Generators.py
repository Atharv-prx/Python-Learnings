# Generator = Function that behaves like an iterator (it can be used in a for loop)
#             Pauses a function, returns a value, then resumes
#             Uses 'yield' instead or 'return'
#             Iterate without loading everything into memory (ex. reading large files)
#             return = Pouring bucket
#             yield = Drip faucet

def count_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

number = int(input("Enter anumber to count to: "))

for n in count_to(number):
    print(n, end=" ")

# This would crash if user enters a absurdly large num
#    numbers = []
#    count = 1
#    while count <= n:
#        numbers.append(count)
#        count += 1
#    return numbers

# ------Reading a file using generators------

file_path = "Functions/08-Text.txt"

def read_file(file_path):

    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()  # Yielding each line one at a time, 
                                # strip function removes any unwanted characters from beginning and end of the string

for line in read_file(file_path):
    print(line) 