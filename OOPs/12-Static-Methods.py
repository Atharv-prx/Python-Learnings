# Static methods = A method that belong to a class rather than any object from that class (instance)
#                                Usually used for general utility functions

# Instance methods - Best for operations on instances of the class (objects) ----WE ALREADY KNOW THIS
# Static methods - Best for utility functions that do not need access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions
    
employee1 = Employee("Eugune", "Manager")
employee2 = Employee("Spongebob", "Cook")

# For instance method, we access an object then call instance method
print(employee1.get_info())
print(employee2.get_info())

# For static method, we only need to access that class; we don't even need to create objects from that class hence it's a geenral utility method
print(Employee.is_valid_position("Rocket Scientist"))
print(Employee.is_valid_position("Cashier"))