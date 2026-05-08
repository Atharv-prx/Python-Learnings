#fruits = ["Apple", "Pineapple", "Banana", "Coconut"]
#vegetable = ["Tomato", "Potato", "Celery", "Carrots"]
#meats = ["Chicken", "Fish", "Turkey"]

#groceries = [fruits, vegetable ,meats]
#print(groceries[1][2]) #Prints 2nd index in 1st index of groceries

groceries = [["Apple", "Pineapple", "Banana", "Coconut"],
             ["Tomato", "Potato", "Celery", "Carrots"],
             ["Chicken", "Fish", "Turkey"]]
#Itterates over rows
for x in groceries: 
    print(x)

#To itterate over elements in each row we use nested loops
for x in groceries: 
    for y in x:
        print(y, end=" ")  #used end=" " to not skip lines and print() to make it ressemble like matrix
    print()
