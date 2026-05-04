# Composition - The composed object owns its components, which cannot exist independently

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        # Where composition comes in
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)] #Did list comprehension cuz car wheel got 4 wheels 🥀

    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}in"
                                    #since engine has attribute of horese power
car1 = Car("Ford", "Mustang", 500, 20)
car2 = Car(make="Chevrolet", model="Corvette", horse_power=670, wheel_size=19)

print(car1.display_car())
print(car2.display_car())