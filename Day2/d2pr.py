print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
perc = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = float(input("How many people to split the bill? "))

tax = bill * (perc / 100)

each = (bill + tax) / people
each = round(each, 2)

print(f"Each person should pay: ${each}")
