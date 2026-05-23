# Temperature Conversion Program
# - Converts a temperature from Celsius to Fahrenheit, or vice versa.
# - A classic program to practice math formulas and conditional logic!

print("--- 🌡️ Temperature Conversion Program 🌡️ ---")

# --- 1. Get User Input ---
unit = input("Is this temperature in Celsius or Fahrenheit? (C or F): ")
temp = float(input("Enter the temperature: "))

print("\n----------------------------------")

# --- 2. Perform the Conversion ---
# We can use the .upper() string method to make the user's input uppercase automatically!
# This way, it matches "C" whether they type "c" or "C".

if unit.upper() == "C":
    # Celsius to Fahrenheit formula: (C * 9/5) + 32
    converted_temp = round((temp * 9 / 5) + 32, 1)
    print(f"The temperature in Fahrenheit is: {converted_temp}°F")

elif unit.upper() == "F":
    # Fahrenheit to Celsius formula: (F - 32) * 5/9
    converted_temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {converted_temp}°C")

else:
    # Error handling if they type something else
    print(f"Error: '{unit}' is an invalid unit of measurement. Please enter C or F.")

print("----------------------------------\n")
