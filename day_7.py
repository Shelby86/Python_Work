# 1
name = "John Brown"
name = name.split()

first_name = name[0]
last_nme = name[1]

print(f"{first_name} {last_nme}")

#2

numbers_list = [1, 2, 3, 4, 5]

str_of_numbers = []
for number in numbers_list:
    str_of_numbers.append(str(number))

print(" | ".join(str_of_numbers))

quotes = [
	"'What a waste my life would be without all the beautiful mistakes I've made.'",
	"'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
	"'The very essence of romance is uncertainty.'",
	"'We are not here to do what has already been done.'"
]
new_quotes = []
for quote in quotes:
    new_quotes.append(quote.strip("'"))
    print(quote)

word = "   Sasquatch   "

word = word.strip()
print(len(word))






