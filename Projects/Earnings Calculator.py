# Create a variable called earningsgoal and set it equal to a prompt asking the user how much money they want to save
earningsgoal = int(input("How much money do you want to save in a year? "))

# Create a variable named months and set it equal to a calculation to find out how much they need to save per month
months = round(earningsgoal / 12, 2)

# Create a variable named weeks and set it equal to a calculation to find out how much they need to save per week
weeks = round(earningsgoal / (12 * 4), 2)

# Create a variable named days and set it equal to a calculation to find out how much they need to save per day
days = round(earningsgoal / 365, 2)

# Print the results
print("To save up " + str(earningsgoal) + " dollars in one year, you will need to save " + str(months) + " per month.")
print("To save up " + str(earningsgoal) + " dollars in one year, you will need to save " + str(weeks) + " per week.")
print("To save up " + str(earningsgoal) + " dollars in one year, you will need to save " + str(days) + " per day.")
