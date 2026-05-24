# if __name__ == '__main__'
# - Indicates that the script can be imported OR run standalone.
# - Functions and classes in this module can be reused without the main block of code automatically executing.
# - Good practice (modular, readable, leaves no global variable, avoids unintended execution).
# - Every Python module has a special built-in variable called __name__.
# - If you run this script directly, Python assigns __name__ = '__main__'.
# - If you import this script into another file, Python assigns __name__ = 'file_name'.

print("--- 🚦 if __name__ == '__main__' 🚦 ---")

# Let's see what __name__ evaluates to right now:
print(f"The special __name__ variable currently evaluates to: '{__name__}'\n")

def main():
    print("🚀 Executing the MAIN program!")
    print("   (This only runs if you run THIS file directly)")

def some_function():
    print("This function can be imported and used in other files safely.")

# This block acts as a gateway or entry point!
# It prevents code from being run automatically if this file is imported elsewhere.
if __name__ == '__main__':
    # This block WILL run because we are executing this file directly.
    main()
else:
    # This block would run if we imported this file into another script.
    print("📦 This file was IMPORTED by another script! The main() function was blocked from running automatically.")

# --- ⏱️ Time Complexities (Average Case) ---
# Comparing strings in Python generally takes O(N) time where N is the length of the string.
"__name__" == "__main__"   # String Comparison - O(N)
