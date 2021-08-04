import itertools
import random

"""
How many players are there? 2

Player 1 was dealt: (4, hearts), (4, clubs)
Player 2 was dealt: (9, clubs), (jack, diamonds)

The flop: (jack, clubs), (4, diamonds), (king, spades)
The turn: (8, hearts)
The river: (ace, hearts)
"""

suites = ["hearts", "diamonds", "clubs", "spades"]
characters = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "King", "Queen", "Ace"]

# Reusable Function to generate a random card
def get_card():
    random.shuffle(suites)
    suite = suites[0]
    random.shuffle(characters)
    character = characters[0]
    card = [character, suite]

    return card

number_of_players = 5

for counter, player in enumerate(range(number_of_players)):
    counter +=1
    print(f"Player {counter} was dealt: {get_card()}, {get_card()}")
print(f"The flop: {get_card()}, {get_card()}, {get_card()}")
print(f"The turn: {get_card()}")
print(f"The river: {get_card()}")




