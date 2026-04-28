import random

#To randomize numbers from 1 to 6
number = random.randint(1,6)
print(number)

number = random.random() #-->  return a floating point num from random module
print(number)

options = ("Rocks", "Paper", "Scissor")
x = random.choice(options)
print(x)

cards = ["2", "3", "4", "6", "7", "k", "a"]
random.shuffle(cards)
print(cards)
