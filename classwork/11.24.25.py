#-------------------------------------------------------------------------------------------
# Simple Inventory System using Python collections 
# This program:
# - Uses a LIST to keep track of the item names 
# - Uses a TUPLE to store menu options (they never change)
# - Uses SET to track low-stock items
# - Uses a DICTIONARY to store item details (quantity and price)
# - USES functions, Loops, and IF/ELIF/ELSE for control flow 
# - USES try & except change str to integer / float for quantity and price 
#--------------------------------------------------------------------------------------------

#------------ DATA STRUCTURES ---------------------
# Dictionary to hold our inventory
# key = item name (string)
# Value = quantity and price 
inventory = {
    "apple" : {"qty": 10, "price": 0.99},
    "bananas" : {"qty": 5, "price": 0.59}
}

# List to keep an ordered list of item names 
# This helps us print items in a consistent order/
item_names = list(inventory.keys())

# Tuple to store menu options that should NOT change 
menu_options = (
    "1. View Inventory",
    "2. Add new item",
    "3. Update item quantity",
    "4. Mark item as low stock",
    "5. View low-stock items",
    "6. Quit"
)

# Set to store items that are low stock
low_stock_items = set()

#--------------- HELPER FUNCTIONS ------------------

# Print the menu using our tuple of options,
# This function shows how we can LOOP over a TUPLE 
def print_menu():
    print("\n=== Simple Inventory System ===")
    for option in menu_options: # Loop through the tuple
        print(option)

# This function display all the items in the inventory dictionary. Shows how we LOPP through
# a dictionary and use a LIST for order 
def view_inventory():
    if not inventory: # If the dictionary is empty
        print("\nInventory is empty.")
        return

    print("\n--- Current Inventory ---")
    # Loop through our list of item names so we have stable order
    for name in item_names:
        details = inventory[name]
        qty = details["qty"]
        price = details["price"]
        # Mark if item is low stock
        low_flag = " (LOW STOCK)" if name in low_stock_items else ""
        print(f" - {name.title()}: {qty} in stock at ${price: .2f}{low_flag}")

# This function add a new item to the inventory. Shows how we READ input and UPDATE our Dictionary
# and LIST 
def add_item():
    print("\n--- Add New Item ---")
    name = input("Enter item name: ").strip().lower()

    # IF the name is empty, we stop early
    if not name:
        print("Item name cannot be empty.")
        return
    
    # If item already exists, we tell the user to update instead 
    if name in inventory:
        print("Item already exists. Use 'update item quantity' instead.")
        return
    
    # Get the quantity from the user 
    qty_str = input("Enter starting quantity: ").strip()
    price_str = input("Enter item price (e.g., 1.99): ").strip()

    # Use try/except to safely convert the strings to number 
    try:
        qty = int(qty_str)
        price = float(price_str)
    except ValueError:
        print("Quantity must be an integer and price must be a number.")
        return
    
    # Add the new item to the inventory dictionary
    inventory[name] = {"qty": qty, "price": price}

    # Add the new name to our list of item names 
    item_names.append(name)

    print(f"Added '{name}' with quantity {qty} and price ${price:.2f}.")

# This function updates the quantity of an existing item.
# Demonstrates IF/ELIF/ELSE logic based on user input. 
def update_quantity():
    print("\n--- Update Item Quantity ---")
    name = input("Enter item name to update: ").strip().lower()

    if name not in inventory:
        print("That item does not exist in the inventory.")
        return
    
    qty_str = input("Enter new quantity: ").strip()

    try: 
        new_qty = int(qty_str)
    except ValueError:
        print("Quantity must be an integer.")
        return
    
    # Update the quantity in the dictionary
    inventory[name]["qty"] = new_qty
    print(f"Updated '{name}' quantity to {new_qty}.")

    # If quantity is low (for example, <=3), add it to low_stock_items set 
    if new_qty <=3:
        low_stock_items.add(name)
        print(f"Note: '{name}' is now marked as LOW STOCK.")
    else: 
        # If quantity is not low anymore, remove from low_stock_items set
        if name in low_stock_items:
            low_stock_items.remove(name)
            print(f" '{name}' removed from LOW STOCK list.")

# This function manually marks an item as low stock. 
# Shows how we use a SET to track unique items.
def mark_low_stock():
    print("\n--- Mark Items as Low Stock ---")
    name = input("Enter item name to mark as low stock: ").strip().lower()

    if name not in inventory:
        print("That item does not exist in the inventory.")
    
    # Add the item to the set
    low_stock_items.add(name)
    print(f" '{name}' has been marked as LOW STOCK.")

# This function views all the items currently marked as low stock.
# Shows how we LOOP through a SET. 
def view_low_stock_items():
    print("\n--- Low Stock Items ---")
    if not low_stock_items:
        print("No items are currently marked as low stock.")
        return
    
    for name in low_stock_items:
        qty = inventory[name]["qty"]
        print(f"- {name.title()} (Qty: {qty})")

#--------------------------- Main Program Loop -----------------------------------
# Main function that runs the program loop. Use WHILE loop and IF/ELIF/ELSE to handle choice.
def main():
    while True:
        print_menu # Show the menu at the top of each loop iteration 

        # Ask the user for their choice 
        choice = input("\nChoose an option (1-6): ").strip()

        # IF/ELIF/ELSE to handle each option 
        if choice == "1":
            view_inventory()
        elif choice == "2":
            add_item()
        elif choice == "3":
            update_quantity()
        elif choice == "4":
            mark_low_stock()
        elif choice == "5":
            view_low_stock_items()
        elif choice == "6":
            # option 6 means quit the program
            print("Goodbye! Thanks for using the inventory system.")
            break
        else:
            # Have any invalid menu input 
            print("Invalid choice. Please enter a number from 1 to 6.")

# This line makes sure main() only run when this file is executed directly
# it will not run if this file is imported somwhere else.
if __name__ == "__main__":
    main()