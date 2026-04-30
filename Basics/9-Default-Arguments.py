# Default arguments = A default value for certain parametres 
#                     default is used when an argument is ommited 
#                     Reduces number of arguments you have to pass in 
import time

def count(end, start=0):  # If we use any default arguments then make sure that they are after poistional argument
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    return "Done!"

print(count(3,1))   