# super() Function
# - A function used to give access to the methods and constructors of a parent class.
# - It returns a temporary object of a parent class when used.
# - Most commonly used in the __init__ method of a child class to initialize inherited attributes and avoid code duplication.

print("--- 🦸‍♂️ super() Function 🦸‍♀️ ---")

# --- 1. The Problem (Without super()) ---
# Imagine we have a Shape class. Without super(), we would have to repeat 
# self.color and self.is_filled in every single child class!
"""
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        self.color = color         # Duplicate code!
        self.is_filled = is_filled # Duplicate code!
        self.radius = radius
"""

# --- 2. The Solution (With super()) ---
print("\n--- 1. Using super() for Initialization ---")

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
        
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}.")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        # We call the parent class's __init__ method using super()
        # This handles self.color and self.is_filled for us!
        super().__init__(color, is_filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

# Creating Objects
circle = Circle(color="Red", is_filled=True, radius=5)
square = Square(color="Blue", is_filled=False, width=10)
triangle = Triangle(color="Green", is_filled=True, width=7, height=8)

print(f"Circle:   Color={circle.color}, Radius={circle.radius}, Filled={circle.is_filled}")
print(f"Square:   Color={square.color}, Width={square.width}, Filled={square.is_filled}")
print(f"Triangle: Color={triangle.color}, Width={triangle.width}, Height={triangle.height}")


# --- 3. Using super() for Other Methods ---
print("\n--- 2. Using super() for Other Methods ---")

# super() isn't just for __init__. You can use it to call ANY method from the parent class.
class Cube(Square):
    def __init__(self, color, is_filled, width):
        # Calls Square's __init__, which in turn calls Shape's __init__!
        super().__init__(color, is_filled, width)
        
    def describe(self):
        # We can call the parent's describe method, then add our own specific behavior!
        print("I am a 3D Cube!")
        super().describe() # Calls Shape's describe() method (inherited via Square)
        print(f"My volume is {self.width ** 3} cubic units.")

cube = Cube(color="Purple", is_filled=True, width=3)
cube.describe()


# --- ⏱️ Time Complexities (Average Case) ---
# super() calls rely on Python's Method Resolution Order (MRO) which is highly optimized.

def do_nothing(): pass
# super().__init__(...)  - Method Delegation - O(1) Time 
# super().describe()     - Method Delegation - O(1) Time
