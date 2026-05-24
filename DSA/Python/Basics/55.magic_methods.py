# Magic Methods (Dunder Methods)
# - Magic methods are special methods that start and end with double underscores (__).
# - They are automatically called by many of Python's built-in operations.
# - They allow developers to define custom behaviors for operators (like +, -, ==) and built-in functions (like str(), len()) for custom objects.

print("--- ✨ Magic Methods ✨ ---")

# --- 1. Defining Magic Methods ---
print("\n--- 1. Overriding Magic Methods ---")

class Book:
    
    # __init__ is a magic method we've already used many times!
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        
    # --- String Representation ---
    
    # Called automatically when you print() the object or use str()
    # It should return a nicely formatted, human-readable string.
    def __str__(self):
        return f"'{self.title}' by {self.author}"
        
    # --- Comparison Operators ---
    
    # Equals (==)
    def __eq__(self, other):
        # Two books are considered "equal" if they share a title and author
        return self.title == other.title and self.author == other.author
        
    # Less Than (<)
    def __lt__(self, other):
        # We can define a book as "less than" another if it has fewer pages!
        return self.num_pages < other.num_pages
        
    # --- Math Operators ---
    
    # Add (+)
    def __add__(self, other):
        # What happens when we add two books together? 
        # Let's say it returns the combined total of their pages!
        return self.num_pages + other.num_pages
        
    # --- Collection Methods ---
    
    # Contains (the 'in' keyword)
    def __contains__(self, keyword):
        # Allows us to search for a keyword in the title or author
        return keyword in self.title or keyword in self.author

# --- 2. Using Magic Methods ---
print("\n--- 2. Using the Magic Methods ---")

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 223)
book3 = Book("The Hobbit", "J.R.R. Tolkien", 310) # Identical to book1

# Uses __str__() behind the scenes!
print(f"Book 1: {book1}")
print(f"Book 2: {book2}")

# Uses __eq__()
print(f"\nIs book1 == book2? {book1 == book2}")
print(f"Is book1 == book3? {book1 == book3} (They have the same content!)")

# Uses __lt__()
print(f"\nIs book2 < book1 (shorter)? {book2 < book1}")

# Uses __add__()
print(f"\nTotal pages of book1 + book2: {book1 + book2}")

# Uses __contains__()
print(f"\nIs 'Hobbit' in book1? {'Hobbit' in book1}")
print(f"Is 'Potter' in book1? {'Potter' in book1}")


# --- ⏱️ Time Complexities (Average Case) ---

def do_nothing(): pass
# print(book1)        - Calls __str__       - O(1) Time 
# book1 == book2      - Calls __eq__        - O(1) Time
# book1 + book2       - Calls __add__       - O(1) Time
# 'Hobbit' in book1   - Calls __contains__  - O(N) Time (String searching relies on string length N)
