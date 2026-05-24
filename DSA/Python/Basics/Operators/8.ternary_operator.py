# Conditional Expressions (Ternary Operator)
# - A one-line shortcut for the if-else statement.
# - Syntax: X if condition else Y
# - Very useful for quickly assigning a value to a variable based on a simple condition!

print("--- ❓ Conditional Expressions ❓ ---")

# --- 1. Basic Example (Positive/Negative) ---
print("\n--- 1. Basic Value Assignment ---")
num = 5
print(f"Number is {num}")

# The standard if-else way:
# if num > 0:
#     result = "Positive"
# else:
#     result = "Negative"

# The Ternary shortcut:
result = "Positive" if num > 0 else "Negative"
print(f"Result: {result}")


# --- 2. Even or Odd ---
print("\n--- 2. Even or Odd ---")
num = 10
# Reads like English: "Assign 'Even' IF num % 2 == 0 ELSE assign 'Odd'"
is_even = "Even" if num % 2 == 0 else "Odd"
print(f"The number {num} is {is_even}")


# --- 3. Max of Two Numbers ---
print("\n--- 3. Max of Two Numbers ---")
a = 6
b = 7
max_num = a if a > b else b
print(f"Between {a} and {b}, the max is {max_num}")


# --- 4. User Status based on a Boolean ---
print("\n--- 4. User Status ---")
is_vip = True
status = "VIP Member" if is_vip else "Standard Member"
print(f"Account Status: {status}")


# --- 5. Age Check ---
print("\n--- 5. Age Check ---")
age = 21
message = "You are an adult" if age >= 18 else "You are a minor"
print(f"Age {age} -> {message}")
