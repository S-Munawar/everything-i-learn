# Dictionaries
# - A mutable collection of unique key:value pairs.
# - Fast because they use hashing, allowing us to access a value quickly via its key.
# - Note: As of Python 3.7, dictionaries are ordered, but we still access elements via keys, not indexes.

print("--- 📚 Dictionaries 📚 ---")

# --- 1. Creating and Accessing ---
print("\n--- 1. Creating & Accessing ---")
capitals = {'USA': 'Washington D.C.',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}

print("Dictionary of Capitals:")
print(capitals)

# Accessing values using bracket notation
print(f"\nCapital of Russia: {capitals['Russia']}")

# Using .get() is safer because it returns None instead of an error if the key doesn't exist
print(f"Capital of Germany (using .get()): {capitals.get('Germany')}") 
# print(capitals['Germany']) # Uncommenting this would raise a KeyError!

# --- 2. Modifying Dictionaries ---
print("\n--- 2. Modifying Dictionaries ---")
# Adding a new key-value pair
capitals.update({'Germany': 'Berlin'})
print(f"After adding Germany:\n{capitals}")

# Updating an existing key
capitals.update({'USA': 'Las Vegas'}) # Update Washington D.C. to Las Vegas
print(f"After updating USA:\n{capitals}")

# Removing items
capitals.pop('China')
print(f"After popping 'China':\n{capitals}")

capitals.popitem() # Removes the last inserted key-value pair
print(f"After popitem() (removes last inserted):\n{capitals}")

# capitals.clear() # Removes all elements from the dictionary

# --- 3. Dictionary Methods ---
print("\n--- 3. Useful Dictionary Methods ---")
keys = capitals.keys()        # Returns an iterable 'dict_keys' view object
print(f"Keys: {keys}")
# print(list(keys))           # You can cast it to a list if you need to index them

values = capitals.values()    # Returns an iterable 'dict_values' view object
print(f"Values: {values}")
# print(list(values))         # You can cast it to a list if you need to index them

items = capitals.items()      # Returns an iterable 'dict_items' view object (contains tuples)
print(f"Items (Key-Value pairs as tuples): {items}")
# print(list(items))          # You can cast it to a list if you need to index them
                              
# print(dir(capitals))        # Lists all attributes and methods of the dictionary
# print(help(capitals))       # Shows comprehensive documentation for the dictionary

# --- 4. Iterating Through a Dictionary ---
print("\n--- 4. Iterating Through Dictionaries ---")
print("Iterating through keys:")
for key in capitals.keys():
    print(f"- {key}")

print("\nIterating through values:")
for value in capitals.values():
    print(f"- {value}")

print("\nIterating through both (items):")
for key, value in capitals.items():
    print(f"The capital of {key} is {value}")

print("\n--- 🔍 Summary ---")
print("Dictionaries store data in key:value pairs.")
print("Use .get(key) to safely access values without risking errors.")
print("Use .update() to add new pairs or modify existing ones.")
print("Use .keys(), .values(), and .items() to retrieve dictionary components and iterate over them.")

# --- ⏱️ Time Complexities (Average Case) ---
my_dict = {'a': 1, 'b': 2, 'c': 3}

my_dict['a']                      # Access - O(1)
my_dict.get('a')                  # get() - O(1)  

my_dict['d'] = 4                  # Insert / Update - O(1)
my_dict.update({'e': 5})          # update() - O(K) (K = elements to add)
my_dict.setdefault('f', 6)        # setdefault() - O(1)

del my_dict['b']                  # Delete - O(1)
my_dict.pop('c')                  # pop() - O(1)
my_dict.popitem()                 # popitem() - O(1)

'a' in my_dict                    # Search / Membership - O(1)
len(my_dict)                      # len() - O(1)

my_dict.keys()                    # keys() - O(1)
my_dict.values()                  # values() - O(1)
my_dict.items()                   # items() - O(1)

my_dict_copy = my_dict.copy()     # copy() - O(N)
new_dict = dict.fromkeys(['A', 'B']) # fromkeys() - O(N)

for key in my_dict:               # Iterate - O(n)
    pass

my_dict.clear()                   # clear() - O(1)
