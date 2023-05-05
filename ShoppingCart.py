#array
shopping_cart = {}

#while loop with try except to check inputs
print("Welcome to the shop! Enter your products below.")
while True:
    name = input("Enter product name: ")
    while len(name)==0:
        print("You must enter a name.")
        name = input("Enter product name: ")
    try:
        price = float(input("Enter product price: "))
        while price <= 0:
            print("Only postive numbers are accepted.")
            price = float(input("Enter product price: "))
    except ValueError:
        print("Price must be a number.")
        continue
    shopping_cart[name] = price
    print(f"{name} added!")

    sel = input("Add another item? (y/n) ")
    while sel not in ['y', 'n']:
        print("Invalid choice.")
        sel = input("Add another item? (y/n) ")
    if sel == 'n':
        break

#printer
total = sum(shopping_cart.values())
print(f"Total shopping cart cost: ${total:.2f}")