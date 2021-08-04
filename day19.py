import math

try:
	number = int("f")
except ValueError:
	print("You didn't enter a valid integer!")

def average(numbers):
	mean = math.fsum(numbers) / len(numbers)
	print(mean)

numbers = {1, 2, 3, 4, 5, 6, 7}
not_numbers = ["blue", "banana", "strawberry", "bal"]

def average(numbers):
	try:
		mean = math.fsum(numbers) / len(numbers)
		print(mean)
	except ZeroDivisionError:
		print(0)
	except TypeError:
		print("You provided invalid values!")

average(not_numbers)

def average(numbers):
	try:
		mean = math.fsum(numbers) / len(numbers)
		print(mean)
	except (ZeroDivisionError, TypeError):
		print("An average cannot be calculated for the values you provided.")


'''
1) Create a short program that prompts the user for a list of grades 
separated by commas. Split the string into individual grades and use a 
 list comprehension to convert each string to an integer. 
 You should use a try statement to inform the user when the 
 values they entered cannot be converted.
'''

strs = ["blue", "2", 4]

def convert_list_of_strings_into_ints(a_list):
    for item in a_list:
        try:
            print(int(item))
        except ValueError:
            print("All values must be numbers")

convert_list_of_strings_into_ints(strs)


try:
    with open("not_realFile.txt", "r") as file:
        file.read()
except FileNotFoundError:
    print("There is no file by that name")