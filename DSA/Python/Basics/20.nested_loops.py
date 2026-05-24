# Nested Loops
# - A loop within another loop (outer, inner).
# - The "inner loop" will finish ALL of its iterations before 
#   finishing one iteration of the "outer loop".

print("--- 🪆 Nested Loops 🪆 ---")

# --- 1. Basic Nested Loop Concept ---
print("\n--- 1. The Concept ---")

# The outer loop will run exactly 3 times
for x in range(3):
    
    # For EACH time the outer loop runs, the inner loop runs 1 through 9
    for y in range(1, 10):
        # We use end="" so the numbers print side-by-side on the same line
        print(y, end="")
        
    # This empty print() is inside the outer loop, but outside the inner loop.
    # It simply drops the cursor down to the next line when the inner loop finishes!
    print()


# --- 2. Interactive Rectangle/Grid Generator ---
# Nested loops are most commonly used for dealing with 2D grids or coordinates
print("\n--- 2. Rectangle Generator ---")

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a single symbol to use (e.g. #, *, @): ")

print("\nHere is your shape:\n")

# The outer loop handles building the rows (moving downwards)
for i in range(rows):
    
    # The inner loop handles building the columns (moving left to right)
    for j in range(columns):
        print(symbol, end=" ")
        
    # Drop down to the next line after the row of columns is finished
    print()
