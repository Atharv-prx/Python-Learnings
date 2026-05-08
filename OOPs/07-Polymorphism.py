# There are 2 ways to acheive polymorphism-
# 1- Inheritance
# 2- Duck-Typing 

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14*self.radius**2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2
    
class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

shapes = [Circle(4), Square(5),Pizza("Mushrooms",4)]

for x in shapes:
    print(f"{x.area()}")