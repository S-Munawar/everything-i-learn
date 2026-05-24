import random
import string

# Python Encryption Program
# This program implements a basic Substitution Cipher!
# It maps every character you type to a randomly shuffled counterpart.

# 1. Create a master list of all characters (space, punctuation, numbers, and letters)
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

# 2. Create a "key" by copying the master list and shuffling it
key = chars.copy()
random.shuffle(key)

print("--- 🔐 Substitution Cipher 🔐 ---")

# --- ENCRYPT ---
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

# For every letter in the user's message, find its index in the 'chars' list,
# then append the character found at that SAME index in the shuffled 'key' list!
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"\nOriginal message : {plain_text}")
print(f"Encrypted message: {cipher_text}")


# --- DECRYPT ---
cipher_text_input = input("\nEnter the encrypted message to decrypt it back: ")
plain_text_output = ""

# To decrypt, we just do the exact opposite! Find the index in the 'key' list,
# and append the character found at that SAME index in the 'chars' list.
for letter in cipher_text_input:
    index = key.index(letter)
    plain_text_output += chars[index]

print(f"\nEncrypted message: {cipher_text_input}")
print(f"Decrypted message: {plain_text_output}")


# --- ⏱️ Time Complexities (Average Case) ---
# chars.index(letter)      - List Index Lookup - O(K) where K is length of the chars list (94)
# for letter in message    - Iterating String  - O(M) where M is length of the message
# Total Encryption Time    - O(M * K) Time Complexity
