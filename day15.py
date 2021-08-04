names = ("mary", "Richard", "Noah", "KATE")

names = [name.title() for name in names]
print(names)

ages = (36, 21, 40, 28)

people = [[name.title(), age] for name,age in zip(names,ages)]
print(people)

student_ids = (112343, 134555, 113826, 124888)
names = ("mary", "Richard", "Noah", "KATE")


students = {id: name.title() for id, name in zip(student_ids,names)}
print(students)

# Convert as a comprehension
numbers = [1, 2, 3, 4, 5]
squares = []

for number in numbers:
	squares.append(number ** 2)

numbers_and_squares = [[number, number ** 2] for number in numbers]
print(numbers_and_squares)

# Put in title case

movie = {
	"title": "thor: ragnarok",
	"director": "taika waititi",
	"producer": "kevin feige",
	"production_company": "marvel studios"
}

movie = {keys.title():values.title() for keys, values in movie.items()}
print(movie)
