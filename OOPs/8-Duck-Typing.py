# Duck Typing - Another way to acheive polymorphism besides inheritance
#               Object must have minimum necessary attributes/methods
#               "If it looks like a duck and wuacks like a duck, then it must be a duck"

class Animal:
    alive = True      #This is defining attribute

class Dog(Animal):
    def speak(self):  #This is defining method
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Cars:
    alive = False
    def speak(self):
        print("Honk!")

animals = [Dog(), Cat(), Cars()]

for x in animals:
    x.speak()         #This is method calling
    print(x.alive)    #This is attribute calling