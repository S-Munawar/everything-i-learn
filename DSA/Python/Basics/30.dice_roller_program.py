import random

# Dice Roller Program
# This program combines random numbers, dictionaries (for ASCII art), and loops!

# Dictionary containing tuples of strings to represent dice faces
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

print("--- 🎲 Dice Roller Program 🎲 ---")

while True:
    num_dice = input("How many dice would you like to roll? (Enter 0 to quit): ")
    
    # Input validation
    if not num_dice.isdigit():
        print("❌ Invalid input. Please enter a whole number.\n")
        continue
        
    num_dice = int(num_dice)
    
    if num_dice == 0:
        print("Thanks for playing! 👋")
        break
        
    dice_results = []
    
    # Roll the dice
    for _ in range(num_dice):
        dice_results.append(random.randint(1, 6))
        
    print("\n--- RESULTS ---")
    
    # Print the ASCII art faces side-by-side
    # A die has 5 lines of ASCII art, so we loop 5 times
    for line in range(5):
        for die in dice_results:
            print(dice_art[die][line], end=" ")
        print() # Move to the next line after printing one row of all dice
        
    total = sum(dice_results)
    
    print(f"\nNumbers Rolled: {dice_results}")
    print(f"Total Sum: {total}\n")

# --- ⏱️ Time Complexities (Average Case) ---
random.randint(1, 6)       # Random Int - O(1)
sum([1, 2, 3])             # Sum List - O(N) where N is number of elements
