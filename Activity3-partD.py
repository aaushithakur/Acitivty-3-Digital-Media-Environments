# Complete the TODOs using the Python concepts introduced in class.
# Run this file to check your result.  

# DG8002 - F26 - Activity 3
# Author Name: Aaushi Thakur
# Date: 29th September 2026

# SCENARIO
# Calculate SIMPLE interest on an investment. This exercise does not use
# compound interest, powers, or square roots.
# Formula: interest = principal * rate * time
# Start with:
# Principal (starting investment): $1,000.00
# Annual interest rate: 5% (store this as 0.05)
# Time: 3 years

# TODO 1: Create variables for the principal, annual interest rate, and time.

# TODO 2: Calculate the interest earned using the formula above.

# TODO 3: Calculate the final investment value (principal + interest).

# TODO 4: Print the starting investment, interest earned, and final value.
# Optional: Format money to two decimal places.

# CHECK YOUR WORK
# Interest earned: $150.00
# Final value: $1,150.00
# Calculate simple interest using example inputs.
principal = 1000.00
annual_interest_percentage = 5
time_years = 3

annual_interest_rate = annual_interest_percentage / 100
interest_earned = principal * annual_interest_rate * time_years
final_balance = principal + interest_earned

print(f"Initial investment: ${principal:.2f}")
print(f"Annual interest rate: {annual_interest_percentage}%")
print(f"Investment period: {time_years} years")
print(f"Interest accumulated: ${interest_earned:.2f}")
print(f"Final investment balance: ${final_balance:.2f}")