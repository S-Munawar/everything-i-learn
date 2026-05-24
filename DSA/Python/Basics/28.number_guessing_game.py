import random

# Number Guessing Game
# This game utilizes the `random` module we just learned, combined with a while loop!

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("--- 🔢 Python Number Guessing Game 🔢 ---")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")

    # Check if the input is actually a valid digit before converting it to an integer
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        # Check if the guess is within the valid range
        if guess < lowest_num or guess > highest_num:
            print("⚠️ That number is out of range!")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        
        # Check if the guess is too low
        elif guess < answer:
            print("📉 Too low! Try again!")
        
        # Check if the guess is too high
        elif guess > answer:
            print("📈 Too high! Try again!")
        
        # If it's not out of range, not too low, and not too high, it must be correct!
        else:
            print(f"\n🎉 CORRECT! The answer was {answer}")
            print(f"Total number of guesses: {guesses}")
            is_running = False
            
    else:
        print("❌ Invalid guess. Please enter a whole number.")
        print(f"Please select a number between {lowest_num} and {highest_num}")

# --- ⏱️ Time Complexities (Average Case) ---
random.randint(1, 100)     # Random Int - O(1)
"10".isdigit()             # String check - O(K)
