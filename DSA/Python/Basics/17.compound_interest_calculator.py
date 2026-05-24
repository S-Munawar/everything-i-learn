# Compound Interest Calculator
# - An interactive program that calculates compound interest over time.
# - This project combines concepts from while loops (for input validation)
#   and format specifiers (to print money beautifully).
#
# Formula: A = P * (1 + r/100)^t
# A = Final Amount
# P = Initial Principal Balance
# r = Interest Rate (percentage)
# t = Time in Years

print("--- 💸 Compound Interest Calculator 💸 ---")

# 1. Get the Principal Amount
principal = 0
while principal <= 0:
    principal = float(input("Enter the principal amount (must be > 0): $"))
    if principal <= 0:
        print("Principal cannot be less than or equal to zero!")

# 2. Get the Interest Rate
rate = 0
while rate <= 0:
    rate = float(input("Enter the annual interest rate (e.g. 5 for 5%): "))
    if rate <= 0:
        print("Interest rate cannot be less than or equal to zero!")

# 3. Get the Time (Years)
time = 0
while time <= 0:
    time = int(input("Enter the time in years (must be > 0): "))
    if time <= 0:
        print("Time cannot be less than or equal to zero!")

# 4. Calculate the Final Amount
# Using the pow() function from our earlier math lessons!
final_amount = principal * pow((1 + rate / 100), time)

# 5. Display the result using format specifiers
print("\n--- 📊 Results 📊 ---")
print(f"Initial Principal: ${principal:,.2f}")
print(f"Interest Rate:     {rate}%")
print(f"Time:              {time} years")
print(f"Final Balance:     ${final_amount:,.2f}")
