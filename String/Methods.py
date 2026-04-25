# To know list of all methods available just type --> print(help(str))

name = input ("What's your name: ")

# result = len(name)             --> Give length of name
# result = name.find("x")        --> Gives first occurence of x letter 
# result = name.rfind("x")       --> Gives last occurence of x letter
# result = name.capitalize()     --> Capitalizes first letter
# result = name.upper()          --> Makes all letter uppercase
# result = name.lower()          --> Makes all letter lowercase
# result = name.isdigit()        --> Returns true only if string contains only digits
# result = name.isalpha()        --> Return true only if string contains alphabetical characters
# result = name.count("x")       --> Counts number of x in string
result = name.replace("x","y")  #--> Replaces x with y in string

print(result)