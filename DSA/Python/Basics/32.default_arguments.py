import time

# Default Arguments = A default value for certain parameters.
#                     A default is used when that argument is omitted.
#                     They make your functions more flexible, reduce the number of arguments needed,
#                     and prevent you from having to write multiple similar functions.
#                     1. Positional, 2. DEFAULT, 3. Keyword, 4. Arbritrary 

print("--- ⚙️ Default Arguments ⚙️ ---")

# --- 1. Basic Example (Calculating Price) ---
print("\n--- 1. Basic Example ---")

# 'discount' and 'tax' are default arguments.
# ⚠️ RULE: Default arguments MUST follow non-default arguments in the parameters list.
# For example: def net_price(discount=0, list_price) would cause a SyntaxError!

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

# We only provide the list_price. It uses the default discount (0) and default tax (0.05)
print(f"Price with default tax: ${net_price(500):.2f}") 

# We provide list_price and discount. It uses the default tax (0.05)
print(f"Price with 10% discount: ${net_price(500, 0.10):.2f}") 

# We provide all three arguments, overriding all defaults
print(f"Price with 10% discount, NO tax: ${net_price(500, 0.10, 0):.2f}") 


# --- 2. Advanced Example (Timer) ---
print("\n--- 2. Timer Example ---")

# Let's create a counting function.
# By default, it will start from 0. The user MUST provide the 'end' number.
def count(end, start=0):
    for x in range(start, end + 1):
        print(x, end=" ")
        time.sleep(0.1) # Pauses execution for 0.1 seconds to simulate a timer
    print("\nDONE!")

print("Counting to 5 (starting from default 0):")
count(5)

print("\nCounting from 15 to 20 (overriding the default start):")
count(20, 15)


# --- ⏱️ Time Complexities (Average Case) ---
def do_nothing(arg="default"): pass
do_nothing()               # Function Call with Default Argument - O(1)
