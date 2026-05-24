import random

# Python Slot Machine Project
# Combines the 'random' module, list comprehensions, functions, and loops!

def spin_row():
    # List of possible symbols
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    
    # We want to return a list of 3 random symbols.
    # We can use a list comprehension!
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*************")
    # Using the string '.join()' method to beautifully format our row
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    # Check if all 3 symbols in the row are identical
    if row[0] == row[1] == row[2]:
        # Payout multipliers based on the winning symbol
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    
    # If they don't match, you get nothing!
    return 0

def main():
    balance = 100.0
    
    print("--- 🎰 Welcome to Python Slots 🎰 ---")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    
    while balance > 0:
        print(f"\nCurrent Balance: ${balance:.2f}")
        
        bet = input("Place your bet amount (or 'q' to quit): ")
        
        if bet.lower() == 'q':
            break
            
        # Basic input validation for the bet
        if not bet.isdigit():
            print("❌ Invalid bet. Please enter a whole number.")
            continue
            
        bet = int(bet)
        
        if bet <= 0:
            print("❌ Bet must be greater than zero.")
            continue
        elif bet > balance:
            print("❌ Insufficient funds!")
            continue
            
        # Deduct bet from balance
        balance -= bet
        
        # Spin the machine
        row = spin_row()
        print("\nSpinning...")
        print_row(row)
        
        # Calculate payout
        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"🎉 WINNER! You won ${payout:.2f}!")
            balance += payout
        else:
            print("Sorry, you lost this spin! 💀")
            
    print("-------------------------------------")
    print(f"Game Over. You walked away with ${balance:.2f}.")
    print("Thanks for playing! 👋")

if __name__ == '__main__':
    main()

# --- ⏱️ Time Complexities (Average Case) ---
# random.choice(symbols)         - Random Element Selection - O(1) Time
# " | ".join(row)                - String Join - O(N) where N is number of symbols
# row[0] == row[1] == row[2]     - Index Checking - O(1) Time
