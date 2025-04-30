# This program builds a dictionary from the inventory.txt file in order for it to be used to register sales.

inventory_file = open("shop_simulator\inventory.txt", "r")

def build_inventory(inventory_file, divider = ","):
  inventory_dict = {}
  try:
    with inventory_file as inventory:
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


# Delete below when not testing. Will be used in the main cash register program.
current_inventory = build_inventory(inventory_file)

if current_inventory:
  for key, value in current_inventory.items():
    print(f"{key}: {value[0]} and {value[1]}")
else:
  print("No data found")