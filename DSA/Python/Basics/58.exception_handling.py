# Exception Handling
# - Exception: An event that interrupts the normal flow of a program (an error).
# - try: Block of code to test for errors while it is being executed.
# - except: Block of code to handle the error if one occurs in the try block.
# - else: Block of code to execute if NO errors were raised.
# - finally: Block of code that ALWAYS executes, regardless of errors (used for cleanup).

print("--- 🚨 Exception Handling 🚨 ---")

# --- 1. Basic Try / Except ---
print("\n--- 1. Basic Try / Except ---")

# Without exception handling, dividing by zero would crash the program.
try:
    print("Attempting to divide 10 by 0...")
    result = 10 / 0
    print("This line will NEVER print because an error occurred above!")
except ZeroDivisionError:
    print("❌ Oops! You tried to divide by zero. That's mathematically illegal!")

print("Program continues running smoothly down here!")


# --- 2. Catching Multiple Specific Exceptions ---
print("\n--- 2. Catching Specific Exceptions ---")

def process_number(index):
    numbers = [10, 20, 30]
    try:
        # We might get an IndexError if index is out of bounds
        selected_number = numbers[index]
        
        # We might get a TypeError if index is not an integer
        result = selected_number / 2
        print(f"Success: {result}")
        
    except IndexError:
        print("❌ Error: You tried to access an index that doesn't exist in the list.")
    except TypeError:
        print("❌ Error: Please provide a valid integer for the index.")
    except Exception as e:
        # This catches ANY other exception we didn't explicitly plan for. 
        # It's good practice to put this at the very bottom as a fallback.
        print(f"❌ An unexpected error occurred: {e}")

process_number(5)       # Triggers IndexError
process_number("two")   # Triggers TypeError
process_number(1)       # Works perfectly


# --- 3. The 'else' and 'finally' Blocks ---
print("\n--- 3. The 'else' and 'finally' Blocks ---")

def divide_safely(a, b):
    try:
        print(f"Attempting: {a} / {b}")
        result = a / b
    except ZeroDivisionError:
        print("❌ Error: Division by zero!")
    except TypeError:
        print("❌ Error: Both arguments must be numbers.")
    else:
        # The 'else' block ONLY runs if NO exceptions occurred in the try block.
        print(f"✅ Success! The result is {result}")
    finally:
        # The 'finally' block ALWAYS runs, regardless of whether an exception occurred or not.
        # It's perfect for cleanup tasks, like closing files or database connections.
        print("🧹 Cleaning up resources...")

divide_safely(10, 2)
print("-" * 20)
divide_safely(10, 0)


# --- 4. Raising Your Own Exceptions ---
print("\n--- 4. Raising Exceptions ---")
# Sometimes you want to trigger an error yourself if a condition isn't met.
# We use the 'raise' keyword for this.

def verify_age(age):
    try:
        if age < 0:
            # We explicitly trigger a ValueError with a custom message
            raise ValueError("Age cannot be a negative number!")
        elif age < 18:
            print("Access denied. You must be 18 or older.")
        else:
            print("Access granted! Welcome.")
    except ValueError as e:
        print(f"❌ Invalid Input: {e}")

verify_age(25)
verify_age(-5)


# --- ⏱️ Time Complexities (Average Case) ---
# Exception handling in Python is generally very fast when no exception occurs.
# However, raising and catching an exception does have a slight performance overhead.

# try/except block (No Exception)   - Overhead             - O(1) Time 
# try/except block (Exception hit)  - Overhead             - O(1) Time (but slightly slower)
