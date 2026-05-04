# Decorator = A function that extends the behavior of another function without modifying the base function
#             Pass the base function as an argument to the decorator

#Decorater-1
def add_sprinkles(func):
    # We need wrapper function so that this function is only called when we call get_icecream function
    def wrapper(*args, **kwargs): # We need args and kwargs here so that it can accept any king of arguments and keyword-arguments if needed
        print("You add sprinkles")
        func(*args, **kwargs) # Same explanation as line 7
    return wrapper

#Decorator-2
def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_icecream(flavour):
    print(f"Here is your {flavour} ice-cream")

get_icecream("Chocolate")