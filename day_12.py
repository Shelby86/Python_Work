
def add_number(a,b):
    print(a + b)

def subtract_number(a,b):
    print(a - b)

def divide_number(a,b):
    if b == 0:
        print("You can't divide by 0.")
    else:
        print(a / b)

def multiply_number(a,b):
    print(a * b)


add_number(2,2)

subtract_number(300,100)

divide_number(2,0)
divide_number(10,2)

multiply_number(10,10)

tv_show = {
 	"title": "Breaking Bad",
 	"seasons": 5,
 	"initial_release": 2008
 }

# Print the show info like this
# Breaking Bad (2008) - 5 seasons

tv_show = {
 	"title": "Breaking Bad",
 	"seasons": 5,
 	"initial_release": 2008
 }


def print_show(show):
    print(f"{show['title']} ({show['initial_release']}) - {show['seasons']} seasons ")

print_show(tv_show)

series = [
 	{"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
 	{"title": "Fargo", "seasons": 4, "initial_release": 2014},
 	{"title": "Firefly", "seasons": 1, "initial_release": 2002},
 	{"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
 	{"title": "True Detective", "seasons": 3, "initial_release": 2014},
 	{"title": "Westworld", "seasons": 3, "initial_release": 2016},
 ]

for entry in series:
	print_show(entry)

palindrome1 = "was it a car or a cat I saw” is a palindrome"
palindrome= "Hannah"

# Function to test a palindrome

def is_palindrome(sequence):
	word = sequence.strip().lower()
	reversed_word = reversed(word)

	if list(word) == list(reversed_word):
		print(True)
	else:
		print(False)

is_palindrome(palindrome)
