# Lists, Sets, and Tuples (Collections)
# - Collection: A single "variable" used to store multiple values.
# - List []: Ordered and mutable. Duplicates are allowed.
# - Set {}: Unordered and mutable (can add/remove). NO duplicates.
# - Tuple (): Ordered and immutable. Duplicates are allowed. Faster than lists.

print("--- 📚 Lists, Sets, and Tuples 📚 ---")

# --- 1. Lists [] ---
# Ordered, changeable (mutable), allows duplicate elements.
# Best for: general-purpose collections where order matters and you might need to add/remove items.
print("\n--- 1. Lists [] ---")
fruits = ["apple", "orange", "banana", "coconut"]
print(f"Original List: {fruits}")

# Accessing elements
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# Modifying lists
fruits[0] = "pineapple"
fruits.append("strawberry") # Add to the end
fruits.insert(1, "kiwi")    # Insert at specific index
fruits.remove("banana")     # Remove specific item
# fruits.pop()              # Removes the last item
# fruits.sort()             # Sorts the list alphabetically
# fruits.reverse()          # Reverses the list
# fruits.clear()            # Removes all elements from the list
# fruits.index("apple")     # Returns the index of the first occurrence of "apple"
# fruits.count("apple")     # Returns the number of occurrences of "apple"
# print(dir(fruits))        # Lists all attributes and methods of the list
# print(help(fruits))       # Shows comprehensive documentation for the list
print(f"Modified List: {fruits}")

# Iterating over a list
print("Fruits in List:")
for fruit in fruits:
    print(f" - {fruit}")

# --- 2. Sets {} ---
# Unordered, unindexed, NO duplicate elements.
# Best for: membership testing and eliminating duplicate entries.
print("\n--- 2. Sets {} ---")
cars = {"BMW", "Audi", "Tesla", "BMW"}
print(f"Original Set: {cars}") # Notice "BMW" only appears once!

# Adding/Removing elements
cars.add("Mercedes")
cars.remove("Audi")
# cars.pop() # Removes a random element, because it's unordered!
# print(dir(cars))        # Lists all attributes and methods of the set
# print(help(cars))       # Shows comprehensive documentation for the set
print(f"Modified Set: {cars}")

# Set operations (useful for mathematical set logic)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"Union (all unique elements): {set1.union(set2)}")
print(f"Intersection (common elements): {set1.intersection(set2)}")
print(f"Difference (in set1 but not set2): {set1.difference(set2)}")

# --- 3. Tuples () ---
# Ordered, unchangeable (immutable), allows duplicate elements.
# Best for: fixed collections of items that shouldn't be modified (faster and safer).
print("\n--- 3. Tuples () ---")
coordinates = (34.0522, -118.2437, 34.0522)
print(f"Original Tuple: {coordinates}")

# Accessing elements (same as lists)
print(f"Latitude: {coordinates[0]}")
print(f"Longitude: {coordinates[1]}")

# You cannot modify a tuple!
# coordinates[0] = 40.7128 # This will raise a TypeError!

# Methods (very few because it's immutable)
print(f"Count of 34.0522: {coordinates.count(34.0522)}")
print(f"Index of -118.2437: {coordinates.index(-118.2437)}")
# print(dir(coordinates))        # Lists all attributes and methods of the tuple
# print(help(coordinates))       # Shows comprehensive documentation for the tuple

print("\n--- 🔍 Summary ---")
print("List  [] : Mutable, ordered, duplicates allowed. Use for general data collections.")
print("Set   {} : Mutable (can add/remove), unordered, NO duplicates. Use for unique items & fast membership tests.")
print("Tuple () : Immutable, ordered, duplicates allowed. Use for fixed data (like coordinates or DB records).")

# --- ⏱️ Time Complexities (Average Case) ---

# --- LISTS ---
my_list = [1, 2, 3]
my_list[0]               # Access - O(1)
my_list.append(4)        # Append - O(1)
my_list.insert(0, 0)     # Insert - O(n)
my_list.pop()            # Pop (last element) - O(1)
my_list.pop(0)           # Pop (specific index) - O(n)
my_list.remove(2)        # Remove (specific value) - O(n)
2 in my_list             # Search / Membership - O(n)
len(my_list)             # Length - O(1)

# --- SETS ---
my_set = {1, 2, 3}
my_set.add(4)            # Add - O(1)
my_set.remove(3)         # Remove - O(1)
my_set.pop()             # Pop (arbitrary element) - O(1)
2 in my_set              # Search / Membership - O(1)
len(my_set)              # Length - O(1)

# --- TUPLES ---
my_tuple = (1, 2, 3)
my_tuple[0]              # Access - O(1)
2 in my_tuple            # Search / Membership - O(n)
len(my_tuple)            # Length - O(1)
