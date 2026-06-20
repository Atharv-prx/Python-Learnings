class Fruit:
    def __init__(self, name,calories):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f"{self.name}: {self.calories} calories"

fruits = [Fruit("banana", 100), 
          Fruit("coconut", 300), 
          Fruit("orange", 200),
          Fruit("apple", 72)]

# fruits = sorted(fruits, key=lambda fruit: fruit.name)
# fruits = sorted(fruits, key=lambda fruit: fruit.name, reverse=True)

# fruits = sorted(fruits, key=lambda fruit: fruit.calories)
fruits = sorted(fruits, key=lambda fruit: fruit.calories, reverse=True)

print(fruits)