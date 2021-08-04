

numbers = [1, 2, 3, 4, 5]
iter_numbers = iter(numbers)
print(*iter_numbers)

# This is what python does automatically
# To verbose
numbers = [1, 2, 3, 4, 5]
iter_numbers = iter(numbers)

while True:
    try:
        number = next(iter_numbers)
    except StopIteration:
        break
    else:
        print(number)


# Generators
# Syntax
# Looks like a normal function but replace return with yield

def first_hundred():
    for number in range(1,101):
        yield number

g = first_hundred()
print(*g)


# g is in iterator

"""
Every time you call the generator it restarts
Prinint n3xt 4 times will just print 1 4 times
"""

"""
Back to yield and why it is different from return
Yield creates a pause in the except
The value of yield is what we want to return before the pause
Next will work if you use yield
"""

def first_hundred():
	print("First value requested\n")

	for number in range(1, 101):
		print("Starting new iteration")
		yield number
		print("Ending this iteration\n")

g = first_hundred()

print(next(g))
print(next(g))

"""
Generator Expressions
Very Similar to the other comprehension
"""

squares = (number ** 2 for number in range(1, 11))

print(next(squares))
print(*squares)

# Write a generator that generates odd numbers in a range

odds = (number for number in range(1,11) if number % 2 != 0)
print(*odds)

# Rewrite with generator

names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]


proper_names = (name.strip().title() for name in names)
print(*proper_names)