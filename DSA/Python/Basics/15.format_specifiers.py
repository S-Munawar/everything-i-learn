# Format Specifiers
# - Used to format a value inside an f-string or using the .format() method.
# - Syntax: {value:flags}
# - Useful for formatting numbers, padding strings, or aligning text.

print("--- 📐 Format Specifiers 📐 ---")

price1 = 3.14159
price2 = -987.65
price3 = 1200000.5

print("\n--- 1. Decimal Places ---")
# Rounds to a specific number of decimal places (e.g., .2f for 2 decimals)
print(f"Original Price 1: {price1}")
print(f"Price 1 (2 decimals): {price1:.2f}")
print(f"Price 2 (1 decimal) : {price2:.1f}")

print("\n--- 2. Number Separators ---")
# Adds commas as thousands separators (very useful for large numbers)
print(f"Original Price 3: {price3}")
print(f"Price 3 (with commas): {price3:,}")
# You can also combine them! (Commas AND 2 decimal places)
print(f"Price 3 (commas & decimals): {price3:,.2f}")

print("\n--- 3. Justification and Padding ---")
# Allocates a specific amount of space and aligns the text
# :<  Left justify
# :>  Right justify
# :^  Center align
text = "Hello"
print(f"|{text:<10}| (Left justify, 10 spaces)")
print(f"|{text:>10}| (Right justify, 10 spaces)")
print(f"|{text:^10}| (Center align, 10 spaces)")

print("\n--- 4. Padding with Characters ---")
# You can specify a character before the alignment symbol to pad with that character instead of spaces
print(f"|{text:_<10}| (Pad right with underscores)")
print(f"|{text:*>10}| (Pad left with asterisks)")
print(f"|{text:-^10}| (Pad both sides with dashes)")

print("\n--- 5. Positive and Negative Signs ---")
# :+  Always show the sign (both + and -)
# :   (Space) Show a space for positive numbers, and a minus for negative numbers
pos_num = 42
neg_num = -42
print(f"Positive with sign: {pos_num:+}")
print(f"Negative with sign: {neg_num:+}")
print(f"Positive with space:{pos_num: }")
print(f"Negative with space:{neg_num: }")

print("\n--- 6. Number Bases (Advanced) ---")
# Format numbers in different bases
number = 255
print(f"Decimal (Base 10): {number:d}")
print(f"Binary (Base 2): {number:b}")
print(f"Octal (Base 8): {number:o}")
print(f"Hexadecimal (Base 16, lowercase): {number:x}")
print(f"Hexadecimal (Base 16, uppercase): {number:X}")
print(f"Scientific Notation: {number:e}")
