import random

# Python Hangman Game
# A classic milestone project that seamlessly ties together strings, sets, loops, and dictionaries!

# A dictionary mapping the number of wrong guesses to the corresponding ASCII art tuple
hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
}

words = ("apple", "orange", "banana", "coconut", "pineapple", "strawberry", "grape")

def display_hangman(wrong_guesses):
    print("\n**********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**********")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    # List comprehension to generate a list of underscores matching the word's length
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set() # A Set is perfect here to prevent duplicate guesses efficiently!
    is_running = True
    
    print("--- 🔤 Welcome to Python Hangman 🔤 ---")
    
    while is_running:
        display_hangman(wrong_guesses)
        display_hint(hint)
        
        guess = input("Enter a letter: ").lower()
        
        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input. Please enter a single letter.")
            continue
            
        # Using the Set to instantly check if they've guessed this before
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'!")
            continue
            
        guessed_letters.add(guess)
        
        if guess in answer:
            # They guessed correctly! Reveal the letter(s) in the hint
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            # They guessed wrong!
            wrong_guesses += 1
            
        # Check Win Condition
        if "_" not in hint:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("🎉 YOU WIN! 🎉")
            is_running = False
            
        # Check Lose Condition
        elif wrong_guesses >= 6:
            display_hangman(wrong_guesses)
            print("The correct answer was:")
            display_answer(answer)
            print("💀 YOU LOSE! 💀")
            is_running = False

if __name__ == '__main__':
    main()

# --- ⏱️ Time Complexities (Average Case) ---
# guess in guessed_letters   - Set Membership Check - O(1) Time
# guess in answer            - String Membership Check - O(N) Time where N is string length
# hint = ["_"] * len(answer) - List Generation - O(N) Time
