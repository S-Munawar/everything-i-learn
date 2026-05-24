# Reading Files
# - open(): Built-in function used to open a file. Default mode is 'r' (read).
# - 'r': Read mode. Opens a file for reading, throws an error if the file doesn't exist.
# - .read(): Reads the entire file content into a single string.
# - .readline(): Reads a single line from the file.
# - .readlines(): Reads all lines into a list of strings.

import os

print("--- 📖 Reading Files 📖 ---")

# Let's use the file we created in the previous lesson!
# If you skipped it, we'll quickly create it here just in case.
filename = "test_write_output.txt"

if not os.path.exists(filename):
    with open(filename, 'w') as file:
        file.write("Hello there!\nThis is a test file.\nIt has multiple lines.\n")

# --- 1. Reading the Entire File ---
print("\n--- 1. Reading the Entire File (.read) ---")

# It's good practice to use try/except block to catch FileNotFoundError!
try:
    with open(filename, 'r') as file:
        # .read() loads the entire file's content into memory at once
        content = file.read()
        print(content)
except FileNotFoundError:
    print("❌ That file was not found :(")


# --- 2. Reading Line by Line (for loop) ---
print("\n--- 2. Iterating Line by Line ---")
# Reading the entire file at once is bad if the file is massive (like a 10GB log file).
# Iterating over the file object reads one line at a time memory-efficiently.

try:
    with open(filename, 'r') as file:
        for line in file:
            # We use end="" because each line already has a hidden \n character at the end!
            print(line, end="")
except FileNotFoundError:
    print("❌ That file was not found :(")


# --- 3. Reading into a List ---
print("\n\n--- 3. Reading into a List (.readlines) ---")

try:
    with open(filename, 'r') as file:
        # .readlines() returns a list where each element is a line from the file.
        lines_list = file.readlines()
        print(f"Total lines: {len(lines_list)}")
        print(f"Second line: {lines_list[1].strip()}") # .strip() removes the trailing \n
except FileNotFoundError:
    print("❌ That file was not found :(")


# --- ⏱️ Time Complexities (Average Case) ---
# file.read()       - System I/O - O(N) Time (N = bytes read)
# file.readline()   - System I/O - O(L) Time (L = length of the line)
# file.readlines()  - System I/O - O(N) Time (N = total bytes read into list)
