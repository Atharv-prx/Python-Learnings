fruits = ("banana", "orange", "apple", "coconut")
pokemons = ("pikachu", "charmander", "balbasaur", "squirtle")
nums = (1, 2, 8, 3, 7)

fruits = sorted(fruits) # Sort function, after sorting converts into list
pokemons = tuple(sorted(pokemons)) # After sorting coverts into tuple again
nums = sorted(nums)

# nums = sorted(nums, reverse=True) --> reverse sorting

print(fruits)
print(pokemons)
print(nums)