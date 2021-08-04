employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

for employee in employees:
    name, hours, rate = employee
    print(f'{name} is due ${hours * rate} this week.')

# Print who earned above average

totals = []

for employee in employees:
    name, hours, rate = employee
    totals_per_employee = hours * rate
    totals.append(totals_per_employee)
    average = sum(totals) / len(totals)
    if totals_per_employee > average:
        print(f"{name} has earned an above average wage this week.")







