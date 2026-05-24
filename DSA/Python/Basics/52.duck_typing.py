# Duck Typing
# - Duck typing is a concept related to dynamic typing, where the type or the class of an object is less important than the methods it defines.
# - Using Duck Typing, we do not check types at all. Instead, we check for the presence of a given method or attribute.
# - "If it walks like a duck, and it quacks like a duck, then it must be a duck." 

print("--- 🦆 Duck Typing 🦆 ---")

# --- 1. Basic Duck Typing Example ---
print("\n--- 1. Basic Duck Typing ---")

class Duck:
    def walk(self):
        print("This duck is waddling.")
        
    def talk(self):
        print("This duck is quacking! (Quack!)")

class Chicken:
    def walk(self):
        print("This chicken is strutting.")
        
    def talk(self):
        print("This chicken is clucking! (Cluck!)")

class Person:
    # This method is designed to conceptually catch a "Duck".
    # However, Python uses Duck Typing. It won't actually verify if 'fowl' is 
    # literally an instance of the 'Duck' class. It only checks if 'fowl' has 
    # the walk() and talk() methods being used inside!
    def catch(self, fowl):
        fowl.walk()
        fowl.talk()
        print("You caught the critter!\n")

duck = Duck()
chicken = Chicken()
person = Person()

print("Passing a Duck to catch():")
person.catch(duck) # Works perfectly!

print("Passing a Chicken to catch():")
# This ALSO works perfectly, because a Chicken has both walk() and talk() methods!
# To the Person's catch() method, the Chicken "walks like a duck" and 
# "talks like a duck", so it happily treats it as one!
person.catch(chicken) 


# --- 2. When Duck Typing Fails (AttributeError) ---
print("--- 2. When Duck Typing Fails ---")

class Fish:
    def swim(self):
        print("This fish is swimming.")
    # Notice: No walk() or talk() methods!

fish = Fish()

print("Passing a Fish to catch():")
try:
    person.catch(fish)
except AttributeError as e:
    print(f"AttributeError Caught: {e}")
    print("The Fish class doesn't have a 'walk' method, so Duck Typing fails!")


# --- ⏱️ Time Complexities (Average Case) ---
# Duck typing relies on Python's dynamic attribute lookup (__dict__ hash table) at runtime.

def do_nothing(): pass
# fowl.walk()      - Method Lookup  - O(1) Time 
# fowl.talk()      - Method Lookup  - O(1) Time
