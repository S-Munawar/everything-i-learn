# Object-Oriented Programming (OOP) in Python
# - Object: A "bundle" of related attributes (variables) and methods (functions).
# - You can think of an object as a physical item in the real world.
# - Class: A blueprint used to design and create those objects.

print("--- 🚗 Object-Oriented Programming (OOP) 🚗 ---")

# --- 1. Defining a Class ---
print("\n--- 1. Defining a Class ---")

class Car:
    # The __init__ method is a special "constructor" method.
    # It runs automatically whenever we create a new object from this class.
    # 'self' refers to the specific object currently being created/used.
    
    def __init__(self, make, model, year, color):
        # These are ATTRIBUTES (variables that belong to the object)
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False # We can set default attributes too!
        
    # These are METHODS (functions that belong to the object)
    def start_engine(self):
        if not self.is_running:
            self.is_running = True
            print(f"The {self.color} {self.make} {self.model}'s engine is now running! Vroom!")
        else:
            print(f"The {self.make}'s engine is already running!")
            
    def stop_engine(self):
        if self.is_running:
            self.is_running = False
            print(f"The {self.make} {self.model}'s engine is turned off.")
        else:
            print(f"The {self.make}'s engine is already off.")


# --- 2. Creating Objects (Instances) ---
print("\n--- 2. Creating Objects ---")

# We use our 'Car' blueprint to create two completely distinct car objects!
car_1 = Car("Ford", "Mustang", 2024, "Red")
car_2 = Car("Chevy", "Corvette", 2025, "Blue")


# --- 3. Accessing Attributes & Calling Methods ---
print("\n--- 3. Accessing Attributes & Calling Methods ---")

# Accessing attributes using "dot notation"
print(f"Car 1 is a {car_1.color} {car_1.make} {car_1.model}.")
print(f"Car 2 is a {car_2.color} {car_2.make} {car_2.model}.")

# Calling methods using "dot notation"
print("\nLet's drive Car 1:")
car_1.start_engine()
car_1.start_engine() # Trying to start it again triggers the 'else' block!
car_1.stop_engine()

print("\nLet's drive Car 2:")
car_2.start_engine()


# --- 4. The 'object' and 'type' Built-ins ---
print("\n--- 4. The 'object' and 'type' Built-ins ---")
# - 'object' is the base class of almost all Python classes.
# - 'type' is the metaclass that creates classes.
# - Every class in Python is an instance of 'type'.
# - 'type' itself is also a class.
# - 'type' is an instance of itself.

print(f"Is Car a subclass of object? {issubclass(Car, object)}")
print(f"Is Car an instance of type? {isinstance(Car, type)}")
print(f"Is type an instance of itself? {isinstance(type, type)}")


# --- ⏱️ Time Complexities (Average Case) ---
# Object instantiation, attribute access, and method calling in Python are implemented 
# using highly optimized hash tables (dictionaries) under the hood.

def do_nothing(): pass
# car_1 = Car(...)         - Object Instantiation - O(1) Time
# car_1.make               - Attribute Lookup     - O(1) Time
# car_1.start_engine()     - Method Call          - O(1) Time
