# '''xyz''' --> this is not comment but docstring lways used right above the function definition 

def square(n):
    '''Takes a number n , returns the square of n'''
    print(n**2)

square(5)
print(square.__doc__)