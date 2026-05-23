# 7. Bitwise Operators
# Used to compare (binary) numbers.

print("--- Bitwise Operators ---")
a = 10  # Binary: 1010
b = 4   # Binary: 0100

print(f"Variables: a = {a} (1010), b = {b} (0100)\n")

print(f"AND (&): a & b = {a & b} (0000 -> 0)")
print(f"OR (|): a | b = {a | b} (1110 -> 14)")
print(f"XOR (^): a ^ b = {a ^ b} (1110 -> 14)")
print(f"NOT (~): ~a = {~a} (Inverts all bits)")
print(f"Zero fill left shift (<<): a << 1 = {a << 1} (10100 -> 20)")
print(f"Signed right shift (>>): a >> 1 = {a >> 1} (0101 -> 5)")
