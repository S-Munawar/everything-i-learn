# Python Calculator Program
# - A simple interactive program that takes an operator and two numbers.
# - Combines user input, type casting, arithmetic, and if statements!

print("--- 🧮 Python Calculator 🧮 ---")

# --- 1. Get User Input ---
# We cast the numbers to floats so the calculator can handle decimals
operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

# --- 2. Calculate based on the Operator ---
# We use an if-elif-else block to figure out which math operation to do
print("\n----------------------------------")

if operator == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {round(result, 3)}")

elif operator == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {round(result, 3)}")

elif operator == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {round(result, 3)}")

elif operator == "/":
    # Nested if statement to prevent division by zero errors!
    if num2 == 0:
        print("Error: You cannot divide by zero!")
    else:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {round(result, 3)}")

else:
    # This runs if the user typed something other than + - * /
    print(f"Error: '{operator}' is not a valid operator.")

print("----------------------------------\n")
