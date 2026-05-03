# Multiple-Inheritance = When child class inherits from multiple classes
#                        C(a,b)

#MultiLevel-Inheritance = Inherit from  a parent which inherits from another parent
#                        C(b) <- b(a) <- a

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal): #Inheritance
    def flee(self):
        print("This animal is fleeing")

class Predator(Animal): #Inheritance
    def hunt(self):
        print("This animal is hunting")


class Rabbit(Prey): #Multilevel inheritance
    pass
    
class Hawk(Predator):  #Multilevel inheritance
    pass

class Fish(Prey, Predator):  #Multilevel/Multiple inheritance
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.eat()
rabbit.sleep()

fish.eat()
fish.sleep()