#Variable Scope- Where a variable is both visible and accessible 
#Scope Resolution- (LEGB)== Local --> Enclosed --> Global --> Built-In 

# Local

def func1():
    x = 1 #local
    print(x)

def func2():
    x = 2 #local
    print(x)

func1()
func2()

# Enclosed Scope
def func1():
    x=1
    def func2():
        print(x)
    func2()

func1()

# Global Scope
def func1():
    print(x)

def func2():
    print(x)

x = 3 #global

func1()
func2()

# Built-In
from math import e 

def func1():
    print(e)

func1()