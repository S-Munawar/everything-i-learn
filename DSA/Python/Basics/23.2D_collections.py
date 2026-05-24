# 2D Collections
# - A list of lists, tuple of tuples, or set of sets.
# - They are often used to represent grids, matrices, or tables.

print("--- 📚 2D Collections 📚 ---")

# --- 1. 2D Lists (Lists of Lists) ---
print("\n--- 1. 2D Lists ---")

fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

# Creating a 2D list by grouping existing lists
groceries = [fruits, vegetables, meats]

print("Groceries 2D List:")
print(groceries)

print("\nAccessing Elements:")
# To access an element, we need two indices: [row][column]
print(f"First list (fruits): {groceries[0]}")
print(f"First item of first list (apple): {groceries[0][0]}")
print(f"Third item of second list (potatoes): {groceries[1][2]}")

print("\nIterating through a 2D list:")
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

# --- 2. 2D Tuples (Tuples of Tuples) ---
# Immutable grids, like a number pad or a coordinate system.
print("\n--- 2. 2D Tuples ---")

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

print("Number Pad:")
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

print(f"\nAccessing row 2, column 3 (6): {num_pad[1][2]}")

# --- 3. 2D Sets (Sets of Tuples) ---
# Sets cannot contain mutable items like lists or other sets, 
# so a "2D set" is typically a set of tuples.
print("\n--- 3. 2D Sets (Set of Tuples) ---")

coordinates = {
    (0, 0),
    (10, 20),
    (5, 5)
}

print("Set of Coordinates:")
for coord in coordinates:
    print(coord)


print("\n--- 🔍 Summary ---")
print("2D collections are just collections nested inside another collection.")
print("Access elements using double index syntax: collection[outer_index][inner_index].")
print("Nested loops are required to iterate through all individual elements.")

# --- ⏱️ Time Complexities (Average Case) ---
# 2D collections inherit their inner elements' complexities but multiplied by dimensions.

matrix = [[1, 2], [3, 4]]

# Accessing a specific element
matrix[1][0]                  # Access - O(1) + O(1) = O(1)

# Iterating through a 2D collection
for row in matrix:            # Outer loop - O(R) where R is number of rows
    for item in row:          # Inner loop - O(C) where C is number of columns
        pass                  # Total Iteration - O(R * C) or O(N) where N is total elements
