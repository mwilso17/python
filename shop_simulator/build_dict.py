# This program builds a dictionary from the inventory.txt file in order for it to be used to register sales.

inventory_file = open("shop_simulator\inventory.txt", "r")

def build_inventory(inventory_file, divider = ","):
  inventory_dict = {}
  try:
    with inventory_file as inventory:
      for item in inventory:
        item = item.strip()
        if divider in item:
          key, value = item.split(divider, 1)
          inventory_dict[key.strip()] = value.strip()
  except FileNotFoundError:
    print("File not found")
  return inventory_dict



current_inventory = build_inventory(inventory_file)

if current_inventory:
  for key, value in current_inventory.items():
    print(f"{key}: {value}")
else:
  print("No data found")