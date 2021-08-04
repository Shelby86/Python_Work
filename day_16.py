numbers = [56, 3, 45, 29, 102, 30, 73]
highest_number = max(numbers)

print(highest_number)


# max and key

'''
- Max does not work for all collection types.
- Does not work on dictionaries
- For dictionaries, max will try to compare the whole dictionary to another dictionary
- For instances like these we need to provide a key argument
- Key does not always mean dictionary key
- Key here tells max what we want to find the max value of
-  We assign the dictionary key of grade_average. It makes logical sense if we want to find the highest grade
'''

# This function will return all the values associated with the key of grade_average
# We pass in the dictionary as a value


students = [
	{"name": "Hannah", "grade_average": 83},
	{"name": "Charlie", "grade_average": 91},
	{"name": "Peter", "grade_average": 85},
	{"name": "Rachel", "grade_average": 79},
	{"name": "Lauren", "grade_average": 92}
]

def get_grade_average(student):
	return student["grade_average"]

valedictorian = max(students, key=get_grade_average)
print(valedictorian)

# sort, max, min can also accept keys

# The get method
# Does something similar

def add(a, b):
	print(a + b)

def subtract(a, b):
	print(a - b)

def multiply(a, b):
	print(a * b)

def divide(a, b):
	if b == 0:
		print("You can't divide by 0!")
	else:
		print(a / b)

operations = {
	"a": add,
	"s": subtract,
	"m": multiply,
	"d": divide
}

selected_option = "a"

operation = operations.get(selected_option)

# if operation:
# 	a = int(input("Please enter a value for a: "))
# 	b = int(input("Please enter a value for b: "))
#
# 	operation(a, b)
# else:
# 	print("Invalid selection")

# lambda

lambda a,b : a + b

# lambda for the grade average

valedictorian = max(students, key=lambda student: student["grade_average"])

print(valedictorian)

# lambda is really only useful in short easy definiations


# Print the names in alphabetical order using whatever method you want

students = [
	{"name": "Hannah", "grade_average": 83},
	{"name": "Charlie", "grade_average": 91},
	{"name": "Peter", "grade_average": 85},
	{"name": "Rachel", "grade_average": 79},
	{"name": "Lauren", "grade_average": 92}
]

students.sort(key=lambda student: student["name"])
print(students)

# Print as a lambda and assign it to a variable named exp

def exponentiate(base, exponent):
	return base ** exponent

exp = lambda base, exponent: base ** exponent

print(exp(2,2))

