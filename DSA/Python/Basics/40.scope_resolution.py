# Variable Scope and Resolution
# - Variable Scope: Where a variable is visible and accessible.
# - Scope Resolution: The order in which Python searches for a variable name.
# - Rule: L.E.G.B. (Local -> Enclosing -> Global -> Built-in)

print("--- 🔭 Variable Scope (LEGB) 🔭 ---")

# --- 1. Global & Local Scope ---
print("\n--- 1. Global vs Local Scope ---")

# This is a GLOBAL variable. It can be accessed anywhere in this file.
name = "Spongebob (Global)"

def greeting():
    # This is a LOCAL variable. It only exists inside this function.
    # When Python sees 'name', it checks the Local scope first.
    name = "Spongebob (Local)"
    print(f"Inside the function: {name}")

greeting()
print(f"Outside the function : {name}")


# --- 2. Enclosing Scope ---
print("\n--- 2. Enclosing Scope ---")
# This occurs when you have nested functions.

def outer_func():
    # This is an ENCLOSING variable (Local to outer_func, but acts as a Global to inner_func)
    color = "Green (Enclosing)"
    
    def inner_func():
        # This is a LOCAL variable
        # color = "Red (Local)"
        
        # If the local variable is commented out (like it is above), 
        # Python checks the Local scope -> doesn't find it -> checks the Enclosing scope!
        print(f"Inside inner_func: {color}")
        
    inner_func()

outer_func()


# --- 3. Built-in Scope ---
print("\n--- 3. Built-in Scope ---")
# Built-in scope refers to the pre-assigned names in Python (like print, max, min, float, e, etc.)

from math import e

def test_func():
    # e = 2.0  # Local
    pass

# e = 3.0      # Global

# If 'e' isn't defined Locally, in an Enclosing function, or Globally, 
# Python checks the Built-in scope last!
print(f"Value of e (from built-in math module): {e}")


# --- ⏱️ Time Complexities (Average Case) ---
# Variable lookup in Python is heavily optimized using dictionaries (hash tables) under the hood.
# Searching through scopes (Local -> Enclosing -> Global -> Built-in) generally takes O(1) time.

print(name)                # Variable Lookup - O(1)
