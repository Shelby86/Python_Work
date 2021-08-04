'''
Calculate the average budget of all movies in the data set.
Print out every movie that has a budget higher than the average you calculated.
You should also print out how much higher than the average the movie's budget was.
Print out how many movies spent more than the average you calculated.
'''

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

budgets = []

expensive_movies = []

for movie in movies:
    title, budget = movie
    budgets.append(budget)
    avergae = sum(budgets) / len(movies)
    if budget > avergae:
        print(f"{title} has a higher then average budget.")
        print(f"{title} budget was higher then average by {budget - avergae}.")
        expensive_movies.append(title)
        print(f"There are {len(expensive_movies)} movies that had a higher then average budget.")






