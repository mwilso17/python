# This program builds a dictionary from the inventory.txt file in order for it to be used to register sales.

inventory_file = "shop_simulator\inventory.txt"

def build_inventory(inventory_file, divider = ","):
  inventory_dict = {}
  try:
    with open(inventory_file, "r") as inventory:
      for item in inventory:
        item = item.strip()
        product_info = item.split(',')
        if len(product_info) == 3:
          product = product_info[0].strip()
          price = product_info[1].strip()
          quantity = product_info[2].strip()
          inventory_dict[product] = [price, quantity]
  except FileNotFoundError:
    print("File not found")
  return inventory_dict

# TODO: check if product is in stock before decrementing inventory and print message stating if something is out of stock. 
def decrease_inventory(inventory, product_sold):
  current_quantity = int(inventory[product_sold][1])
  if product_sold in inventory and current_quantity > 0:
    old_quantity = int(inventory[product_sold][1])
    new_quantity = str(old_quantity - 1)
    inventory[product_sold][1] = new_quantity

    with open(inventory_file, "w") as file:
      for key, value in inventory.items():
        file.write(f"{key} , {value[0]} , {value[1]} \n")

  elif current_quantity == 0:
    print(f"We are out of {product_sold}. Please check back later.")
        
  else:
    print(f"We either don't carry {product_sold}.")

  




# Delete below when not testing. This is used for testing purposes
current_inventory = build_inventory(inventory_file)

if current_inventory:
  for key, value in current_inventory.items():
    print(f"{key}: {value[0]} and {value[1]}")
else:
  print("No data found")
print("\n")

decrease_inventory(current_inventory, "Burger")
decrease_inventory(current_inventory, "Soda")
decrease_inventory(current_inventory, "Soda")
decrease_inventory(current_inventory, "Fries")
decrease_inventory(current_inventory, "Burger")

if current_inventory:
  for key, value in current_inventory.items():
    print(f"{key}: {value[0]} and {value[1]}")
else:
  print("No data found")
print("\n")