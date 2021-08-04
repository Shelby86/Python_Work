import itertools
from operator import methodcaller

# Proboaly a good idea to remember the operator method caller and google the details

words = ["anaconda", "peach", "gravity", "cattle", "anime", "addition"]
a_words = filter(methodcaller("startswith", "a"), words)
print(next(a_words))
print(next(a_words))

numbers = [(23, 3, 56), (98, 1034, 54), (254, 344, 5), (45, 2), (122, 63, 74)]

totals = map(lambda number: sum(number), numbers)
print(next(totals))
print(next(totals))

employees = ["John", "Jonna", "Steve"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


employees = itertools.cycle(employees)
days = itertools.cycle(days)

for number in range(1,21):
    print(f"{next(employees)} closes on {next(days)}")


