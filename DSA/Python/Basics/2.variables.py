# Variable
# - A container for a value
# - Cannot start with a number
# - Must start with a letter or _ 
# - Can contain letters, numbers, and _
# - Case-sensitive (age and Age are different)

# Strings
first_name = "Bro Code"
print(f"Hello {first_name}") # f(format) string 

# Integers
age = 25
print(f"Your age is: {age}") #

# Float
gpa = 3.2
print(f"Your GPA is: {gpa}") #

# Boolean
is_student = True
print(f"You are a student? {is_student}") #

# --- Multiple Assignment ---
# Allows us to assign multiple variables at the same time in one line of code
name, age, attractive = "Bro", 25, True
print(f"{name} is {age} years old. Attractive: {attractive}")

# Assigning the same value to multiple variables
x = y = z = 0
print(f"x: {x}, y: {y}, z: {z}")
