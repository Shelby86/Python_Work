#2
word = "python"

for letter in word:
    if letter == 'o':
        continue
    else:
        print(letter)

# 3
# Create a program that prints every odd number between 1 and 100.

for number in range(1,101):
    if number % 2 == 0:
        continue
    else:
        print(number)

for number in range(1,101):
    if number % 2 != 0:
        print(number)

#1 While loop with prompts
magic_number = 73
while True:
    user_number = int(input("Please enter a number between 1 and 100: "))
    if user_number == magic_number:
        print("You have guessed the magic number")
        break
    elif user_number < magic_number:
        print("Guess higher")
    elif user_number > magic_number:
        print("Guess lower")

