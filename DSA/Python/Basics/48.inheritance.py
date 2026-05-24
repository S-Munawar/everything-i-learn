# Inheritance
# - Inheritance allows us to create a new class based on an existing class.
# - The new class (Child/Derived class) inherits all attributes and methods of the existing class (Parent/Base class).
# - This promotes code reusability and establishes a natural "is-a" relationship.

print("--- 🧬 Inheritance 🧬 ---")

# --- 1. Defining a Parent (Base) Class ---
print("\n--- 1. Defining a Parent Class ---")

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating.")
        
    def sleep(self):
        print(f"{self.name} is sleeping.")

# --- 2. Defining Child (Derived) Classes ---
print("\n--- 2. Defining Child Classes ---")

# To inherit from another class, we pass the Parent class as a parameter
# in parentheses after the class name.
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says woof!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says meow!")
        
class Mouse(Animal):
    def squeak(self):
        print(f"{self.name} says squeak!")

# --- 3. Creating Objects and Using Inherited Methods ---
print("\n--- 3. Using Inherited Methods ---")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(f"Created a Dog named {dog.name}, a Cat named {cat.name}, and a Mouse named {mouse.name}.")

# These methods were inherited from the Animal class!
print("\nInherited Methods:")
dog.eat()
cat.sleep()

# These methods are unique to the child classes
print("\nUnique Child Methods:")
dog.bark()
cat.meow()
mouse.squeak()

print(f"\nIs {dog.name} alive? {dog.is_alive} (Inherited attribute)")


# --- 4. Method Overriding ---
# Sometimes a child class needs a different implementation of a parent's method.
print("\n--- 4. Method Overriding ---")

class Bird(Animal):
    # Overriding the 'eat' method from the Animal class
    def eat(self):
        print(f"{self.name} is pecking at some seeds.")

bird = Bird("Tweety")
bird.eat() # Calls the Bird's eat() method, NOT the Animal's eat() method
# Note: bird.sleep() would still call the Animal's sleep() method.


# --- ⏱️ Time Complexities (Average Case) ---
# When you call a method, Python first looks in the object's class dictionary.
# If it's not found, it traverses up the "Method Resolution Order" (MRO) to the parent class(es).

def do_nothing(): pass
# dog.eat()              - Method Lookup (Inherited) - O(1) Time (MRO lookup is highly optimized)
# dog.bark()             - Method Lookup (Direct)    - O(1) Time
# class Dog(Animal):     - Inheritance Definition    - O(1) Time
