'''

Rules:
1) start at the number 1
2) end at 100
3) if a number is divisible by 3, print fizz
4) if a number is divisible by 5 print buzz
5) if a number is divisible by both 3 and 5 print fizz buzz

'''

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)