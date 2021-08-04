



# Make a Program.
# If someone works over 40 hours, add message they are due overtime
# Add message of the wage
# Overtime = 110% of the standard wage

wage = 10
hours_worked = 50

input("Please enter your wage: ")
input("Please enter the total hours you worked this week: ")

total_regular_pay = wage * hours_worked
overtime_wage = wage * 1.10

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_amount = hours_worked * overtime_wage
    total_pay = total_regular_pay + overtime_amount
    print('You have worked more then 40 hours this week.')
    print(f'You have earned the overtime amount of {overtime_amount}')
    print(f'Your total pay is {total_pay}')
else:
    print(f"You have earned {total_regular_pay}")




