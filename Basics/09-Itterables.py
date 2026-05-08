# Iterables - An object/colelction that can return its element one at a time, 
#             allowing it to be iterated over in a loop

number = [1,2,3,4]
for x in number:
    print(x, end="")
print()
for x in reversed(number):
    print(x,end="")
print()

pokemons = {"Pikachu ", "Balbasaur ", "Charmendar ", "Squirtle "}
for x in pokemons:
    print(x, end="")
print()

name = "Atharv-prx"
for x in name:
    print(x, end="")
print()

my_dictionary = {'A': 1, 'B': 2, 'C': 3}
for x in my_dictionary:           #Prints keys by default without using .keys()
    print(x,end="")
print()
for x in my_dictionary.values():  #Prints value
    print(x,end="")
print()
for x in my_dictionary.items():   #Prints key value pair
    print(x)
print()
for x, y in my_dictionary.items():   #Prints key value pair
    print(x, y)