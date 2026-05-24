# Type casting 
# - Converting one data type into another data type.
# - Functions: str(), int(), float(), bool()

# --- 1. Float to Integer ---
gpa = 3.2
gpa = int(gpa)
print(f"Float to Int: {gpa} | Type: {type(gpa)}")

# --- 2. Integer to Float ---
age = 25
age = float(age)
print(f"Int to Float: {age} | Type: {type(age)}")

# --- 3. Number to String ---
age = 25
age = str(age)
print(f"Number to Str: '{age}' | Type: {type(age)}")

# --- 4. String to Integer ---
grade = "5"
grade = int(grade)
print(f"Str to Int: {grade} | Type: {type(grade)}")

# --- 5. String (with decimal) to Integer ---
gpa_str = "3.2"
# gpa_str = int(gpa_str) # ERROR: Cannot directly cast float-string to int
gpa_str = int(float(gpa_str))
print(f"Float-Str to Int: {gpa_str} | Type: {type(gpa_str)}")

# --- 6. Boolean Conversions ---
is_student = True
is_student_int = int(is_student)
is_student_str = str(is_student)
print(f"Bool to Int: {is_student_int} | Type: {type(is_student_int)}")
print(f"Bool to Str: '{is_student_str}' | Type: {type(is_student_str)}")

# --- 7. Converting to Boolean ---
# Non-empty strings/numbers are True; empty strings/zero are False
name = "Bro Code"
name_bool = bool(name)
empty_str = ""
empty_bool = bool(empty_str)
zero_num = 0
zero_bool = bool(zero_num)

print(f"Non-empty Str to Bool: {name_bool}")
print(f"Empty Str to Bool: {empty_bool}")
print(f"Zero to Bool: {zero_bool}")

# --- 8. Implicit Type Casting ---
# Python automatically converts data types in some operations
a = 5       # int
b = 2.5     # float
c = a + b   # float (int + float = float)
print(f"Implicit Cast (int + float): {c} | Type: {type(c)}")

# --- 9. Invalid Conversions (Errors) ---
x = "hello"
# int(x) # ValueError: invalid literal for int()

# --- 10. String Concatenation ---
age_str = "25"
# age_str += 1 # TypeError: can only concatenate str (not "int") to str
age_str += "1"
print(f"String Concatenation: '{age_str}'")
