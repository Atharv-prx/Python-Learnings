# *args    = allows you to pass multiple non-key arguments (pack in tupple)
# **kwargs = allows you to pass multiple keyword-arguments (pack in dictionary)
# * ---> Unpacking operator 

#def add (*args):
#    total = 0 
#    for arg in args:
#        total += arg
#    return total
#print(add(1,2,3))

#def print_address(**kwargs):
#    for x, y in kwargs.items():
#        print(f"{x}: {y}")
#print_address(street="123", city= "New york", state= "MI", zip= "29429" )

def shipping_label(*args, **kwargs):
    for x in args:
        print(x, end="")
    print()

    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")


shipping_label("Dr. ", "Spongebob", " Squarepants", " III", street="123", city= "New york", state= "MI", zip= "29429")    