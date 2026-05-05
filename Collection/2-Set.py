# Set   - {} unordered and immutable, but Add/Remove Ok. No duplicates 

fruits = {"Apple", "Orange", "Banana", "Coconut"}
print(fruits) #Prints in different order
print(len(fruits))
print("Coconut" in fruits)

fruits.add("Pineapple")
fruits.remove("Apple")
print(fruits)

fruits.pop() #Removes random element
print(fruits)

fruits.clear() #Clears set
print(fruits)
