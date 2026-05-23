import math

# Arithmetic & Math
# - Basic operators: +, -, *, /, //, %, **
# - Precedence: ()  **  *  /  +  - (PEMDAS)
# - Built-in functions: round(), abs(), pow(), max(), min()
# - The 'math' module provides more advanced mathematical functions.

# --- 1. Basic Arithmetic Operators ---
print("--- 1. Basic Arithmetic Operators ---")
friends = 10
print(f"Starting friends: {friends}")

friends = friends + 1    # Addition
friends = friends - 2    # Subtraction
friends = friends * 3    # Multiplication
friends = friends / 2    # Division (always returns a float)
friends = friends ** 2   # Exponentiation (squared)
remainder = friends % 3  # Modulo (returns the remainder of division)

print(f"Friends calculation result: {friends}")
print(f"Remainder of friends / 3: {remainder}")

# --- Operator Precedence (PEMDAS) ---
print("\n--- Operator Precedence ---")
# 1. Parentheses ()
# 2. Exponents **
# 3. Multiply/Divide * / // %
# 4. Add/Subtract + -
result1 = 3 + 4 * 5
print(f"3 + 4 * 5 = {result1} (Multiplication first)")

result2 = (3 + 4) * 5
print(f"(3 + 4) * 5 = {result2} (Parentheses first)")

# --- 2. Augmented Assignment Operators ---
# A shorter, cleaner way to write math operations
print("\n--- 2. Augmented Assignment Operators ---")
apples = 5
print(f"Starting apples: {apples}")

apples += 2 # Same as: apples = apples + 2
apples -= 1 # Same as: apples = apples - 1
apples *= 3 # Same as: apples = apples * 3
apples /= 2 # Same as: apples = apples / 2
print(f"Apples after augmented operations: {apples}")

# --- 3. Built-in Math Functions ---
# Functions that are always available in Python without needing to import anything
print("\n--- 3. Built-in Math Functions ---")
x = 3.14
y = -4
z = 5

print(f"round({x}) = {round(x, 1)}")               # Rounds to nearest integer
print(f"abs({y}) = {abs(y)}")                   # Absolute value (distance from zero)
print(f"pow(4, 3) = {pow(4, 3)}")               # 4 to the power of 3 (4 * 4 * 4)
print(f"max({x}, {y}, {z}) = {max(x, y, z)}")   # Finds the maximum value
print(f"min({x}, {y}, {z}) = {min(x, y, z)}")   # Finds the minimum value

# --- 4. The 'math' Module ---
# You must write 'import math' at the top of your file to use these!
print("\n--- 4. The 'math' Module ---")
radius = 10.4

print(f"math.pi = {math.pi}")
print(f"math.e = {math.e}")
print(f"math.sqrt(9) = {math.sqrt(9)}")             # Square root
print(f"math.ceil({radius}) = {math.ceil(radius)}") # Rounds UP to nearest integer
print(f"math.floor({radius}) = {math.floor(radius)}")# Rounds DOWN to nearest integer

# Real-world Example: Circumference of a circle (C = 2 * pi * r)
circumference = 2 * math.pi * radius
print(f"\nCircumference of a circle with radius {radius} is: {round(circumference, 2)}")

