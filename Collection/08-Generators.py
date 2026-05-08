# Lowkey similar to list comprehension but different
# Normal way creates a full list memory but this is like “Don’t give me everything now… just give me the next value when I ask.”

#Example - 1
class Product:
    def __init__(self, price):
        self.price = price

class Cart:
    def __init__(self, products: list):
        self.products = products

    @property
    def total(self): #Property only takes self
        t = 0
        return sum(x.price for x in self.products)
        
        #Instead of using the given below for loop, we use the above geenrator

        #for x in self.products:
        #    t += x.price
        #return f"Your total is {t}"

p1 = Product (50)
p2 = Product (20)
p3 = Product (30)

c = Cart([p1, p2, p3])
print(c.total) #Can't call it like function it is a property

#Example - 2

# Instead of the given for loop we use ---> count = sum(1 for p in self.products if p.price > 30)
# count = 0
# for p in self.products:
#     if p.price > 30:
#         count += 1