# A consice way to create lists 
# Comoact and easier to read than a tradionional loop
# [ expression for value in itterable if condition]

#Traditional Loop

doubles = []
for x in range(1,11):
    doubles.append(x*2)
print(doubles)

#List-Comprehension
numbers = [ x*2 for x in range(1,11)]    
print(numbers)

#Example
fruit = ["apple", "orange", "banana", "coconut"]
uppercase_words = [x.upper() for x in fruit]
print(uppercase_words)

fruit_chars = [x[0] for x in fruit]
print(fruit_chars)

numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_numbers = [x for x in numbers if x >= 0]
negative_numbers = [x for x in numbers if x < 0]
even_numbers = [x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x % 2 == 1]
print(positive_numbers)
print(negative_numbers)
print(even_numbers)
print(odd_numbers)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)