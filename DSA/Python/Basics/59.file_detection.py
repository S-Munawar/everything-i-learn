# File Detection
# - os.path.exists(): Checks if a file or directory exists at a given path.
# - os.path.isfile(): Checks specifically if the given path is a file.
# - os.path.isdir(): Checks specifically if the given path is a directory (folder).

import os

print("--- 📁 File Detection 📁 ---")

# We'll use the path of THIS current script to test with, and a fake path.
current_script = __file__ 
current_dir = os.path.dirname(os.path.abspath(__file__))
fake_path = "some_random_nonexistent_file.txt"

# --- 1. Checking if a path exists ---
print("\n--- 1. Checking Path Existence ---")

# os.path.exists() checks if a file OR directory exists at the given path
if os.path.exists(current_script):
    print(f"✅ It exists! Found: {os.path.basename(current_script)}")
else:
    print("❌ That location doesn't exist.")

if os.path.exists(fake_path):
    print(f"✅ It exists! Found: {fake_path}")
else:
    print(f"❌ '{fake_path}' does not exist.")


# --- 2. Differentiating Files and Directories ---
print("\n--- 2. Is it a File or a Directory? ---")

# os.path.isfile() checks if the path points specifically to a FILE
print(f"Is '{os.path.basename(current_script)}' a file?")
if os.path.isfile(current_script):
    print("➡️ Yes, it's a file! 📄")
else:
    print("➡️ No, it's not a file.")

# os.path.isdir() checks if the path points specifically to a DIRECTORY (folder)
print(f"\nIs '{os.path.basename(current_dir)}' a directory?")
if os.path.isdir(current_dir):
    print("➡️ Yes, it's a directory! 📁")
else:
    print("➡️ No, it's not a directory.")


# --- 3. Getting Absolute Paths ---
print("\n--- 3. Getting Absolute Paths ---")

# os.path.abspath() converts a relative path into an absolute, full path from the system root.
# This is useful when you only have a relative path but need the full location.
relative_path = "example.txt"
absolute_path = os.path.abspath(relative_path)
print(f"Relative Path : {relative_path}")
print(f"Absolute Path : {absolute_path}")


# --- ⏱️ Time Complexities (Average Case) ---
# Checking file attributes generally interacts directly with the OS filesystem.

# os.path.exists()   - OS System Call - O(1) Time 
# os.path.isfile()   - OS System Call - O(1) Time
# os.path.isdir()    - OS System Call - O(1) Time
