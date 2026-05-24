# User Input
# - The input() function prompts the user to enter data from the console.
# - It ALWAYS returns data as a string (str) by default.
# - You must type cast the input if you need to use it as a different data type (like int or float).

# --- 1. Basic String Input ---
print("--- 1. Basic String Input ---")
name = input("Enter your name: ")
print(f"Hello, {name}! | Type: {type(name)}")

# --- 2. Integer Input ---
# You can get the input and convert it to an integer on separate lines
print("\n--- 2. Integer Input ---")
age_str = input("Enter your age: ")
age = int(age_str)
print(f"You are {age} years old. | Type: {type(age)}")

# --- 3. Float Input (One-Liner) ---
# It is more common to wrap the input() function directly inside a cast function
print("\n--- 3. Float Input ---")
gpa = float(input("Enter your GPA: "))
print(f"Your GPA is {gpa} | Type: {type(gpa)}")

# --- 4. Boolean Input (Edge Case) ---
# Warning: bool(input()) will be True for ANY text, and False ONLY if the user just hits Enter.
print("\n--- 4. Boolean Input ---")
is_student_input = input("Are you a student? (Type anything for yes, press Enter for no): ")
is_student = bool(is_student_input)
print(f"Student Status: {is_student} | Type: {type(is_student)}")

# --- 5. Math with Inputs ---
print("\n--- 5. Math Calculation with Inputs ---")
quantity = int(input("How many items are you buying?: "))
price = float(input("What is the price of each item?: $"))
total = quantity * price
print(f"Your total comes to: ${total}")
