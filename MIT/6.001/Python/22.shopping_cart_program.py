# Shopping Cart Program

print("--- 🛒 Welcome to the Shopping Cart Program 🛒 ---")

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    
    price_input = input(f"Enter the price of a {food}: $")
    
    try:
        price = float(price_input)
        foods.append(food)
        prices.append(price)
    except ValueError:
        print("Invalid input. Please enter a valid number for the price.")

print("\n--- 🧾 Your Receipt 🧾 ---")

for i in range(len(foods)):
    print(f" - {foods[i]:<15} ${prices[i]:.2f}")
    total += prices[i]

print("-" * 25)
print(f"Total:{' '*10} ${total:.2f}")
print("-------------------------")
