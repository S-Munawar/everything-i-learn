# Multiple & Multilevel Inheritance
# - Multiple inheritance is when a child class inherits from MORE THAN ONE parent class.
# - Multilevel inheritance is when a child class inherits from another child class.

print("--- 🦅 Multiple & Multilevel Inheritance 🐟 ---")

# --- 1. Multiple Inheritance ---
# A child class gets all the attributes and methods of ALL its parent classes.
print("\n--- 1. Multiple Inheritance ---")

# Parent Class 1
class Prey:
    def flee(self):
        print("This animal is fleeing!")

# Parent Class 2
class Predator:
    def hunt(self):
        print("This animal is hunting!")

# Single Inheritance
class Rabbit(Prey):
    pass # 'pass' means do nothing; just inherit the Parent's traits.

class Hawk(Predator):
    pass

# MULTIPLE INHERITANCE
# A Fish can be both hunted (Prey) and hunt others (Predator).
# We pass both parent classes separated by a comma.
class Fish(Prey, Predator):
    pass

print("\n--- Using Multiple Inheritance ---")
rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

print("Rabbit Actions:")
rabbit.flee()

print("\nHawk Actions:")
hawk.hunt()

print("\nFish Actions:")
# The fish can do BOTH because it inherited from both parent classes!
fish.flee()
fish.hunt()


# --- 2. Multilevel Inheritance ---
print("\n--- 2. Multilevel Inheritance ---")
# Multilevel inheritance occurs when a derived class inherits from another derived class.
# Imagine a family tree: Grandparent -> Parent -> Child.

class Organism:
    def breathe(self):
        print("This organism is taking a breath.")

# Animal inherits from Organism
class MultilevelAnimal(Organism):
    def eat(self):
        print("This animal is eating.")

# Dog inherits from MultilevelAnimal, which inherits from Organism
class MultilevelDog(MultilevelAnimal):
    def bark(self):
        print("This dog is barking.")

dog = MultilevelDog()
print("\nDog Actions (Multilevel):")
dog.bark()      # Dog's own method
dog.eat()       # Inherited from MultilevelAnimal
dog.breathe()   # Inherited from Organism (Multilevel!)


# --- 3. Method Resolution Order (MRO) ---
# If multiple parent classes have a method with the SAME NAME, Python uses the
# Method Resolution Order (MRO) to decide which one to call. 
# - For multiple inheritance, it generally searches left-to-right.
# - For multilevel inheritance, it searches bottom-to-top (Child -> Parent -> Grandparent).
# Under the hood, Python uses the C3 Linearization algorithm to build this order.
print("\n--- 3. Method Resolution Order (MRO) ---")

class A:
    def say_hello(self):
        print("Hello from Class A!")

class B:
    def say_hello(self):
        print("Hello from Class B!")

# Inherits from A first, then B
class C(A, B):
    pass

c_instance = C()
# Since A was listed first in C(A, B), it uses A's say_hello() method.
print("Calling c_instance.say_hello():")
c_instance.say_hello() 

# You can actually see the MRO by using the .mro() method on the class!
print(f"\nMRO for Class C: {C.mro()}")


# --- ⏱️ Time Complexities (Average Case) ---
# MRO resolution is highly optimized in Python. While the worst-case lookup
# time is proportional to the depth of the inheritance tree, Python caches
# these lookups, making subsequent calls extremely fast.

def do_nothing(): pass
# fish.flee()            - Method Lookup (Inherited) - O(1) Time 
# c_instance.say_hello() - MRO Method Lookup         - O(1) Time (due to caching)
