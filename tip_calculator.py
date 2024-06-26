# Welcome!
print("Welcome to the tip calculator!")

# Tip Calculator - Bill
bill = float(input("What was the total bill? $"))

# Tip Calculator - Tip
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# Tip Calculator - People
people = int(input("How many people to split the bill? "))

# Tip Calculator - Bill + tip
print("Each people would pay: $", round(bill * (1 + tip / 100) / people, 2))
