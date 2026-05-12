# Data Class = A special kind of class that's designed mostly for holding data
#              without writing a lot of the boilerplate code for regular classes.
#              They automatically generate: _init__, __repr__, __eq_
#              (Python 3.7+)

from dataclasses import dataclass, field

@dataclass (frozen=True) # frozen=True makes the data class immutable (cannot change values after creation)
class Person:
    name: str
    age: int
    password: str = field(repr=False) # This will exclude the password from the generated __repr__ method for security reasons
    is_alive: bool = True

    # Data class can automatically call __post_init__ after __init__ to perform additional initialization
    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")

person1 = Person("Alice", 30, "Pineapple123")
person2 = Person("Patrick", 35, "SecretPassword", is_alive=False)
# person3 = Person("Bob", -5) ---> Would give ValueError because age cannot be negative

# person1.age = 31 # Would give error because the data class is frozen (immutable)

print(person1) 
print(person2) 
print(person1 == person2) # False because they have different values