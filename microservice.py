import json
import os.path


def update_inventory():
    # open inventory totals file - if empty set inventory to empty dictionary
    if os.path.getsize('inventory_totals.json') == 0:
        inventory = {}
    else:
        with open('inventory_totals.json', 'r') as f:
            inventory = json.load(f)
    # open the json file with data to be added
    with open('inventory.json', 'r') as i:
        data = json.load(i)
    # store values
    name = data['name']
    price = data['price']
    quantity = data['quantity']
    # if item exists in inventory, increment quantity and total value
    if name in inventory:
        inventory[name]['quantity'] += quantity
        inventory[name]['total'] += (quantity * price)
    # if item is not in inventory, add new item with data from input json file
    else:
        inventory[name] = {'quantity': quantity, 'total': quantity * price}

    # write the updated inventory to inventory totals json file
    with open('inventory_totals.json', 'w') as f:
        json.dump(inventory, f)


update_inventory()
