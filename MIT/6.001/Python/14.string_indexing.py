# String Indexing
# - Accessing elements of a sequence using [] (indexing operator)
# - Indexing starts at 0 for the first element.
# - You can also use negative indexing to start from the end (-1 is the last element).
# - Syntax: [start:stop:step]
#   - start: the starting index (inclusive)
#   - stop: the ending index (exclusive)
#   - step: how much to increase the index by (default is 1)

print("--- ✂️ String Indexing & Slicing ✂️ ---")

credit_number = "1234-5678-9012-3456"
print(f"\nOriginal String: '{credit_number}'")

# --- 1. Basic Indexing ---
print("\n--- 1. Basic Indexing ---")
# Positive Indexing
print(f"First character [0]: {credit_number[0]}")
print(f"Second character [1]: {credit_number[1]}")

# Negative Indexing
print(f"Last character [-1]: {credit_number[-1]}")
print(f"Second to last character [-2]: {credit_number[-2]}")

# --- 2. String Slicing [start:stop] ---
# Slicing extracts a portion of a string. The 'stop' index is exclusive.
print("\n--- 2. String Slicing [start:stop] ---")
print(f"First 4 characters [0:4]: {credit_number[0:4]}")

# If you leave out the start index, it assumes 0
print(f"First 4 characters (shorthand) [:4]: {credit_number[:4]}")

# If you leave out the stop index, it goes all the way to the end
print(f"Everything from index 5 to the end [5:]: {credit_number[5:]}")

# Using negative indexing in a slice (e.g. drop the last 4 characters)
print(f"Everything EXCEPT the last 4 characters [:-4]: {credit_number[:-4]}")

# --- 3. Step in Slicing [start:stop:step] ---
print("\n--- 3. Step in Slicing [start:stop:step] ---")
# Extracting every 2nd character
print(f"Every 2nd character [::2]: {credit_number[::2]}")

# Extracting every 3rd character
print(f"Every 3rd character [::3]: {credit_number[::3]}")

# Reversing a string (VERY common trick!)
# A negative step moves backwards through the string
print(f"Reversed string [::-1]: {credit_number[::-1]}")

# --- 4. Combining Start, Stop, and Step ---
print("\n--- 4. Combining Start, Stop, and Step ---")
# For example, get characters from index 5 to 14, stepping by 2
print(f"From index 5 to 14, every 2nd char [5:14:2]: {credit_number[5:14:2]}")

# --- 5. Strings are Immutable ---
print("\n--- 5. Strings are Immutable ---")
# You CANNOT change a character at a specific index like this:
# credit_number[0] = "9"  <-- This will cause a TypeError!

# To "change" a string, you must create a new one using slicing and concatenation
new_credit_number = "9" + credit_number[1:]
print(f"Replacing first digit via slicing: '{new_credit_number}'")
