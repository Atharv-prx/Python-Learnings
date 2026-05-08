# Keyword Arguments - An arguments preceeded by an identifier, helps with readability
#                     Order of arguments doesn't matter

def Hello(greetings, title, first, last):
    print(f"{greetings} {title} {first} {last}")

Hello("Hello", title="Mr", first="Squarepants", last="Spongebob") #Positional arguments follow keyword arguments

#Separate Keyword argument 
print("1", "2", "3", "4", "5", sep="-")