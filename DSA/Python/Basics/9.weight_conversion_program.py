# Weight Conversion Program
# - Converts a user's weight from Kilograms to Pounds, or vice versa.
# - Combines input(), float casting, if statements, and math operations.

print("--- ⚖️ Weight Conversion Program ⚖️ ---")

# --- 1. Get User Input ---
# Cast the weight to a float so we can do math with it
weight = float(input("Enter your weight: "))

# Ask for the unit (we don't cast this, it stays a string)
unit = input("Is this in Kilograms or Pounds? (Type K or L): ")

print("\n----------------------------------")

# --- 2. Perform the Conversion ---
# We check for both uppercase and lowercase inputs just in case!

if unit == "K" or unit == "k":
    # Kilograms to Pounds formula: kg * 2.205
    weight *= 2.205
    new_unit = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {new_unit}")

elif unit == "L" or unit == "l":
    # Pounds to Kilograms formula: lbs / 2.205
    weight /= 2.205
    new_unit = "Kgs."
    print(f"Your weight is: {round(weight, 1)} {new_unit}")

else:
    # Error handling if they type something else
    print(f"Error: '{unit}' is not a valid unit. Please enter K or L.")

print("----------------------------------\n")
