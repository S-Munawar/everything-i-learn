# Class Variables
# - Class variables are variables defined outside the constructor, directly inside the class.
# - They are shared among all instances (objects) of that class.
# - This is different from instance variables (like self.name), which are unique to each object.

print("--- 🏫 Class Variables 🏫 ---")

# --- 1. Defining Class Variables ---
print("\n--- 1. Defining Class Variables ---")

class Student:
    # CLASS VARIABLES
    # These exist only once in memory and are shared by EVERY Student object.
    school_name = "MIT"
    graduating_class = 2028
    num_students = 0  # We can use this to keep track of how many objects are created!
    
    def __init__(self, name, major):
        # INSTANCE VARIABLES
        # These are unique to the specific object being created (self).
        self.name = name
        self.major = major
        
        # Every time a new student is created, we increment the class variable
        # Notice we access it using the Class Name (Student.num_students)
        Student.num_students += 1
        
    def get_info(self):
        # Even though school_name is a class variable, we can access it using self
        return f"{self.name} is majoring in {self.major} at {self.school_name}."


# --- 2. Accessing Class Variables ---
print("\n--- 2. Accessing Class Variables ---")

# Creating our first students
student_1 = Student("Spongebob", "Culinary Arts")
student_2 = Student("Patrick", "Philosophy")

# We can access class variables directly from the class itself:
print(f"School Name (from class): {Student.school_name}")
print(f"Total Students created: {Student.num_students}")

# We can also access them from instances (objects):
print(f"Student 1's school: {student_1.school_name}")
print(f"Student 2's graduating class: {student_2.graduating_class}")


# --- 3. Modifying Class Variables ---
print("\n--- 3. Modifying Class Variables ---")

# IMPORTANT: To modify a class variable for ALL future/current instances, 
# you MUST modify it via the Class Name, not the instance!

print("Changing the school name for EVERYONE using Student.school_name...")
Student.school_name = "Massachusetts Institute of Technology"

print(student_1.get_info())
print(student_2.get_info())

# What happens if we try to modify a class variable through an INSTANCE?
print("\nPatrick decides he's graduating in 2029 instead...")
student_2.graduating_class = 2029 
# This does NOT change the class variable! 
# It creates a BRAND NEW INSTANCE VARIABLE for student_2 that "shadows" the class variable.

print(f"Student 1's grad class: {student_1.graduating_class} (Still uses class variable)")
print(f"Student 2's grad class: {student_2.graduating_class} (Uses new instance variable)")
print(f"Class default grad class: {Student.graduating_class}")

# Let's create a 3rd student to prove the class variable hasn't changed.
student_3 = Student("Squidward", "Music")
print(f"Student 3's grad class: {student_3.graduating_class} (Uses class variable)")
print(f"Total Students created: {Student.num_students}")


# --- ⏱️ Time Complexities (Average Case) ---
# Accessing class vs instance variables happens via hash tables (__dict__)

def do_nothing(): pass
# Student.school_name                - Class Var Lookup    - O(1) Time
# student_1.school_name              - Lookup              - O(1) Time (Checks instance first, then falls back to class)
# Student.num_students += 1          - Modification        - O(1) Time
