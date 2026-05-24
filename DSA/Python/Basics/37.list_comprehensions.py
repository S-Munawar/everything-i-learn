# List Comprehension
# - A concise, elegant way to create lists in Python.
# - Often more readable and slightly faster than traditional loops.
# - Syntax: [expression for item in iterable if condition]

print("--- 📝 List Comprehensions 📝 ---")

# --- 1. The "Normal" Way vs The "Comprehension" Way ---
print("\n--- 1. Creating a List of Squares ---")

# The Normal Way (using a standard for loop):
squares_loop = []
for i in range(1, 11):
    squares_loop.append(i * i)
print(f"Normal loop   : {squares_loop}")

# The Comprehension Way:
# [expression   for item in iterable]
squares_comp = [i * i for i in range(1, 11)]
print(f"Comprehension : {squares_comp}")


# --- 2. Filtering with 'if' Statements ---
print("\n--- 2. Filtering (Even Numbers) ---")
# Let's say we only want the squares that are EVEN numbers.

# Normal Way:
evens_loop = []
for i in range(1, 11):
    if i % 2 == 0:
        evens_loop.append(i * i)
print(f"Normal loop   : {evens_loop}")

# Comprehension Way:
# [expression   for item in iterable  if condition]
evens_comp = [i * i for i in range(1, 11) if i % 2 == 0]
print(f"Comprehension : {evens_comp}")


# --- 3. Working with Strings ---
print("\n--- 3. Working with Strings ---")
fruits = ["apple", "orange", "banana", "coconut", "apricot"]
print(f"Original list: {fruits}")

# Let's create a new list where every fruit is UPPERCASE.
# Note: 'fruit.upper()' is our expression!
uppercase_fruits = [fruit.upper() for fruit in fruits]
print(f"\nUppercase fruits: {uppercase_fruits}")

# Let's filter out only the fruits that start with 'a' or 'o'.
# Note: 'fruit[0]' grabs the first letter of the string.
vowel_fruits = [fruit for fruit in fruits if fruit[0] in "ao"]
print(f"Fruits starting with 'a' or 'o': {vowel_fruits}")


# --- ⏱️ Time Complexities (Average Case) ---
# List comprehensions still iterate through the entire sequence under the hood.
# They are slightly faster than equivalent for-loops because they are optimized in C,
# but the theoretical time complexity remains the same!

[i * i for i in range(1, 10)]      # List Comprehension - O(N) (Iterates through N items)
