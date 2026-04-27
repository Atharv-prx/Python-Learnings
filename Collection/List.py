# Collection = single "variable" used to store multiple values
# List  - [] ordered and changeable. Duplicated OK

fruits = ["Apple", "Orange", "Banana", "Coconut"]
print(fruits[0:3]) #Prints first 4 elements
print(fruits[0:4:2]) #Prints every 2nd element beginning from index 0
print(fruits[::-1]) #Prints list backwards

for x in fruits:
    print(x)
print(len(fruits))   
print("Apple" in fruits) #Checks if Aplleis in fruits

fruits.append("Pineapple")
print(fruits)

fruits.insert(0,"Pumpkin")
print(fruits)

num = [5,2,7,3,9]
num.sort()
print(num)

num.reverse() #Prints sorted reverse order
print(num)