''''
The algorithm:

1) Remove the rightmost digit from the card number.
This number is called the checking digit, and it will be excluded from most of our calculations.
2) Reverse the order of the remaining digits.
3) For this sequence of reversed digits,
take the digits at each of the even indices (0, 2, 4, 6, etc.) and multiply by 2.
If any of the results are greater than 9, subtract 9 from those numbers.
4) Add together all of the results and add the checking digit.
5) If the result is divisible by 10, the number is a valid card number. If it's not, the card number is not valid.

'''
valid_card_number = '5893804115457289'

# Would be better to convert the valid card number into a list of int
numbers = []
for char in valid_card_number:
    numbers.append(int(char))

check_digit = numbers.pop(0)
numbers.reverse()

processed_digits = []

for index, digit in enumerate(numbers):
	if index % 2 == 0:
		doubled_digit = int(digit) * 2

		# Subtract 9 from any results that are greater than 9
		if doubled_digit > 9:
			doubled_digit = doubled_digit - 9

		processed_digits.append(doubled_digit)
	else:
		processed_digits.append(int(digit))

total = int(check_digit) + sum(processed_digits)







