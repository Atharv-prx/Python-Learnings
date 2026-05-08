# Dictionary = a collection of {key: value} pair
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.", "India": "New Delhi", "China": "Bejing"}

print(capitals.get("USA")) #Prints value for USA
print()

#To check if a key is in a dictionary--> if capitals.get("Japan"): 
#                                            print("Capital does exist")
#                                        else:
#                                            print("Capital doesn't exist")

capitals.update({"Germany": "Berlin"}) #Can also use this to update any value
capitals.pop("China") #Removes a key
print(capitals)
print()

#capitals.clear() --> clears dictionary
#To get all keys--> Keys = capitals.keys() 
#                   print(Keys)

for x in capitals.keys(): #Itterating over keys
    print(x)
print()

#To get all values--> Value = capitals.values() 
#                     print(Value)

for x in capitals.values(): #Itterating over values
    print(x)
print()

#Items returns a dictionary object which resembles 2-D tupples--> Items = capital.items()
#                                                                 print(Items)

for key, value in capitals.items():
    print(f"{key}: {value}")
print()