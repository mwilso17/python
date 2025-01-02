# The goal of this program is to simulate a pizza restaurant taking an order from a customer and giving them a price based on their selections.
# The program takes an order via input statements, notifies the customer if any items are unavailable, prints the request, and gives them a price for the order.

#TODO: store sales seperately. Calculate sales at end of day.
#TODO: calculate costs vs sales.
#TODO: Cash vs credit sales
#TODO: Delivery system vs store pick up.
class Pizza:
  def __init__(self, size="", toppings=None):
    self.size = size
    self.toppings = toppings if toppings else []
    self.price = self.calculate_price()

  def calculate_price(self):
    #TODO: Add crust types (thin, hand tossed, new york, stuffed crust, and price accordingly)
    #TODO: Look into other ways to handle topping size price difference.
    #TODO: Add premium pizza toppings with own price list (ie: bacon, chicken, stake, and shittake mushrooms cost double the normal topping price)
    #TODO: Add taxes! Cause taxes are a thing. 
    #TODO: Add tipping system, cause why not.
    base_price = {"small": 5.99, "medium": 9.99, "large": 11.99}

    if self.size == "small":
      topping_price = 1
    elif self.size == "large":
      topping_price = 2
    elif self.size == "medium":
      topping_price = 1.5

    return base_price[self.size] + (topping_price * len(self.toppings))
  
  def __str__(self):
    return f"{self.size} pizza topped with {', '.join(self.toppings)} - total: ${self.price}!"
  
def order_food():
  size = input("What size pizza do you want? (small, medium, large): ")
  toppings = []
  while True:
    #TODO: If someone types in multiple toppings seperated as a comma, program only tallys for 1 topping. Need to fix.
    #TODO: Program repeats the topping input line after every press of 'return'. Need it to be less repetitive.
    #TODO: Program currently allows anything to be input in topping (ie: you can put shoes as a topping). Need to have users only select from a list of approved toppings.
    #TODO: Extra thoughts: add wings, drinks, and bread items to menu.
    #TODO: Extra thoughts: Add 'out of stock' toppings and items and let customer know if a requested item is out of stock. 
    topping = input("What toppings would you like? When finished, type 'done'. :") 
    if topping.lower() == "done":
      break
    toppings.append(topping)
  
  return Pizza(size, toppings)


if __name__ == "__main__":
  print("Welcome to your local pizza restaurant!")
  order = []

  while True:
    pizza = order_food()
    order.append(pizza)
    order_more = input("Would you like to order more? (y/n): ")
    if order_more.lower() == 'n':
      break

  print("\nYou ordered: ")
  total_price = 0
  for pizza in order:
    print(pizza)
    total_price += pizza.price

  print(f"\nYour total price is: ${total_price}.")