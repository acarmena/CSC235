# Concepts: lists, tuples, and dictionaries 
# -------------------------------------------------------------------------------------

# This tuple stores basic store info
# Tuples are like lists, but they CANNOT be changed 
store_info = ("Grocery Adventure", "123 Python Lane")

# Print a simple welcome message using values from tuple 
print("Welcome to ", store_info[0])
print("Location:", store_info[1])
print("---------------------------------------")

# A list of items the store sells
# Lists are ordered and can be changed (add / remove items)
store_items = ["apple", "bananas", "bread", "milk"]

# A dictionary that maps each item to a price 
# Dictionary stores data as key:value pairs 
# Key --> item name (string)
# value --> price (number)

store_prices = {
    "apple" : 0.75,
    "bananas" : 0.50,
    "bread" : 2.50,
    "milk" : 3.00
}

# This list will hold the items that the user chooses to buy. 
shopping_cart = [] # starts empty 

def show_menu(): # This function prints the main manu / function help us reuse code instead of repeating statements
    print("\nWhat would you like to do?")
    print("1 - View store items")
    print("2 - Add item to cart")
    print("3 - View cart and total")
    print("4 - Quit game")

def show_store_items(): # Shows all the items in the store_items lost and their prices from the store prices dictionary
    print("\n--- Store Items ---")
    # We loop through each item in the list
    for item in store_items:
        # For each item, we look up its price in the dictionary
        price = store_prices[item]
        print(f"- {item} : ${price: .2f}")

def add_item_to_cart(): # This function asks the user which item they want to add and thens adds it to the shopping cast list if it exists
    # Ask the user to type an item name 
    item = input("\nType the name of the item to add: ").strip().lower()

    # Check if the item is in the store_items list 
    if item in store_items:
        # If its exists, add it (append) to the shopping_cart list
        shopping_cart.append(item)
        print(f"{item} has been added to your cart!")
    else:
        # If it doesn't exist, show a message 
        print("Sorry, that item is not in the store.")

def view_cart_and_total(): # Print all the items in the cart and calculates the total price using store_price dictionary
    print("\n--- Your Cart ---")

    # If the cart is empty, tell the user and return early
    if len(shopping_cart) == 0:
        print("Your cart is empty")
        return # exit the function here 
    
    # Create a dictionary to count how many of each item the user has 
    # Example: {"apple" : 2, "bread" : 1}
    item_counts = {}

    # Loop through each item in the cart and count them
    for item in shopping_cart:
        #if item is not in the dictionary yet, start at 1
        if item not in item_counts:
            item_counts[item] = 1
        else: 
            # If it already exists, add 1 to the count 
            item_counts[item] += 1

    total_cost = 0 # this will hold the sum of all item prices 

    # Now loop through the counted items to display them neatly 
    for item, count in item_counts.items():
        # Loopk up the price of the item in the store_prices dictionary
        price = store_prices[item]
        # Calculate subtotal for this item (Price * quantity)
        subtotal = price * count 
        # Add the running total 
        total_cost += subtotal
        print(f"{item} x {count} = ${subtotal: .2f}")

    # After the loop, print the total cost 
    print("-----------------------------------------")
    print(f"Total cost: ${total_cost: .2f}")

#----------------------------Main Game Loop----------------------------------------
# This while loop keeps the game running unt the user chooses to exit
running = True # A boolean variable to control the loop 

while running:
    # Show the menu options one each loop 
    show_menu()

    # Ask the user for their choice
    choice = input("Enter your choice (1-4): ").strip()
    # Use if/elif/else to decided what to do
    if choice == "1":
        # show store items
        show_store_items()
    elif choice == "2":
        # Add item to cart
        add_item_to_cart()
    elif choice == "3":
        # View cart and total 
        view_cart_and_total()
    elif choice == "4":
        # Quit game: change running to False to break the loop 
        running = False 
    else: 
        # If the user types something invalid 
        print("Invalid choice. Please enter 1, 2, 3, or 4.")