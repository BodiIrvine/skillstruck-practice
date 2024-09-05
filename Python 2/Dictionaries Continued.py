# Starting dictionary
coins = {
    "pennies": 1,
    "nickels": 5,
    "dimes": 10,
    "quarters": 25,
}

# Adding the key "silver dollar" with an example value (e.g., 100)
coins["silver dollar"] = 100

# Removing the key "pennies" using the pop method
coins.pop("pennies")

# Printing the new dictionary
print(coins)

# Printing the length of the dictionary
print(len(coins))
