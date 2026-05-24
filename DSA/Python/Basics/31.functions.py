# Functions
# - A block of reusable code that only runs when it is called.
# - Helps to keep code DRY (Don't Repeat Yourself) and highly organized.
# - You define a function using the 'def' keyword.

print("--- ⚙️ Python Functions ⚙️ ---")

# --- 1. Basic Function ---
print("\n--- 1. Basic Function ---")

# Definition
def greet():
    print("Hello! Welcome to the functions lesson!")

# The code inside the function doesn't execute until you "call" or "invoke" it.
greet()
greet() # We can call it as many times as we want!

# --- 2. Arguments and Parameters ---
print("\n--- 2. Arguments & Parameters ---")
# Parameters = The variables listed inside the parentheses in the function definition.
# Arguments  = The actual values sent to the function when it is called.

def greet_user(first_name, last_name): # <- Parameters
    print(f"Hello there, {first_name} {last_name}!")

greet_user("Bro", "Code")              # <- Arguments
greet_user("SpongeBob", "SquarePants")

# --- 3. The Return Statement ---
print("\n--- 3. Return Statement ---")
# Functions can send values/objects back to the caller using 'return'.

def add(x, y):
    result = x + y
    return result
    # Note: As soon as 'return' is executed, the function ends immediately.
    # Any code written below 'return' inside the function will NOT run.

sum_result = add(5, 3)
print(f"The sum of 5 and 3 is: {sum_result}")

# A more concise way to write it:
def multiply(x, y):
    return x * y

print(f"The product of 10 and 4 is: {multiply(10, 4)}")

# --- 4. Side Effects vs Return ---
print("\n--- 4. Side Effects vs Return ---")
# If a function doesn't explicitly return a value, it returns 'None' by default.
# It might still DO something (a "side effect"), like printing to the console or modifying a list.

def print_sum(x, y):
    print(f"(Side Effect) The sum is: {x + y}")
    # No return statement here!

# Calling the function executes its side effect (printing)
returned_value = print_sum(5, 3) 

# But because it didn't return anything, the variable stores None!
print(f"The actual returned value stored in the variable is: {returned_value}")

# --- 5. Returning Multiple Values ---
print("\n--- 5. Returning Multiple Values ---")
# Python functions can return multiple values simultaneously by separating them with commas.
# Under the hood, Python packages them into a Tuple!

def get_user_info():
    name = "Alice"
    age = 25
    is_admin = True
    return name, age, is_admin # Returns a tuple: ("Alice", 25, True)

# You can unpack the tuple immediately into separate variables:
user_name, user_age, user_status = get_user_info()

print(f"Name: {user_name}")
print(f"Age: {user_age}")
print(f"Is Admin?: {user_status}")

# --- ⏱️ Time Complexities (Average Case) ---
def do_nothing(): pass
do_nothing()               # Function Call - O(1) (Executing the jump to the code block)
# return x                 # Return Statement - O(1)
