# String Methods
# - Strings in Python come with many built-in methods to manipulate them.
# - Methods are called by adding a dot (.) after the string variable.

print("--- 〰️ String Methods 〰️ ---")

# --- 1. String Length ---
# len() is technically a built-in function, not a method, but crucial for strings!
print("\n--- 1. String Length ---")
name = "Bro Code"
length = len(name)
print(f"The length of '{name}' is: {length} characters")


# --- 2. Changing Case ---
print("\n--- 2. Changing Case ---")
name = "bro CODE"
print(f"Original: '{name}'")
print(f".upper(): '{name.upper()}'")           # All uppercase
print(f".lower(): '{name.lower()}'")           # All lowercase
print(f".capitalize(): '{name.capitalize()}'") # Capitalizes ONLY the first letter
print(f".title(): '{name.title()}'")           # Capitalizes first letter of EVERY word


# --- 3. Removing Whitespace ---
print("\n--- 3. Removing Whitespace ---")
spaced_name = "   Bro Code   "
print(f"Original: '{spaced_name}'")
print(f".strip(): '{spaced_name.strip()}'")   # Removes leading and trailing whitespace
print(f".lstrip(): '{spaced_name.lstrip()}'") # Removes leading (left) whitespace
print(f".rstrip(): '{spaced_name.rstrip()}'") # Removes trailing (right) whitespace


# --- 4. Searching and Counting ---
print("\n--- 4. Searching and Counting ---")
phone_number = "123-456-7890"
print(f"Original: '{phone_number}'")

# .find() returns the index of the FIRST occurrence. Returns -1 if not found.
print(f".find('-'): {phone_number.find('-')}")   

# .rfind() returns the index of the LAST occurrence (reverse find).
print(f".rfind('-'): {phone_number.rfind('-')}") 

# .count() counts how many times the character appears.
print(f".count('-'): {phone_number.count('-')}") 


# --- 5. Replacing ---
print("\n--- 5. Replacing ---")
phone_number = "123-456-7890"
print(f"Original: '{phone_number}'")

# Replaces all dashes with an empty string (nothing)
clean_number = phone_number.replace("-", "") 
print(f".replace('-', ''): '{clean_number}'")


# --- 6. Checking String Content ---
# These methods return booleans (True or False)
print("\n--- 6. Checking String Content ---")
print(f"'123'.isdigit(): {'123'.isdigit()}")           # True if ALL characters are digits
print(f"'abc'.isalpha(): {'abc'.isalpha()}")           # True if ALL characters are alphabetical letters
print(f"'a1b2'.isalnum(): {'a1b2'.isalnum()}")         # True if ALL characters are alphanumeric (letters + numbers)

# Notice this is False because it contains a space! A space is not a letter.
print(f"'Bro Code'.isalpha(): {'Bro Code'.isalpha()}") 

# --- 7. Splitting and Joining ---
print("\n--- 7. Splitting and Joining ---")
csv_data = "apple,banana,cherry"
# .split() splits a string into a list based on a delimiter
fruits = csv_data.split(",")
print(f"Original: '{csv_data}'")
print(f".split(','): {fruits}")

# .join() joins an iterable (like a list) into a single string, using the string as a separator
joined_string = "-".join(fruits)
print(f"'-'.join(fruits): '{joined_string}'")

# --- 8. Start and End Checking ---
print("\n--- 8. Start and End Checking ---")
website = "https://www.google.com"
print(f"Original: '{website}'")
# Returns True if string starts/ends with the specified value
print(f".startswith('https'): {website.startswith('https')}")
print(f".endswith('.com'): {website.endswith('.com')}")

# --- 9. Padding and Formatting ---
print("\n--- 9. Padding and Formatting ---")
number_str = "42"
print(f"Original: '{number_str}'")
# .zfill() pads the string with zeros on the left until it reaches the specified length
print(f".zfill(5): '{number_str.zfill(5)}'")

text = "Hello"
# Centers the string within a specified width, padding with a character (default is space)
print(f".center(20, '-'): '{text.center(20, '-')}'")
# Left and Right justify
print(f".ljust(10, '*'): '{text.ljust(10, '*')}'")
print(f".rjust(10, '*'): '{text.rjust(10, '*')}'")

# --- Help ---
# print(help(str))

# --- ⏱️ Time Complexities (Average Case) ---
# Note: Since strings are immutable in Python, most methods that "modify" a string 
# actually create a new one, which generally takes O(N) time (where N is the string length).

my_str = "hello world"

len(my_str)                           # Length - O(1)

my_str.upper()                        # Case conversion - O(N)
my_str.strip()                        # Whitespace removal - O(N)

my_str.find('world')                  # Searching - O(N)
my_str.count('o')                     # Counting - O(N)

my_str.replace('world', 'python')     # Replacing - O(N)

my_str.isalpha()                      # Checking content - O(N)

my_str.split(' ')                     # Splitting - O(N)
'-'.join(['hello', 'world'])          # Joining - O(N)

my_str.startswith('hello')            # Prefix check - O(K) where K is substring length
