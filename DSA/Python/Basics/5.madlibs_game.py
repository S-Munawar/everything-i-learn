# Mad Libs Game
# - A word game where players are prompted for a list of words to substitute for blanks in a story.
# - This is a great way to practice using input() and f-strings!

print("--- 📖 Welcome to the Python Mad Libs Game! 📖 ---")
print("Please enter the following words to create a funny story:\n")

# --- 1. Gather User Inputs ---
adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, or thing): ")
adjective2 = input("Enter another adjective: ")
verb1 = input("Enter a verb ending with 'ing' (action): ")
adjective3 = input("Enter one last adjective: ")

# --- 2. Generate and Print the Story ---
# We use f-strings to dynamically insert the user's variables into our sentences!
print("\n--------------------------------------------------")
print("Here is your Mad Libs story:")
print("--------------------------------------------------\n")

print(f"Today I went to a very {adjective1} zoo.")
print(f"In an exhibit, I saw a giant {noun1}.")
print(f"The {noun1} was so {adjective2} and it was {verb1} all around!")
print(f"I had a really {adjective3} time at the zoo today.")

print("\n--------------------------------------------------")
