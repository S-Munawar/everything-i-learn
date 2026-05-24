import random

# The random module provides functions to generate pseudo-random numbers.
# "Pseudo-random" means they look random but are generated mathematically, not truly random.

print("--- 🎲 Random Numbers 🎲 ---")

# --- 1. random.randint(a, b) ---
# Returns a random integer N such that a <= N <= b.
print("\n--- 1. random.randint() ---")
number = random.randint(1, 6) # Think of rolling a standard 6-sided die
print(f"Random integer between 1 and 6: {number}")

# --- 2. random.random() ---
# Returns a random floating point number between 0.0 and 1.0
print("\n--- 2. random.random() ---")
float_num = random.random()
print(f"Random float between 0 and 1: {float_num}")

# --- 3. random.choice(sequence) ---
# Returns a randomly selected element from a non-empty sequence (like a list or tuple).
print("\n--- 3. random.choice() ---")
options = ["rock", "paper", "scissors"]
choice = random.choice(options)
print(f"Random choice from list: {choice}")

# --- 4. random.choices(population, weights=None, k=1) ---
# Returns a list of elements chosen from the population with replacement.
print("\n--- 4. random.choices() ---")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# Pull 3 random cards (with replacement, meaning you could draw the same card twice)
hand = random.choices(cards, k=3)
print(f"Random 3 cards (with replacement): {hand}")

# --- 5. random.shuffle(x) ---
# Shuffles the sequence x in place. (This modifies the original list!)
print("\n--- 5. random.shuffle() ---")
deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
print(f"Original deck: {deck}")
random.shuffle(deck)
print(f"Shuffled deck: {deck}")

# --- ⏱️ Time Complexities (Average Case) ---
random.randint(1, 10)      # Random Int - O(1)
random.random()            # Random Float - O(1)
random.choice(['a', 'b'])  # Random Choice - O(1)
random.choices(['a'], k=3) # Multiple Choices - O(K)
random.shuffle(deck)       # Shuffle in-place - O(N)
