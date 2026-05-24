# Membership Operators
# - Used to test whether a value or variable is found in a sequence.
# - Works with strings, lists, tuples, sets, or dictionaries.
# - They evaluate to a boolean value: True or False.
# - The two operators are: 'in' and 'not in'.

print("--- 🎫 Membership Operators 🎫 ---")

# --- 1. Strings ---
print("\n--- 1. Strings ---")
word = "APPLE"
letter = "A"

print(f"Is '{letter}' in '{word}'? : {letter in word}")
print(f"Is 'Z' NOT in '{word}'?    : {'Z' not in word}")

# Real world example: Checking for valid inputs (like in a Hangman game!)
# guess = input("Guess a letter: ").upper()
# if guess in word:
#     print(f"Yes! {guess} is in the word!")


# --- 2. Lists and Tuples ---
print("\n--- 2. Lists & Tuples ---")
students = ["Spongebob", "Patrick", "Sandy"]
student = "Squidward"

print(f"Is {student} a student? : {student in students}")

if student not in students:
    print(f"{student} was NOT found in the class list.")


# --- 3. Sets ---
print("\n--- 3. Sets ---")
# Remember: Sets are optimized specifically for membership testing!
valid_grades = {"A", "B", "C", "D", "F"}
grade = "B"

if grade in valid_grades:
    print(f"'{grade}' is a valid grade option.")


# --- 4. Dictionaries ---
print("\n--- 4. Dictionaries ---")
student_grades = {"Sandy": "A", "Squidward": "B", "Spongebob": "C"}
search_student = "Patrick"

# By default, the 'in' operator checks the dictionary KEYS
print(f"Did {search_student} take the class? (Checking keys) : {search_student in student_grades}")
print(f"Did Sandy take the class? (Checking keys)    : {'Sandy' in student_grades}")

# If you want to check if a VALUE exists, you must explicitly use .values()
target_grade = "A"
print(f"Did anyone get an {target_grade}? (Checking values)       : {target_grade in student_grades.values()}")


# --- ⏱️ Time Complexities (Average Case) ---
"A" in "APPLE"                       # String - O(N) (Where N is string length)
"Sandy" in ["Spongebob", "Sandy"]    # List/Tuple - O(N) (Iterates through the sequence)
"A" in {"A", "B", "C"}               # Set - O(1) (Lightning fast hash table lookup!)
"Sandy" in student_grades            # Dictionary (Keys) - O(1) (Hash table lookup!)
"A" in student_grades.values()       # Dictionary (Values) - O(N) (Must search through all values)
