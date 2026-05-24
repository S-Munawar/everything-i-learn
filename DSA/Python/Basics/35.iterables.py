# Iterables
# - An object/collection that can return its elements one at a time.
# - Allows the collection to be iterated over in a loop.
# - Examples: Lists, Tuples, Sets, Dictionaries, Strings.

print("--- 🔄 Iterables 🔄 ---")

# --- 1. Lists ---
print("\n--- 1. Iterating over a List ---")
fruits = ["apple", "orange", "banana", "coconut"]

for fruit in fruits:
    print(fruit, end=" ")
print()


# --- 2. Tuples ---
print("\n--- 2. Iterating over a Tuple ---")
coordinates = (34.0522, -118.2437, 0.0)

for coordinate in coordinates:
    print(coordinate, end=" ")
print()


# --- 3. Sets ---
print("\n--- 3. Iterating over a Set ---")
# Remember: Sets are unordered, so the iteration order will likely be random!
colors = {"red", "green", "blue", "yellow"}

for color in colors:
    print(color, end=" ")
print()


# --- 4. Strings ---
print("\n--- 4. Iterating over a String ---")
name = "Bro Code"

for character in name:
    print(character, end=" ")
print()


# --- 5. Dictionaries ---
print("\n--- 5. Iterating over a Dictionary ---")
my_dict = {"a": 1, "b": 2, "c": 3}

# By default, iterating directly over a dictionary iterates over its KEYS
print("Iterating directly (Keys):")
for key in my_dict:
    print(key, end=" ")
print()

print("\nIterating over Values:")
for value in my_dict.values():
    print(value, end=" ")
print()

print("\nIterating over Items (Key-Value pairs):")
for key, value in my_dict.items():
    print(f"{key} = {value}")


# --- ⏱️ Time Complexities (Average Case) ---
# Iterating over any of these data structures generally takes O(N) time,
# where N is the total number of elements (or characters) within the iterable.

my_list = [1, 2, 3]
for item in my_list:           # Iterate Iterable - O(N)
    pass
