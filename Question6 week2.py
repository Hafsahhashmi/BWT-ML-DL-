#Question 6
#Write a code for function `update_inventory(inventory_dict, item, quantity)` that will:
#1. Take a dictionary where keys are item names and values are quantities, an item name, and a quantity to add or remove.
#2. Updates the inventory by adding or removing the specified quantity (use negative values for removal).
#3. Ensures that the quantity of any item does not go below zero.
#4. Returns the updated dictionary.
#Use this function to
#1. Initialize an inventory dictionary with at least 5 items.
#2. Prompt the user to update the inventory by adding or removing quantities of 3 items.
#3. Display the updated inventory.

def update_inventory(inventory_dict, item, quantity):
    if item in inventory_dict:
        # Update the quantity, ensuring it does not go below zero
        inventory_dict[item] = max(0, inventory_dict[item] + quantity)
    else:
        # Add the item to the inventory if it doesn't exist, ensuring non-negative quantity
        inventory_dict[item] = max(0, quantity)
    
    return inventory_dict

#Code:

def main():
    # Initialize inventory with at least 5 items
    inventory = {
        "pens": 10,
        "pencils": 5,
        "brushes": 8,
        "copies": 12,
        "sheets": 6
    }
    
    print("Initial inventory:", inventory)

    # Prompt the user to update the inventory for 3 items
    for _ in range(3):
        item = input("Enter the item name to update: ")
        quantity = int(input(f"Enter the quantity to add/remove for {item} (use negative values for removal): "))
        inventory = update_inventory(inventory, item, quantity)

    # Display the updated inventory
    print("Updated inventory:", inventory)

if __name__ == "__main__":
    main()
