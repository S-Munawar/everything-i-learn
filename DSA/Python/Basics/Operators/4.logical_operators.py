# Logical Operators
# - Used to combine conditional statements or reverse them.
# - The primary operators are: 'and', 'or', 'not'

print("--- 🌦️ Logical Operators 🌦️ ---")

# --- 1. The 'and' Operator ---
# BOTH conditions must be True for the entire statement to be True.
# You can chain as many 'and' operators as you want!
print("\n--- 1. 'and' ---")
temp = 25
is_sunny = True

if temp > 0 and temp < 30 and is_sunny:
    print("The weather is absolutely perfect today!")
else:
    print("The weather could be better.")


# --- 2. The 'or' Operator ---
# AT LEAST ONE condition must be True.
print("\n--- 2. 'or' ---")
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend, time to relax!")
else:
    print("It's a weekday, time to work.")


# --- 3. The 'not' Operator ---
# Reverses the boolean value (True becomes False, False becomes True)
print("\n--- 3. 'not' ---")
is_raining = False

if not is_raining:
    print("You don't need an umbrella today.")
else:
    print("Grab an umbrella!")


# --- 4. Combining Operators (Precedence) ---
# In Python, 'not' evaluates first, then 'and', then 'or'. 
# ALWAYS use parentheses () to make complex conditions easier to read!
print("\n--- 4. Combining Operators ---")
has_ticket = True
has_id = False
is_vip = True

# They need (a ticket AND an ID) OR to be a VIP
if (has_ticket and has_id) or is_vip:
    print("Access Granted: Welcome to the event!")
else:
    print("Access Denied.")


# --- 5. Truthy and Falsy Values ---
# You don't just have to use booleans! 
# Empty strings (""), 0, and None evaluate to False. Everything else is True!
print("\n--- 5. Truthy and Falsy Values ---")
username = "" # Empty strings are 'Falsy'

if not username:
    print("Error: Please enter a valid username!")
else:
    print(f"Welcome, {username}!")
