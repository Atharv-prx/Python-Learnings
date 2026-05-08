# Abstract-Classes - A class that can't be instantiated on it's own; Meant to be subclassed
#                    They contain abstract methods, which are declared but have no implementation.
# Benefits - 1.Prevents instantiation of the class itself
#            2.Requires children to use inherited abstract methods

from abc import ABC, abstractmethod #abc = abstract base classes, ABC = abstract base class

class Vehicle(ABC):
    
    #We declare them but don't define them, we define them in children classes
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle): 
    #If a class is inheriting from a parent which is abstract and there are abstract methods then we have to finish defining thode methods
    def __init__(self, name):
        self.name = name    
    def go(self):
        print(f"You drive {self.name}")

    def stop(self):
        print(f"You stop {self.name}")   
    
car1 = Car("Mustang")

car1.go()
car1.stop()