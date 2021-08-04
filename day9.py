#1
main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

# Write a for loop that uses destructuring so that you can print each tuple in the following format
# BoJack Horseman is a horse voiced by Will Arnet.

for name, actor, species in main_characters:
    print(f"{name} is a {species} voiced by {actor}.")

# 2)Unpack the following tuple into 4 variables:
student = ("John Smith", 11743, ("Computer Science", "Mathematics"))
# The data represents a student's name, their student id number,
# and their major and minor disciplines in that order.

name, id_number, (major,minor) = student
print(name, id_number, major, minor)

names = ["Paul", "Steve", "Larry", "Joe"]
for index, name in enumerate(names, start=1):
    print(f"{index}) {name}")