# Map

# Map is like comprehension
# Let's us call a function on every item in an iterable

def cube(number):
	return number ** 3

numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(cube, numbers)

# We passed in the function but didn't call it
# How to call

# or for loop
for number in cubed_numbers:
    print(cubed_numbers)
# Unpacking the numbers using *args
print(*cubed_numbers, sep=",")
# or store as a list
# cubed_numbers = list(map(cubed_numbers))

# map works with multiple collections
def add(a, b):
	return a + b

odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8, 10]

totals = map(add, odds, evens)
print(*totals, sep=", ")  # 3, 7, 11, 15, 19

# Map with lambda expressions
# Cube with lambda
numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(lambda number: number **3, numbers)
print(*cubed_numbers, sep = ",")

# Operator
# lambda in this case is just another way of using **kwargs
# Operator has some built in functions
# It has add and some other functions

from operator import add

odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8, 10]

totals = map(add,odds,evens)
print(*totals, sep =", ")

# Method caller is also a useful function
# it has title
from operator import methodcaller

names = ["tom", "richard", "harold"]
title_names = map(methodcaller("title"), names)

# Conditional Comprehension
# Allows us to Filter

# If the condition is True, the item is added
# if False, the item is discarded
numbers = [1, 56, 3, 5, 24, 19, 88, 37]

# Comprehension
even_numbers = [number for number in numbers if number % 2 == 0]

# This is a little harder to read, so using a finction

def is_even(number):
    return number % 2 == 0

numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = filter(is_even, numbers)

# Filter can only handle one collection at a time

# You can use None with filters
# This will discard all False values and keep all True values

values = [0, "Hello", [], {}, 435, -4.2, ""]
truthy_values = filter(None, values)

print(*truthy_values, sep=", ")


# Use map and strip to print on different lines

humpty_dumpty = [
	"  Humpty Dumpty sat on a wall,  ",
	"Humpty Dumpty had a great fall;     ",
	"  All the king's horses and all the king's men ",
	"    Couldn't put Humpty together again."
]

def stip(line):
    return line.strip()

processed_lines = map(stip, humpty_dumpty)
print(*processed_lines, sep="\n")

'''
Use a list comprehension with a filtering condition so that only names with 
fewer than 8 characters end up in the new list. 
Make sure that every name in the new list is in title case.
'''

names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")

short_names = [name.title() for name in names if len(name) < 8]
print(short_names)

'''
Use filter to remove all negative numbers from the following range: 
range(-5, 11). Print the remaining numbers to the console.
'''

print(*filter(lambda number: number >= 0, range(-5, 11)))
def is_positive(number):
	return number >= 0

print(*filter(is_positive, range(-5, 11)))