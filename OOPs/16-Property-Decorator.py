# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit: Add additional logic when you read, write, or delete attributes
#             Gives you a getter, setter, and deleter method

class Rectangle:
    def __init__(self, width, height):
        # Prefix these attributes with _ so that it tell us and other devs that these attributes are meant to be protected, 
        # they are internal we shouldn't access these outisde of the class
        self._width = width   
        self._height = height

        #Additional logic
    @property
    def width(self):
        return f"{self._width:.1f} cm"

    @property
    def height(self):
        return f"{self._height:.1f} cm"
    
    @width.setter
    def width(self, new_width):
        if new_width>0:
            self._width = new_width
        else:
            print("Width must be greater than 0")

    @height.setter 
    def height(self, new_height):
        if new_height>0:
            self._height = new_height
        else:
            print("Height must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")

rec1 = Rectangle(10,20)

rec1.width = 5
rec1.height = 6

del rec1.width
del rec1.height