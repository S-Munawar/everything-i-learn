import random

# Rock, Paper, Scissors Game
# This game utilizes the random module, while loops, and conditional statements.

options = ("rock", "paper", "scissors")
is_running = True

print("--- ✂️ 📄 🪨 Rock, Paper, Scissors 🪨 📄 ✂️ ---")

while is_running:

    player = None
    computer = random.choice(options)

    # Keep prompting the player until they enter a valid option
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"\nPlayer: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie! 🤝")
    elif player == "rock" and computer == "scissors":
        print("You win! 🏆")
    elif player == "paper" and computer == "rock":
        print("You win! 🏆")
    elif player == "scissors" and computer == "paper":
        print("You win! 🏆")
    else:
        print("You lose! 💀")

    # Ask the user if they want to play another round
    if input("\nPlay again? (y/n): ").lower() != "y":
        is_running = False

print("\nThanks for playing! 👋")

# --- ⏱️ Time Complexities (Average Case) ---
random.choice(options)      # Random Choice - O(1)
"rock" in options           # Tuple Membership Check - O(N)
