# zip() = Combines multiple iterables (lists, tuples, sets, dict) into a single iterator of tuples.
#         Makes managing multiple indices easier.

names = ["charmander", "squirtle", "bulbasaur"]
ages = [5, 6, 7] 

# Instead of this we can use zip function to combine both lists and print them in a single loop
# for name, age in zip(names, ages):
#    print(f"{name} is {age} years old.")

data = zip(names, ages)
# print(data) gives memory address , each pair is stored as tuple

for name, age in data:
    print(f"{name} is {age} years old.")