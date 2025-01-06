# The goal of this program is to simulate a pizza restaurant taking an order from a customer and giving them a price based on their selections.
# The program takes an order via input statements, notifies the customer if any items are unavailable, prints the request, and gives them a price for the order.

#TODO: store sales seperately. Calculate sales at end of day.
#TODO: calculate costs vs sales.
#TODO: Cash vs credit sales
#TODO: Delivery system vs store pick up.
store_toppings = ["pepperoni", "bacon", "sausage", "salami", "ham", "chicken", "mushrooms", "green peppers", "black olives", "pineapple", "onions", "done"]

class Pizza:
  def __init__(self, size="", crust="", toppings=None):
    self.size = size
    self.crust = crust
    self.toppings = toppings if toppings else []
    self.price = self.calculate_price()

  def calculate_price(self):
    #TODO: Look into other ways to handle topping size price difference.
    #TODO: Add premium pizza toppings with own price list (ie: bacon, chicken, stake, and shittake mushrooms cost double the normal topping price)
    #TODO: Add tipping system, cause why not.
    base_price = {"small": 5.99, "medium": 9.99, "large": 11.99}
    crust_price = {"regular": 0, "stuffed": 2, "thin": 0}

    if self.size == "small":
      topping_price = 1
    elif self.size == "large":
      topping_price = 2
    elif self.size == "medium":
      topping_price = 1.5

    return base_price[self.size] + crust_price[self.crust] + (topping_price * len(self.toppings))
  
  def __str__(self):
    return f"{self.size} {self.crust} pizza topped with {', '.join(self.toppings)} - total: ${self.price}!"


#TODO: Tax calculates but doesn't leave trailing 0s where needed (like ordering a small plain pizza leaves sales tax at .3 instead of .30).
def calculate_tax(sub_total, sales_tax_rate):

  return round(sub_total * sales_tax_rate, 2)

def calculate_total_price(sub_total, sales_tax_amount, delivery_fee=0):

  return sub_total + sales_tax_amount + delivery_fee

def get_valid_toppings(ordered_toppings, store_toppings):
  while True:
    customer_toppings = input(ordered_toppings)
    if customer_toppings in store_toppings:
      return customer_toppings
    if "," in customer_toppings:
      print("Please enter toppings one at a time.")
    else:
      print(f"That is not a valid topping. Please choose from: {store_toppings}")
  
def order_food():
  size = input("What size pizza do you want? (small, medium, large): ")
  crust = input("What type of crust would you like? (regular, stuffed, thin): ")
  toppings = []
  while True:
    #TODO: Program repeats the topping input line after every press of 'return'. Need it to be less repetitive.
    #TODO: Find way to remove the 'done' option from the store_toppings. Doesn't really make sense but keeps the code funcitioning for now.
    #TODO: Extra thoughts: add wings, drinks, and bread items to menu.
    #TODO: Extra thoughts: Add 'out of stock' toppings and items and let customer know if a requested item is out of stock. 
    topping = get_valid_toppings("What toppings would you like? (when finsihed, type 'done') : ", store_toppings)
    if topping.lower() == "done":
      break
    toppings.append(topping)
  
  return Pizza(size, crust, toppings)

def get_customer_address():

  street = input("Enter street address: ")
  city = input("Enter city: ")
  state = input("Enter state: ")
  zipcode = input("Enter zip code: ")

  return {
      "street": street,
      "city": city,
      "state": state,
      "zipcode": zipcode
  }

if __name__ == "__main__":
  print("Welcome to your local pizza restaurant!")
  order = []
  sales_tax_rate = .05

  delivery_option = input("Is this for delivery? (y/n): ")

  if delivery_option == "y":
    address = get_customer_address()
    delivery_fee = 2.99
  if delivery_option == "n":
    print("Ok. We will prepare your order for pick up in the store.")

  while True:
    pizza = order_food()
    order.append(pizza)
    order_more = input("Would you like to order more? (y/n): ")
    if order_more.lower() == 'n':
      break

  print("\nYou ordered: ")
  sub_total = 0
  for pizza in order:
    print(pizza)
    sub_total += pizza.price

  print(f"\nYour sub total is: ${sub_total}.")

  sales_tax = calculate_tax(sub_total, sales_tax_rate)

  print(f"\nSales tax is: ${sales_tax}.")

  total_price = calculate_total_price(sub_total, sales_tax, delivery_fee=0)

  print(f"\nYour total amount is: ${total_price}")

  if delivery_option == "y":
    print(f"We will deliver your pizza to {address} soon!")
  else:
    print("Your order will be ready for pickup in the store soon!")