# Class Methods
# - A class method is a method that is bound to the CLASS rather than an instance.
# - It receives the class itself as its first argument (usually named 'cls'), much like an instance method receives the instance ('self').
# - They are often used to modify class state (class variables) or to create "alternative constructors".
# - Instance methods: Best for operations on instances of the class (takes 'self').
# - Static methods: Best for utility functions that don't need class/instance state (no 'self' or 'cls').
# - Class methods: Best for modifying class-level state or alternative constructors (takes 'cls').

print("--- 🏫 Class Methods 🏫 ---")

# --- 1. Defining a Class Method ---
print("\n--- 1. Modifying Class State ---")

class Student:
    
    # Class Variable (Shared by all instances)
    school_name = "MIT"
    num_students = 0
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Student.num_students += 1
        
    # Instance Method (Takes 'self')
    def get_info(self):
        return f"{self.first_name} {self.last_name} attends {self.school_name}"
        
    # Class Method (Takes 'cls' instead of 'self')
    # We use the @classmethod decorator. 
    @classmethod
    def set_school_name(cls, new_name):
        # We modify the class variable using 'cls'
        cls.school_name = new_name

student_1 = Student("Spongebob", "Squarepants")
student_2 = Student("Patrick", "Star")

print(f"Original School for the class: {Student.school_name}")

# Calling the class method to change the school name for EVERYONE
Student.set_school_name("Oxford University")

print(f"Updated School for the class: {Student.school_name}")
print(f"Student 1's Info: {student_1.get_info()}")
print(f"Student 2's Info: {student_2.get_info()}")


# --- 2. Alternative Constructors ---
print("\n--- 2. Alternative Constructors ---")
# A very common use case for class methods is providing alternative 
# ways to create objects (since Python doesn't support multiple __init__ methods).

class Employee:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def get_info(self):
        return f"{self.name} works as a {self.position}."
        
    # This class method acts as a secondary constructor!
    @classmethod
    def from_string(cls, employee_str):
        # Imagine we receive data as a hyphen-separated string from a file
        name, position = employee_str.split("-")
        
        # We use 'cls' to create and return a brand new instance of the class
        return cls(name, position)

# Creating an object using the standard __init__ constructor
emp_1 = Employee("Squidward", "Cashier")

# Creating an object using our alternative class method constructor!
emp_string = "Mr.Krabs-Manager"
emp_2 = Employee.from_string(emp_string)

print("Created via __init__:")
print(emp_1.get_info())

print("\nCreated via @classmethod from_string():")
print(emp_2.get_info())


# --- ⏱️ Time Complexities (Average Case) ---

def do_nothing(): pass
# Student.set_school_name(...) - Method Call - O(1) Time 
# Employee.from_string(...)    - String Split & Instantiation - O(N) Time (where N is string length)
