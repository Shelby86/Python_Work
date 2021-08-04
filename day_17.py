'''
1) Create a function that accepts any number of numbers as positional arguments and prints
the sum of those numbers.
 Remember that we can use the sum function to add the values in an iterable.
'''

def add(*numbers):
        print(sum(numbers))


add(3,2,4,5,8)

'''
2) Create a function that accepts any number of positional and keyword arguments, 
and that prints them back to the user. 
Your output should indicate which values were provided as positional arguments, 
and which were provided as keyword arguments.
'''

def print_shit(*args,**kwargs):
    print(f"The arguments are {args}")
    print(f"The keywords are {kwargs}")

print_shit(7,37, 'mittens',color='blue')

'''
3) Print the following dictionary using the format method and ** unpacking.
'''

country = {
 	"name": "Germany",
 	"population": "83 million",
 	"capital": "Berlin",
 	"currency": "Euro"
 }

print("{name}, {population}, {capital}, {currency}".format(**country))




'''
4) Using * unpacking and range, print the numbers 1 to 20, separated by commas. 
You will have to provide an argument for print function's sep parameter for this exercise.
'''

numbers = range(1,21)
print(*numbers, sep=" | ")