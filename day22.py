'''
Iterable:
- any value we can iterate over
- strings, lists,tuples, dictionaries, sets, enumerate, map, filter are all iterables

Iterators give us the value from iterbles
'''
import itertools

'''
Iterables are lazy types, meaning it only takes up memory when called
Iterator values are consumes
'''

'''
Manual iterators with the next function
Request the value of iterators one at a time without a for loop
'''

# Grab the first word in our words list that begins with "a"
from operator import methodcaller
words = ["anaconda", "peach", "gravity", "cattle", "anime", "addition"]
a_words = filter(methodcaller("startswith", "a"), words)

print(next(a_words))
# Call it again wi will get the next a word
print(next(a_words))

'''
What would be the pratical real world use of this?
'''
# Can be usefule in working with large files
# instead of dumoing in all of the file at once,
# We can dump in one at a time
# Open is already an iterator

# The same iris file, we use next to get just the first line then
# Use the standard for loop and do the same thing for the rest

irises = []
with open("iris.csv", "r") as iris_file:
    headers = next(iris_file).strip().split(",")

    for row in iris_file:
        irises = row.strip().split(",")
        iris_dict = dict(zip(headers,irises))
        irises.append(iris_dict)

'''
Stop iteration exception
'''

# Raised when an iterator has run out of values to iterate
# To avoid it use try, except

numbers = [(23, 3, 56), (98, 1034, 54), (254, 344, 5), (45, 2), (122, 63, 74)]
# Use the map function to find the sum of the numbers in each tuple.
# Use manual iteration to print the first 2 results

def totals(numbers):
    return sum(numbers)

sums = map(totals, numbers)

print(next(sums))
print(next(sums))

# Review
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
# USe the cycle function of itertools we never went over

employees = itertools.cycle(["A","B", "C"])
days = itertools.cycle(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

for day_number in range(1, 31):
	print(f"Day {day_number} ({next(days)}): {next(employees)} closes.")
