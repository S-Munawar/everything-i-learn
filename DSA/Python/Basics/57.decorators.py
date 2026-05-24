# Decorators
# - A decorator is a function that takes another function as an argument, adds some kind of functionality to it, and then returns another function.
# - All of this happens WITHOUT altering the source code of the original function.
# - It essentially "wraps" the original function with new behavior!

print("--- 🎀 Decorators 🎀 ---")

# --- 1. The Anatomy of a Decorator ---
print("\n--- 1. Basic Decorator ---")

# This is our decorator function
def add_sprinkles(func):
    
    # This is the "wrapper" function that wraps around the original function.
    # We use *args and **kwargs so it can accept ANY number of arguments 
    # that the original function might require!
    def wrapper(*args, **kwargs):
        print("🎉 [Decorator Action] Adding sprinkles...")
        
        # We execute the original function here and store its return value
        result = func(*args, **kwargs)
        
        print("🎉 [Decorator Action] Sprinkles added!")
        return result
    
    # The decorator returns the wrapper function object (notice no parenthesis!)
    return wrapper

# We apply the decorator using the '@' symbol right above our function.
@add_sprinkles
def bake_cake(flavor):
    print(f"🎂 Baking a delicious {flavor} cake!")
    return f"{flavor} cake"

# Calling the function! It automatically runs through the decorator wrapper.
my_cake = bake_cake("chocolate")
print(f"Returned value: {my_cake}")


# --- 2. A Practical Example: The Timer Decorator ---
print("\n--- 2. Practical Decorator (@timer) ---")
# Decorators are incredibly useful for things like logging, authentication, 
# and performance testing. Let's build a @timer!

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        # Execute the original function
        result = func(*args, **kwargs)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        print(f"⏱️  '{func.__name__}' took {execution_time:.5f} seconds to execute.")
        return result
        
    return wrapper

@timer
def count_to_million():
    print("Counting to a million...")
    for i in range(1000000):
        pass # Do nothing 1,000,000 times
    print("Done!")

@timer
def simulate_network_request():
    print("Fetching data from internet...")
    time.sleep(1.5) # Pauses program for 1.5 seconds
    print("Data received!")

# Testing our timer!
count_to_million()
print("-" * 20)
simulate_network_request()


# --- ⏱️ Time Complexities (Average Case) ---
# Applying a decorator adds the overhead of an extra function call.

def do_nothing(): pass
# @decorator         - Overhead             - O(1) Time 
