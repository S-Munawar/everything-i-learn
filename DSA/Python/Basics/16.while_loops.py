# While Loops
# - A statement that will execute its block of code AS LONG AS its condition remains True.
# - You can think of it like an "if" statement that repeats.
# - CAUTION: Make sure there is a way for the condition to eventually become False, 
#   otherwise you will create an "Infinite Loop"!

print("--- 🔁 While Loops 🔁 ---")

# --- 1. Basic While Loop (Counter) ---
print("\n--- 1. Basic Counter ---")
count = 1

while count <= 5:
    print(f"Count is: {count}")
    count += 1  # Crucial! We must update the variable so the loop eventually ends

print("Counter loop finished!")


# --- 2. While Loop for User Input ---
# While loops are excellent for repeatedly asking a user for input until it's valid
print("\n--- 2. User Input Loop ---")
name = ""

# len(name) == 0 means the string is empty
while len(name) == 0:
    name = input("Please enter your name: ")

print(f"Hello, {name}!")


# --- 3. The 'break' Keyword ---
# Used to completely exit out of a loop immediately, regardless of the condition.
print("\n--- 3. The 'break' Keyword ---")

while True:  # This would normally be an infinite loop
    response = input("Type 'q' to quit this loop: ")
    if response.lower() == 'q':
        print("Breaking out of the loop!")
        break
    else:
        print("You are stuck in the loop...")


# --- 4. The 'continue' Keyword ---
# Used to skip the rest of the CURRENT iteration and go straight to the next iteration.
print("\n--- 4. The 'continue' Keyword ---")
number = 0

while number < 5:
    number += 1
    if number == 3:
        print("Skipping number 3...")
        continue  # Skips the print statement below for number = 3
    print(f"Current number: {number}")


# --- 5. Logical Operators in While Loops ---
print("\n--- 5. Logical Operators ---")
food = input("Enter a food you like (press 'q' to quit): ")

while not food.lower() == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (press 'q' to quit): ")

print("Goodbye!")
