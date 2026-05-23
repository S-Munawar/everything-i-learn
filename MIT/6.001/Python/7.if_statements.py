# If Statements
# - Do some code only IF some condition is True.
# - Else, do something else.
# - Remember to use indentation (spaces/tabs) for the code inside the statement!

# --- 1. Basic If-Else Statement ---
# The simplest form of checking a condition
print("--- 1. Basic If-Else ---")
age = 21

if age >= 18:
    print(f"You are {age} years old, so you are an adult.")
else:
    print(f"You are {age} years old, so you are a minor.")

# --- 2. If-Elif-Else Statement ---
# When you have multiple conditions to check in order
print("\n--- 2. If-Elif-Else ---")
score = 85

if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B!")
elif score >= 70:
    print("You got a C!")
else:
    print("You failed the test.")

# --- 3. Using Booleans Directly ---
# You can check a boolean variable directly without writing `== True`
print("\n--- 3. Using Booleans ---")
is_online = True

if is_online:
    print("The user is currently online.")
else:
    print("The user is offline.")

# --- 4. Comparing Strings ---
# You can use == to check if strings match exactly
print("\n--- 4. Comparing Strings ---")
name = "Bro Code"

if name == "Bro Code":
    print("Welcome back, Bro!")
elif name == "Spongebob":
    print("I'm ready! I'm ready!")
else:
    print(f"I don't know who you are, {name}.")

# --- 5. Nested If Statements ---
# An if statement inside another if statement
print("\n--- 5. Nested If Statements ---")
is_raining = True
have_umbrella = False

if is_raining:
    print("It is raining outside...")
    if have_umbrella:
        print("You can go outside safely, you have an umbrella.")
    else:
        print("You will get wet if you go outside without an umbrella!")
else:
    print("It's a beautiful day, no umbrella needed.")

# --- 6. The 'pass' Statement ---
# if statements cannot be empty. If you need an empty if statement (for example, as a placeholder), use the 'pass' keyword to avoid getting an error.
print("\n--- 6. The 'pass' Statement ---")
is_ready = False

if is_ready:
    # TODO: write code here later
    pass
else:
    print("Still waiting to be ready...")
