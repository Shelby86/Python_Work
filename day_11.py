import random

fruits = {"apple", "banana", "blueberry", "cherry", "pineapple", "raspberry", "persimmon"}



pies = {"apple", "cherry", "coconut cream", "blueberry", "lemon meringue"}


#1
games = set()

#2
# Add 3 items to the empty set

games.update(["Jet Force Gemini", "Mario", "Zelda"])
# print(games)

#3
games2 = {"Wario", "Mario", "Animal Crossing"}

#4 Print union, intersection and symetric difference on the sets

print(games.union((games2)))
print(games.intersection(games2))
print(games.symmetric_difference(games2))

#5 Create a sequence of numbers using range, then ask the user to enter a number.
# Inform the user whether or not their number was within the range you specified.
#If you want an extra challenge,
# also tell the user if their number was too high or too low.

value = random.randint(1,51)
print(value)



while True:
    user_guess = int(input("Guess a Number between 1 and 50: "))
    if user_guess < value:
        print("Guess Higher")
    elif user_guess > value:
        print("Guess Lower")
    elif user_guess == value:
        print("Correct!")
        break



