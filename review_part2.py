import json
import math
import itertools

# 1 Comprehension exercises
'''
1)
Convert this into a comprehension
'''

numbers = [1, 2, 3, 4, 5]
squares = []

print("Exercise 1: ")
numbers_and_squares = [{number: number **2} for number in numbers]
print(*numbers_and_squares)
print()

'''
2) 
Use a dictionary comprehension to convert this to a new dictionary in title case
'''
movie = {
	"title": "thor: ragnarok",
	"director": "taika waititi",
	"producer": "kevin feige",
	"production_company": "marvel studios"
}

print("Exercise 2")
appended_movies = {key.title(): value.title() for key,value in movie.items()}
print(appended_movies)
print()

# 2 Quicksort

# 3 Day 16 exercises

# Review
'''
1) 
Use the sort method to sort this alphabetically by student names
'''

students = [
	{"name": "Hannah", "grade_average": 83},
	{"name": "Charlie", "grade_average": 91},
	{"name": "Peter", "grade_average": 85},
	{"name": "Rachel", "grade_average": 79},
	{"name": "Lauren", "grade_average": 92}
	]

print("Exercise 3")
students.sort(key=lambda student: student['name'])
print(students)
print()

''''
2) 
Convert the following function to a lambda expression and assign it to a variable called exp.
'''

def exponentiate(base, exponent):
	return base ** exponent


print("Exercise 3.1")

print()

# 4 Day 17 exercises
'''
1)
Create a function that accepts any numbers as positional arguments that prints the sum of those numbers.
'''

print("Exercise 4.1")

print()

'''
2) 
Create a function that takes any number of positional arguments and print them back to the user telling them
which ones are args and which ones are kwargs
'''
# Kwargs must be last here or there will be an error

print("Exercise 4.2")

print()


# Review
'''
3) Print the following using the format method and ** unpacking
'''

country = {
	"name": "Germany",
	"population": "83 million",
	"capital": "Berlin",
	"currency": "Euro"
}

'''
4)
Using * unpacking and range, print the number 1 to 20 separated by commas
'''

print("Exercise 4.4")

print()
'''
5)
Do the same but separate by | 
'''
print("Exercise 4.5")

print()

# Review
# 6 Read and write to a json file

print("Exercise 6.1")





# 7 Use try and except for the following:
# 7a: divide by 0 and divide by a string
# TypeError
# ZeroDivisionError
# 7b: Open a non existing file
# FileNotFoundError

# Review
# 8 Day 20 Exercises
'''
1)
Use map to call the strip method on each string in the following list:
Print each entry on a new line
'''
humpty_dumpty = [
	"  Humpty Dumpty sat on a wall,  ",
	"Humpty Dumpty had a great fall;     ",
	"  All the king's horses and all the king's men ",
	"    Couldn't put Humpty together again."
]

print("Exercise8.1")

print()

'''
2)
Use a list comprehension with a filtering condition so that only 
names with fewer than 8 characters end up in the new list.
Make sure that every name in the new list is in title case.
'''

print("Exercise 8.2")

print()

'''
3) Use filter to remove all negative numbers from the 
following range: range(-5, 11).
 Print the remaining numbers to the console.
'''

print("Exersice 8.3")

print()

# 9 Use operator and Map to add number as pairs from:
# ie add 1 + 2, 3 + 4, 5 + 6

print("Exercise 9")

print()

# 10
# Grab the first word in our words list that begins with "a"
from operator import methodcaller
words = ["anaconda", "peach", "gravity", "cattle", "anime", "addition"]

print("Exercise 10.1")


print()

numbers = [(23, 3, 56), (98, 1034, 54), (254, 344, 5), (45, 2), (122, 63, 74)]
# Use the map function to find the sum of the numbers in each tuple.
# Use manual iteration to print the first 2 results

print("Exercise 10.2")

print()

'''
Imagine you have 3 employees and it's been agreed that the employees 
will take it in turns to lock up the shop at night. 
This means that for employees A, B, and C, employee A will close the shop on day 1, 
then B will close the shop on day 2, C will close the shop on day 3, 
and then we start the cycle again with employee A.

Write a program to create a schedule that lists which of your employees 
will lock up the shop on a given day over a 30 day period. 
You should list the day number, the employee name, and the day of the week. 
You can choose any employee to lock the shop on day 1, and you 
can also choose which day of the week day 1 corresponds to.
'''
# Use the cycle function of itertools we never went over

print("Exercise 10.3")

print()

#11 Write a generator that generates odd numbers in a range

print("Exericse 11.1")

print()

# Rewrite with generator
names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]

print("Exercise 11.2")

print()

