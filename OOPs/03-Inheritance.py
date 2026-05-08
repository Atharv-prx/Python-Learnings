#Inheritance = Allows a class to inherit attributes and method from another class
#              Helps with code reusability and extensibility
#              class child(parent)

class animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")

class Dog(animal):
    def speak(self):
        print("WOOF!")

class Cat(animal):
    def speak(self):
        print("MEOW!")

class Mouse(animal):
    def speak(self):
        print("SQUEEK!")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.is_alive)
dog.sleep()
dog.eat()
dog.speak()
