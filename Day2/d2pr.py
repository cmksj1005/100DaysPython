print("Welcome to the tip calculator.")

bill = input("What was the total bill? $")
perc = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

output = (bill * (perc / 100)) / people
output = round(output, 2)

print("Each person should pay: $" + output)
