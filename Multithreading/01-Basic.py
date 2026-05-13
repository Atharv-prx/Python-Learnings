# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs

import threading
import time

def walk_dog(name, dog_name):
    time.sleep(6) # Simulate the time taken to walk the dog
    print(f"{name} finishes walking {dog_name}")

def take_out_trash():
    time.sleep(2)
    print("You finish taking out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

chore1 = threading.Thread(target = walk_dog, args = ("Spongebob", "Goofy")) # args is used to pass arguments to the target function
chore1.start() 
# When we use single parametre be sure to add a comma after the argument in args --> args = ("Spongebob",) otherwise it will give error because it will not recognize it as a tuple                                     

chore2 = threading.Thread(target = take_out_trash)
chore2.start()

chore3 = threading.Thread(target = get_mail)
chore3.start()

chore1.join() # Wait for chore1 to finish before moving on
chore2.join() # Wait for chore2 to finish before moving on
chore3.join() # Wait for chore3 to finish before moving on

print("You finish all your chores")

# Creating thread - threading.Thread()
# Target function - target = function name ---> this tells “Run this function in a separate thread.”
# Passing arguments - args = (arg1, arg2, ...), or when we have single argument then --> args = (arg1,) 
# Starting Threads Concurrently - start()
# Waiting for Threads to Finish - join()