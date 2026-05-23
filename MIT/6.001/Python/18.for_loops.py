# For Loops
# - A statement that will execute its block of code a limited amount of times.
# - You can iterate over a range, string, sequence, etc.
# - Remember: 
#     "While loop = Unlimited (runs until a condition is false)"
#     "For loop   = Limited (runs a set amount of times)"

print("--- 🔄 For Loops 🔄 ---")

# --- 1. Iterating through a range(stop) ---
# range(5) will count from 0 to 4 (it stops BEFORE 5)
print("\n--- 1. range(stop) ---")
for i in range(5):
    print(i)

# --- 2. Iterating through a range(start, stop) ---
# Starts at 1, stops BEFORE 6
print("\n--- 2. range(start, stop) ---")
for i in range(1, 6):
    print(i)

# --- 3. Iterating through a range(start, stop, step) ---
# The step determines how much to increment by each time
print("\n--- 3. range(start, stop, step) ---")
for i in range(2, 11, 2):
    print(f"Counting by twos: {i}")

# Counting backwards requires a negative step!
print("\n--- 4. Counting Backwards ---")
for i in range(5, 0, -1):
    print(i)
print("BLASTOFF! 🚀")

# --- 5. Iterating through a String ---
# A string is an "iterable", meaning we can loop through it character by character.
print("\n--- 5. Iterating over a String ---")
name = "Bro Code"
for letter in name:
    print(letter)

# --- 6. 'continue' and 'break' in For Loops ---
print("\n--- 6. 'continue' and 'break' ---")
# Skipping the number 13 (Superstition!)
for i in range(1, 16):
    if i == 13:
        continue # Skips 13 and jumps straight to 14
    # The end="" argument prevents print() from starting a new line!
    print(i, end="-") 
print() # Just prints a new line

# Breaking the loop early
for i in range(1, 16):
    if i == 13:
        break # Completely completely stops the loop
    print(i, end="-")
print("\nLoop broken when it hit 13!")
