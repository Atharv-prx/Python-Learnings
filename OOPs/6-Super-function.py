# super() = used within a child class to call methods from parent class
#           child class is subclass and parent class is superclass
#           Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, colour, is_filled):
        self.colour = colour
        self.is_filled = is_filled
    def describe(self):
        print(f"It is {self.colour} and {'filled' if self.is_filled else 'not filled'}")

#We have to call constructor of super class in constructor of children class
#So instead of using self.colour() and self.is_filled every time time for every child class we just use this
    
class Circle(Shape):
    def __init__(self, colour, is_filled, radius):
        super().__init__(colour, is_filled)  
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        super().describe()
class Square(Shape):
    def __init__(self, colour, is_filled, width):

        super().__init__(colour, is_filled)

        self.width = width

class Triangle(Shape):
    def __init__(self, colour, is_filled, width, height):

        super().__init__(colour, is_filled)

        self.width = width
        self.height = height

circle = Circle(colour = "red", is_filled = True, radius = 5)
#circle = Circle("red", True, 5)  ----> Can also write like this

square = Square("blue", False, 4)
triangle = Triangle("green", True, 7,8)

print(circle.colour)
print(circle.is_filled)
print(f"{circle.radius}cm")
print()

print(square.colour)
print(square.is_filled)
print(f"{square.width}cm")
print()

print(triangle.colour)
print(triangle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")
print()

circle.describe() #If parent and child class both have same method then children class method prevails

#if we want to use both describe method then we add