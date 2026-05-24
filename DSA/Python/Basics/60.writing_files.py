# Writing Files
# - open(): Built-in function used to open a file and return a file object.
# - 'w': Write mode. Overwrites the file if it exists, creates a new one if it doesn't.
# - 'x': Exclusive creation mode. Creates a new file, but fails if the file already exists.
# - 'a': Append mode. Adds new data to the end of the file.
# - with: Statement that automatically handles closing the file after the block executes.

import os

print("--- 📝 Writing Files 📝 ---")

# We'll create a temporary file for our demonstrations
filename = "test_write_output.txt"

# --- 1. Writing to a File ('w' mode) ---
print("\n--- 1. Write Mode ('w') ---")
# 'w' mode opens a file for writing.
# IMPORTANT: If the file already exists, 'w' mode will completely OVERWRITE it.
# If the file doesn't exist, it will create a new one.

text_to_write = "Hello there!\nThis is some text written from Python.\nHave a great day!\n"

with open(filename, 'w') as file:
    file.write(text_to_write)
    print(f"✅ Successfully wrote to '{filename}'.")

# Let's verify it exists!
if os.path.exists(filename):
    print(f"File '{filename}' now exists in the directory.")


# --- 2. Appending to a File ('a' mode) ---
print("\n--- 2. Append Mode ('a') ---")
# 'a' mode opens a file for appending.
# It adds new content to the END of the file without deleting what's already there.

text_to_append = "Oh wait, I forgot to add this extra line!\n"

with open(filename, 'a') as file:
    file.write(text_to_append)
    print(f"✅ Successfully appended to '{filename}'.")


# --- 3. Writing Multiple Lines at Once ---
print("\n--- 3. Writing Multiple Lines ---")

# You can use writelines() to write a list of strings to a file.
# Note: writelines() does NOT automatically add newline characters (\n), 
# you have to include them in your strings.

shopping_list = ["\n--- Shopping List ---\n", "1. Apples\n", "2. Bananas\n", "3. Milk\n"]

with open(filename, 'a') as file:
    file.writelines(shopping_list)
    print("✅ Successfully appended the shopping list.")


print(f"\n(Check the generated '{filename}' file to see the final result!)")

# --- ⏱️ Time Complexities (Average Case) ---
# File I/O operations are generally bounded by disk speed, not CPU time.
# O(N) where N is the amount of data being written, but we usually abstract 
# single write operations as O(1) in the context of program logic.

# file.write()      - System I/O - O(N) Time (N = bytes written)
# file.writelines() - System I/O - O(N) Time (N = bytes written)
