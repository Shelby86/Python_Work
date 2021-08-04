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

letters = ['j', 'q', 'p', 'r', 'a']

# 2 Return a value from a list

#print(letters[4])

# 3 Return multiple values from a list

#print(letters[0:4])

# 4 Return the last value from a list

#print(letters[-1])

# 5 Add a value to a list

# letters.append('t')
# print(letters)

# 6 Add an item to the second index in a list

# letters.insert(2,'u')
# print(letters)

# 7 Use remove

# letters.remove('j')
# print(letters)

# 8 Use del

# del(numbers[3])
# print(numbers)

# 9 Use pop

# numbers.pop()
# print(numbers)

# 10 Make an empty set

# new_set = set()
# print(type(new_set))

# 11 Print "Momento from the following"

movies = [
    ("Eternal Sunshine of a Spotless Mind", 2004),
    ("Momento", 2000),
    ("Requiem for a Dream", 2000)
]

# print(movies[1][0])

# 12 use len

# print(len(numbers))

# 13 Convert to a list into single and individual strings

# single string
str_of_numbers = str(numbers)
# list of individual string

# str_of_numbers = []
#
# for number in numbers:
#     number = str(number)
#     str_of_numbers.append(number)
#
# print(str_of_numbers)

# 13a For the single string, replace the commas with |

# str_of_numbers = str_of_numbers.replace(","," | ")
# print(str_of_numbers)

# 14 Print the following on 2 lines

"Hop on Pop. by Dr Seuss"
# print("Hop on Pop. \n - by Dr Seuss")

# 15 Unpack into 3 variables:

# movie = ["The Dark Night", "Christophe Nolan", "2008"]
# title, director, year = movie
# print(title)

# Prints <zip object at 0x107d9efc0> and not anything useful
# 16 Pair these
owners = ["Paul", "Andrea", "Frank"]
pets = ["Fluffy", "Bubbles", "Captian Catsworth"]

# for owner, pet in zip(owners,pets):
#     print(f'{owner} owns {pet}')

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

# print(operas["Aida"])

# 19 Add an item to a dictionary

# operas["The Magical Flute"] = "Mozart, Classical"
# print(operas)

# 20 Add multiple items to a dictionary

# operas2 = {
#     "Carmen": "Versimo: Bizet",
#     "Norma": "Bel Canto: Bellini"
# }
#
# operas.update(operas2)
# print(operas)

# 21 Modify a Value in a dictionary

# operas["The Magical Flute"] = "Classical: Mozart"
#
# print(operas)

# 22 Modify multiple values in a dictionary

# 23 Return all keys

# for key in operas.keys():
#     print(key)

# 24 Return all values

# for value in operas.values():
#     print(value)

# 25 Use del

# del(operas["The Ring"])
# print(operas)

# 26 Use pop

# 27 Check to see if a value is in a dictionary

# print("La Sonambula" in operas)

# Use these sets for the following

bundle1 = {"Jet Force Gemini", "Zelda", "Mario"}
bundle2 = {"Zelda", "Animal Crossing", "Mario"}

# 28 Make a set

# 29 Make an empty set


# 30 Add an item to a set

# bundle1.add("Donkey Kong Racing")
# print(bundle1)


# 31 Remove an item to a set

# bundle1.remove("Donkey Kong Racing")
# print(bundle1)

# 32 Print unique values from 2 sets

# print(bundle1.union(bundle2))

# 33 Print only common values from 2 sets

# print(bundle1.intersection(bundle2))


# 35 Remove all common values from 2 sets

# print(bundle1.difference(bundle2))

# 36, Given 2 sets, print all the values in one set except for valuest hat are in the other set

# 37 Check if a value is in a set

# 38 Sort a list
pies = ["cherry", "apple", "coconut cream", "strawberry", "peach"]

# pies.sort()
# print(pies)

# 39 Read a file

# with open("iris.csv", "r")  as file:
#     print(file.read())

# 40 Write to a file

# with open("new_file.txt", "w") as file:
#     file.write("I am the first line")

# 38 Append a file

# with open("new_file.txt", "a") as file:
#     file.write("\nI am the second line")

# 39 Print a csv

# 40 Make a csv a dictionary

with open("iris.csv", "r") as iris_csv:
    irises = iris_csv.readlines()

    headers = irises[0].strip('\n').split(",")

    entries = []

    for iris in irises[1:]:
        iris = iris.strip('\n').split(',')
        entries.append(dict(zip(headers, iris)))

print(entries)

# Review
# 41 Make a dictionary into a csv

with open("back_to_csv.csv", "w") as back_to_csv:
    for iris in entries:
            back_to_csv.write(",".join(iris.values()) + "\n")












