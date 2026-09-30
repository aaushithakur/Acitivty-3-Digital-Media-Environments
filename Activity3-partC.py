# Complete the TODOs using the Python concepts introduced in class.
# Run this file to check your result.  

# DG8002 - F26 - Activity 3
# Author Name: Aaushi Thakur
# Date: 29th September 2026

# SCENARIO
# A group is splitting a restaurant bill, including a tip.
# For this exercise, use these starting values:
# Meal cost (before tip): $80.00
# Tip rate: 18% (store this as 0.18)
# Number of people: 4
# Ignore taxes for this simplified calculation.

# TODO 1: Create variables for the meal cost, tip rate, and number of people.

# TODO 2: Calculate the dollar amount of the tip.

# TODO 3: Calculate the total bill, including the tip.

# TODO 4: Use an if/else statement to check whether the number of people
# is greater than zero.
#   - If it is, calculate the cost per person and print the tip amount,
#     total bill, and cost per person.
#   - Otherwise, print a helpful message explaining why the bill
#     cannot be split.

# CHECK YOUR WORK
# With the starting values above:
# Tip: $14.40
# Total: $94.40
# Per person: $23.60
# Test again with zero people. Your program should not divide by zero.
# Example inputs: replace with the starter-file values if provided.
meal_cost = 80.00
tip_percentage = 18
number_of_people = 4

tip_amount = meal_cost * (tip_percentage / 100)
total_bill = meal_cost + tip_amount
cost_per_person = total_bill / number_of_people

print(f"Meal cost: ${meal_cost:.2f}")
print(f"Tip ({tip_percentage}%): ${tip_amount:.2f}")
print(f"Total bill including tip: ${total_bill:.2f}")
print(f"Number of people: {number_of_people}")
print(f"Amount each person owes: ${cost_per_person:.2f}")