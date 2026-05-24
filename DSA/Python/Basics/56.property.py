# @property Decorator
# - @property allows us to define methods that we can access exactly like attributes.
# - This gives us Getter, Setter, and Deleter functionality in a very Pythonic way.
# - It is highly useful for encapsulation, dynamically calculating values, and input validation when variables are updated.

print("--- 🏠 @property Decorator 🏠 ---")

# --- 1. Getters (@property) ---
print("\n--- 1. Using @property for Dynamic Attributes ---")
# If we have an Employee class where 'email' is statically created in __init__, 
# changing the first name later DOES NOT automatically update the email.
# @property solves this!

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # We don't define self.email or self.fullname here anymore!
        
    # GETTER: Allows us to access this method exactly like an attribute
    @property
    def email(self):
        return f"{self.first.lower()}.{self.last.lower()}@company.com"
        
    @property
    def fullname(self):
        return f"{self.first} {self.last}"

emp_1 = Employee("John", "Smith")

print(f"Original Name: {emp_1.first}")
# Notice: We access .email without parenthesis (), even though it's a method!
print(f"Original Email: {emp_1.email}") 

# If we change the first name...
emp_1.first = "Jim"

print(f"\nUpdated Name: {emp_1.first}")
# The email magically updates because the @property getter calculates it on the fly!
print(f"Updated Email: {emp_1.email}") 


# --- 2. Setters (@name.setter) ---
print("\n--- 2. @property Setters ---")
# What if we want to assign a string directly to the fullname attribute?
# Example: emp_1.fullname = "Spongebob Squarepants" 
# By default, a @property creates a read-only property, that throws an AttributeError. We need to define a Setter!

class BetterEmployee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    # GETTER: Allows us to access this method exactly like an attribute
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
        
    # SETTER: Runs whenever we assign a value using the = operator
    @fullname.setter
    def fullname(self, name):
        # We can perform logic here, like splitting the string to update other vars!
        first, last = name.split(" ")
        self.first = first
        self.last = last
        
    # DELETER: Runs whenever we use the 'del' keyword
    @fullname.deleter
    def fullname(self):
        print("--> Deleting Name! <--")
        self.first = None
        self.last = None


emp_2 = BetterEmployee("Squidward", "Tentacles")
print(f"Original Full Name: {emp_2.fullname}")

# This triggers the @fullname.setter method!
emp_2.fullname = "Patrick Star"

print(f"New First Name: {emp_2.first}")
print(f"New Last Name: {emp_2.last}")
print(f"New Full Name: {emp_2.fullname}")


# --- 3. Deleters (@name.deleter) ---
print("\n--- 3. @property Deleters ---")

# This triggers the @fullname.deleter method!
del emp_2.fullname

print(f"After deletion - First Name: {emp_2.first}")
print(f"After deletion - Last Name: {emp_2.last}")


# --- ⏱️ Time Complexities (Average Case) ---

def do_nothing(): pass
# emp_1.email            - Getter Execution - O(1) Time 
# emp_2.fullname = "..." - Setter Execution - O(N) Time (N = String length for splitting)
# del emp_2.fullname     - Deleter Execution- O(1) Time
