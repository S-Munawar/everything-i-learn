# Modules
# - A file containing Python code. May contain functions, classes, etc.
# - Used with modular programming, which is to separate a program into parts.

print("--- 📦 Python Modules 📦 ---")

# --- 1. Importing standard modules ---
print("\n--- 1. Standard Imports ---")
# 'math' is a built-in standard Python module
import math
print(f"Value of Pi: {math.pi}")

# --- 2. Using an alias ---
print("\n--- 2. Aliases ---")
# You can give modules a nickname so you don't have to type out their full name every time.
import math as m
print(f"Value of e: {m.e}")

# --- 3. Importing specific items ---
print("\n--- 3. Specific Imports ---")
# If you only need one or two things, you can import them directly to avoid typing the module name!
from math import pi, e
print(f"Pi + e = {pi + e}")

# --- 4. Seeing all available modules ---
print("\n--- 4. Help ---")
# You can see all available built-in modules by running:
# help("modules")


# --- 5. Custom Modules ---
print("\n--- 5. Custom Modules ---")
# I created a separate file called 'my_custom_module.py' in this same folder.
# We can import it just like a built-in module!

import my_custom_module

print(my_custom_module.greet("Student"))
print(f"The meaning of life is: {my_custom_module.secret_number}")


# --- ⏱️ Time Complexities (Average Case) ---
# Importing a module is generally O(1) in terms of the main script's runtime, 
# as Python caches the module after the first import.

def do_nothing(): pass
do_nothing()               # Module Import - O(1)
