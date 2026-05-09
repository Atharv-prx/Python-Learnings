fruits = {"banana" : 90, "orange" : 70, "apple" : 75, "coconut" : 350}

# fruits = sorted(fruits) --> Keys get sorted in alphabetical order and values get truncated
# fruits = sorted(fruits.keys()) --> Does same thing as above
# fruits = sorted(fruits.values()) --> Values get sorted but keys get truncated

## Sort by key

# fruits = dict(sorted(fruits.items())) --->used dict() to convert output into dictionary

# fruits = dict(sorted(fruits.items(), key=lambda x: x[0], reverse=True)) # ---> Reverse order
# key=lambda x: x[0] --->  Since items method return a tuple during each itteration 
#                          So this basically says that for each pair of items in dictionary take each pair(x) and return the first element/element at index 0  

## Sort by value

fruits = dict(sorted(fruits.items(), key=lambda x: x[1])) # Index of 1 applies to the value, whearas index of 0 refers to keys

# fruits = dict(sorted(fruits.items(), key=lambda x: x[1], reverse = Ture)) ---> Reverses 

print(fruits)