# Python Banking Program
# - Demonstrates functions, while loops, input validation, and scope!
# - It also utilizes the if __name__ == '__main__' idiom from the previous lesson.

def show_balance(balance):
    print(f"\n💰 Current Balance: ${balance:.2f}")

def deposit():
    print("\n--- Deposit ---")
    amount = input("Enter an amount to deposit: $")
    
    # Input validation (allows decimals by removing ONE decimal point before checking isdigit)
    if not amount.replace('.', '', 1).isdigit():
        print("❌ Invalid input. Please enter a valid number.")
        return 0
        
    amount = float(amount)
    
    if amount <= 0:
        print("❌ Amount must be greater than zero.")
        return 0
        
    print(f"✅ Deposited ${amount:.2f} successfully!")
    return amount

def withdraw(balance):
    print("\n--- Withdraw ---")
    amount = input("Enter an amount to withdraw: $")
    
    if not amount.replace('.', '', 1).isdigit():
        print("❌ Invalid input. Please enter a valid number.")
        return 0
        
    amount = float(amount)
    
    if amount <= 0:
        print("❌ Amount must be greater than zero.")
        return 0
    elif amount > balance:
        print("❌ Insufficient funds!")
        return 0
        
    print(f"✅ Withdrew ${amount:.2f} successfully!")
    return amount

def main():
    balance = 0.0
    is_running = True
    
    print("--- 🏦 Welcome to Python Bank 🏦 ---")
    
    while is_running:
        print("\nWhat would you like to do?")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        match choice:
            case '1':
                show_balance(balance)
            case '2':
                balance += deposit()
            case '3':
                balance -= withdraw(balance)
            case '4':
                is_running = False
                print("\nThank you for banking with us! 👋")
            case _:
                print("\n❌ Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == '__main__':
    main()

# --- ⏱️ Time Complexities (Average Case) ---
"10.50".replace('.', '', 1).isdigit()     # String Validation - O(N) where N is string length
# show_balance(balance)                   # Function Call - O(1)
