"""
Questions

What is a list?

What is the difference between insert and append?

What is the difference between remove and pop?

What is join on a string?

What is split on a string?

Can you add a remove a value from a tuple?

What is the difference between remove, del and pop?

What is the difference between a set and a list?

What is the difference between append and write?

9) What is union?

10) What is intersection?

11) What is difference?

12) What is Symmetric difference?

13) Can we use set operators with other collections?

"""

numbers = [1, 2, 3, 4, 5, 6, 7]
# 1 Make a list

# 2 Return a value from a list

# 3 Return multiple values from a list

# 4 Return the last value from a list

# 5 Add a value to a list

# 6 Add an item to the second index in a list

# 7 Use remove

# 8 Use del

# 9 Use pop


# 11 Print "Momento from the following"

movies = [
    ("Eternal Sunshine of a Spotless Mind", 2004),
    ("Momento", 2000),
    ("Requiem for a Dream", 2000)
]

# 12 use len

# 13 Convert to a list into single and individual strings

numbers = [1,2,3,4,5,6]

# single_string

# 13a For the single string, replace the commas with |

# 14 Print the following on 2 lines

# 15 Unpack into 3 variables:
movie = ["The Dark Night", "Christophe Nolan", "2008"]

# 16 Pair these
owners = ["Paul", "Andrea", "Frank"]
pets = ["Fluffy", "Bubbles", "Captian Catsworth"]

# 17 Print owner owns pet

# Dictionary for the following:

operas = {
    "Aida": "Bel Canto: Verdi",
    "Turnadot": "Versimo: Puccini",
    "Armida": "Bel Canto: Rossini",
    "The Ring": "Romantic, Wagner",
    "Nabucco": "Bel Canto: Verdi"
}

# 18 Return a value from a dictionary

# 19 Add an item to a dictionary

# 20 Add multiple items to a dictionary

other_operas = {
    "The Magical Flute": "Classical: Mozart",
    "La Sonnambula": "Bel Canto: Bellini",
    "Roberto Deveroux": "Bel Canto: Donzinetti"
}

# 21 Modify a Value in a dictionary

# 22 Modify multiple values in a dictionary

# 23 Return all keys

# 24 Return all values

# 26 Use pop

# 27 Check to see if a value is in a dictionary

# Use these sets for the following

n64 = {"Jet Force Gemini", "Zelda", "Mario"}
switch= {"Mario", "Animal Crossing", "Zelda"}

fruits = {"apple", "strawberry", "blueberry", "banana"}

# 29 Make an empty set

# 30 Add an item to a set

# 31 Remove an item to a set

# 32 Print unique values from 2 sets

# 33 Print only common values from 2 sets

# 35 Remove all common values from 2 sets

# 36, Given 2 sets,

# 37 Check if a value is in a set

# 38 Sort a list
pies = ["cherry", "apple", "coconut cream", "strawberry", "peach"]

# 39 Read a file

# 40 Write to a file

# 38 Append a file

# 40 Make a csv into a list of dictionaries

with open("iris.csv", "r") as iris_file:
    irises = iris_file.readlines()
    headers = irises[0].strip().split(",")
    list_of_irises = []

    for iris in irises[1:]:
        iris = iris.strip().split(",")
        iris_dict = dict(zip(headers,iris))
        list_of_irises.append(iris_dict)

    print(list_of_irises)


# 41 Make a list of dictionaries into a csv
# Would be super easy as a json file



    with open("back_to_csv.csv", "w") as file:
        for iris in list_of_irises:
            file.write(",".join(iris.values()) + "\n")

















