# Keyword Arguments
# - An argument preceded by an identifier (e.g. name="value").
# - Helps significantly with readability.
# - The order of arguments doesn't matter when using them!
# - Order precedence: 1. Positional, 2. Default, 3. Keyword, 4. Arbitrary

print("--- 🔑 Keyword Arguments 🔑 ---")

# --- 1. Basic Keyword Arguments ---
print("\n--- 1. Basic Example ---")
def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

# Positional arguments: The order matters completely!
print("Positional:")
hello("Hello", "Mr.", "SpongeBob", "SquarePants")

# Keyword arguments: The order does NOT matter!
print("\nKeyword:")
hello(last="SquarePants", title="Mr.", first="SpongeBob", greeting="Hello")

# Mixing positional and keyword:
# ⚠️ RULE: Positional arguments MUST come before keyword arguments!
print("\nMixed:")
hello("Hello", title="Mr.", last="SquarePants", first="SpongeBob")


# --- 2. Real World Built-in Examples ---
print("\n--- 2. Built-in Examples ---")
# You've actually already been using keyword arguments without knowing it!
# The print() function has 'sep' and 'end' parameters that you can override via keyword arguments.

# By default, print separates items with a space.
print("1", "2", "3", "4", "5") 

# We can override the default by explicitly providing the 'sep' (separator) keyword argument:
print("1", "2", "3", "4", "5", sep="-") 

# --- 3. Generating a formatted string ---
print("\n--- 3. Formatted String Example ---")
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

# When a function has many parameters, keyword arguments make calling it extremely readable:
phone_num = get_phone(country=1, area=123, first=456, last=7890)
print(f"Formatted Phone Number: {phone_num}")


# --- ⏱️ Time Complexities (Average Case) ---
def do_nothing(arg="default"): pass
do_nothing(arg="keyword")               # Function Call with Keyword Argument - O(1)
