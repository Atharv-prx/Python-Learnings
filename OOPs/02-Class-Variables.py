# Class-Variables = Shared among all instances of class, Defined outside the constructor
#                   Allows you to share data among all objects created from that class 

class pokemon:

    age = 7 #Class variable
    num_pokemon = 0

    def __init__(self, name, type):
        self.name = name
        self.type = type  #Instance variable
        pokemon.num_pokemon += 1

pokemon1 = pokemon("pikachu", "electric")
pokemon2 = pokemon("balbasaur", "grass")
pokemon3 = pokemon("charmander", "red")
print(pokemon1.name)
print(pokemon1.type)
print(pokemon.age)
print(pokemon.num_pokemon)