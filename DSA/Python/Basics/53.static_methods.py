# Static Methods
# - A static method is a method that belongs to a class rather than an instance.
# - It does NOT have access to 'self' (the object) or 'cls' (the class itself).
# - It is essentially a regular Python function that is placed inside a class because it logically belongs there.

print("--- 🛠️ Static Methods 🛠️ ---")

import datetime

# --- 1. Defining a Static Method ---
print("\n--- 1. Defining and Using a Static Method ---")

class Employee:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    # Instance method (requires 'self' to access object attributes)
    def get_info(self):
        return f"{self.name} is a {self.position}."
        
    # Static method (does NOT require 'self' or 'cls')
    # We use the @staticmethod decorator to tell Python this is a static method.
    @staticmethod
    def is_workday(day):
        # In Python's datetime, Monday = 0, Sunday = 6
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# --- 2. Calling a Static Method ---

# We can call a static method DIRECTLY from the Class Name itself! 
# We DO NOT need to create an object (instance) first to use it.
my_date = datetime.date(2026, 5, 24) # A Sunday

print(f"Is {my_date} a workday? {Employee.is_workday(my_date)}")

# You *can* also call it from an instance, but it's best practice to call it via the Class.
emp_1 = Employee("Spongebob", "Fry Cook")
print(f"Is {my_date} a workday? (called via instance): {emp_1.is_workday(my_date)}")

print("\nEmployee Info:")
print(emp_1.get_info())


# --- 3. Another Example (Utility Classes) ---
print("\n--- 2. Utility Classes ---")
# Sometimes classes are purely used to group related static methods together.
# In these cases, you might never actually instantiate the class!

class Calculator:
    
    @staticmethod
    def add(x, y):
        return x + y
        
    @staticmethod
    def multiply(x, y):
        return x * y

# We don't instantiate Calculator() anywhere, we just use its static methods!
print(f"Calculator.add(5, 3)      = {Calculator.add(5, 3)}")
print(f"Calculator.multiply(5, 3) = {Calculator.multiply(5, 3)}")


# --- ⏱️ Time Complexities (Average Case) ---

def do_nothing(): pass
# Employee.is_workday(...) - Method Call - O(1) Time 
# Calculator.add(...)      - Method Call - O(1) Time
