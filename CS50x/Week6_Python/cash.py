from cs50 import get_float

# Prompt
while True:
    change = get_float('Change: ')
    if change >= 0:
        break

# Convert dollars to coins
change = int(change * 100)

# Count coins
coins = 0
coins += int(change / 25)  # Quarters
change %= 25
coins += int(change / 10)  # Dimes
change %= 10
coins += int(change / 5)  # Nickels
change %= 5
coins += change  # Pennies

# Output
print(int(coins))