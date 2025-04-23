import datetime

# Medicine inventory format: { 'medicine_name': { 'quantity': int, 'price': float } }
inventory = {}

# Sales history format: list of dicts
sales_history = []

def add_medicine(name, quantity, price):
    if name in inventory:
        inventory[name]['quantity'] += quantity
    else:
        inventory[name] = {'quantity': quantity, 'price': price}
    print(f"{quantity} units of '{name}' added to inventory.")
# cORRECTED
def view_inventory():
    print("\n--- Inventory ---")
    if not inventory:
        print("No medicine in stock.")
        return
    for name, details in inventory.items():
        print(f"{name} | Quantity: {details['quantity']} | Price: ${details['price']:.2f}")
#git you
def sell_medicine(name, quantity):
    if name not in inventory:
        print(f"'{name}' is not in stock.")
        return
    if inventory[name]['quantity'] < quantity:
        print(f"Only {inventory[name]['quantity']} units available for '{name}'.")
        return

    total_price = quantity * inventory[name]['price']
    inventory[name]['quantity'] -= quantity
    sale_record = {
        'medicine': name,
        'quantity': quantity,
        'total_price': total_price,
        'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    sales_history.append(sale_record)
    print(f"Sold {quantity} units of '{name}' for ${total_price:.2f}")

def view_sales():
    print("\n--- Sales History ---")
    if not sales_history:
        print("No sales made yet.")
        return
    for sale in sales_history:
        print(f"{sale['date']} | {sale['medicine']} | Quantity: {sale['quantity']} | Total: ${sale['total_price']:.2f}")

def main():
    while True:
        print("\n=== Pharmacy Inventory System ===")
        print("1. Add Medicine")
        print("2. View Inventory")
        print("3. Sell Medicine")
        print("4. View Sales History")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == '1':
            name = input("Enter medicine name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per unit: "))
            add_medicine(name, quantity, price)
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            name = input("Enter medicine name to sell: ")
            quantity = int(input("Enter quantity to sell: "))
            sell_medicine(name, quantity)
        elif choice == '4':
            view_sales()
        elif choice == '5':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option. Please select 1-5.")

if __name__ == "__main__":
    main()
