# Polymorphism
# - Poly = Many, Morph = Form. Polymorphism means "many forms".
# - In Python, the same method or operator can behave differently depending on the object.
# - Types: Method Overriding, Method Overloading (params) & Operator Overloading.

print("--- 🎭 Polymorphism 🎭 ---")

# --- 1. Built-in Polymorphism ---
print("\n--- 1. Built-in Polymorphism ---")
# You've been using polymorphism all along! 
# The len() function acts differently depending on the data type passed to it.

name = "Spongebob"                          # String
friends = ["Patrick", "Sandy", "Squidward"] # List

# Same function name, completely different underlying implementation!
print(f"Length of string '{name}': {len(name)}")
print(f"Length of list: {len(friends)}")


# --- 2. Polymorphism with Inheritance (Method Overriding) ---
print("\n--- 2. Polymorphism with Inheritance ---")
# Different child classes can use the same method name but implement it differently.

class Animal:
    def speak(self):
        # We can raise an error if a child class forgets to override this
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
        
class Cow(Animal):
    def speak(self):
        return "Moo!"

# Creating a list of different objects
animals = [Dog(), Cat(), Cow()]

# We can loop through them and call the EXACT SAME method, 
# and each specific object knows how to respond correctly.
for animal in animals:
    print(animal.speak())


# --- 3. Duck Typing (Polymorphism without Inheritance) ---
print("\n--- 3. Duck Typing ---")
# "If it walks like a duck and quacks like a duck, it must be a duck."
# Python doesn't necessarily care what specific class an object belongs to. 
# It only cares if the object has the required methods!

class Car:
    def start_engine(self):
        print("Vroom! Car engine started.")

class Motorcycle:
    def start_engine(self):
        print("Vrrrt! Motorcycle engine started.")

class Lawnmower:
    def start_engine(self):
        print("Putt putt putt! Lawnmower started.")

# This function expects ANY object that has a 'start_engine' method.
# It DOES NOT care if they share a parent class or not!
def start_any_engine(machine):
    machine.start_engine()

car = Car()
bike = Motorcycle()
mower = Lawnmower()

# Duck Typing Polymorphism in action!
start_any_engine(car)
start_any_engine(bike)
start_any_engine(mower)


# --- ⏱️ Time Complexities (Average Case) ---
# Duck typing and polymorphism rely on dynamic attribute lookup during runtime.

def do_nothing(): pass
# animal.speak()         - Dynamic Method Lookup - O(1) Time 
# machine.start_engine() - Dynamic Method Lookup - O(1) Time
