# Object = A "Bundle" of related attribute(variable) and methods(functions)
#          You need a "Class" to create many objects

#Class = (blueprint) used to design the structure and layout of an object 

class car:
    #constructor
    def __init__(self, model, year, colour, for_sale):
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive a {self.model}")

    def stop(self):
        print(f"You stop the {self.model}")

car1 = car("Mustang", 2024, "red", False)
car2 = car("Corvette", 2025, "blue", True)

print(car1)  # prints memory address

print(car1.model)   # . is known as attribute access operator
print(car1.year) 
print(car1.colour)
print(car1.for_sale)
car1.drive()
car1.stop()