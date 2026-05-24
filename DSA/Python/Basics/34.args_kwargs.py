# *args and **kwargs
# - *args: Allows you to pass multiple non-key (positional) arguments. Packaged into a TUPLE.
# - **kwargs: Allows you to pass multiple keyword arguments. Packaged into a DICTIONARY.
# - * is the unpacking operator (acts as a "packing" operator here).
# - Order precedence: 1. Positional, 2. Default, 3. Keyword, 4. ARBITRARY (*args, **kwargs).

print("--- 📦 *args & **kwargs 📦 ---")

# --- 1. *args (Arbitrary Positional Arguments) ---
print("\n--- 1. *args ---")
# *args packs all provided positional arguments into a TUPLE.
# You can name it whatever you want (e.g. *numbers), but *args is the standard convention.

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
    # return sum(args) # This built-in function would also work perfectly!

print(f"Sum of 1, 2, 3: {add(1, 2, 3)}")
print(f"Sum of five numbers: {add(10, 20, 30, 40, 50)}")

def display_name(*args):
    for arg in args:
        print(arg, end=" ")
    print()

display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")


# --- 2. **kwargs (Arbitrary Keyword Arguments) ---
print("\n--- 2. **kwargs ---")
# **kwargs packs all provided keyword arguments into a DICTIONARY.
# The keys are the argument names, and the values are the assigned values.

def print_address(**kwargs):
    # Since kwargs is a dictionary, we iterate through its items()
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St.", 
              apt="100", 
              city="Detroit", 
              state="MI", 
              zip="54321")


# --- 3. Mixing *args and **kwargs ---
print("\n--- 3. Mixing *args and **kwargs ---")
# ⚠️ RULE: *args must ALWAYS come before **kwargs in the parameters list!

def shipping_label(*args, **kwargs):
    # Print the name (args)
    for arg in args:
        print(arg, end=" ")
    print() # Newline
    
    # Print the address (kwargs)
    # We can access specific kwargs using the .get() method to avoid KeyError!
    if kwargs.get('apt'):
        print(f"{kwargs.get('street')} Apt {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")
        
    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants",
               street="123 Fake St.",
               apt="100",
               city="Detroit",
               state="MI",
               zip="54321")


# --- ⏱️ Time Complexities (Average Case) ---
def do_nothing(*args, **kwargs): pass
do_nothing(1, 2, a=3, b=4)               # Function Call - O(1)
