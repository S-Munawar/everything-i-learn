# Concession Stand Program
# - This program demonstrates using dictionaries to store a menu and lists to keep track of a user's cart.

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25
}

cart = []
total = 0

print("--------- MENU ---------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None: # Using .get() prevents KeyError if item doesn't exist
        cart.append(food)
        total += menu.get(food)
    else:
        print("❌ Item not found on the menu. Please try again.")

print("\n------ YOUR ORDER ------")
for food in cart:
    print(food, end=" ")
print()

print("------------------------")
print(f"Total is: ${total:.2f}")

# --- ⏱️ Time Complexities (Average Case) ---
menu.get('pizza')        # Dict Access - O(1)
cart.append('pizza')     # List Append - O(1)

for food in cart:        # Iterating List - O(N)
    pass
