# This function basically check if a object is from a particular class/type
# isinstance (object, type)
# It return True or False

# Simple-Example
# x = 5
# print(isinstance(x, int)) --> Returns - true

# name = "Rahul"
# print(isinstance(name, str)) --> Returns - true

class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("This animal makes a sound")


class Dog(Animal):

    def speak(self):
        print(f"{self.name} says Woof!")


class Cat(Animal):

    def speak(self):
        print(f"{self.name} says Meow!")


class Car:

    def __init__(self, brand):
        self.brand = brand


def animal_sound(animal):

    if isinstance(animal, Animal):
        animal.speak()

    else:
        print("Invalid object! Not an Animal.")


dog1 = Dog("Rocky")
cat1 = Cat("Milo")
car1 = Car("BMW")

animal_sound(dog1)
animal_sound(cat1)
animal_sound(car1)