# The goal of this program is to simulate a pizza restaurant taking an order from a customer and giving them a price based on their selections.
# The program takes an order via input statements, notifies the customer if any items are unavailable, prints the request, and gives them a price for the order.

store_sizes = ['small', 'medium', 'large', 'x-large']

store_crusts = ['thin', 'hand tossed', 'stuffed crust']

store_toppings = ['pepperoni', 'bacon', 'sausage', 'ham', 'pineapple', 'mushrooms', 'onions', 'green peppers']

tax = .08


customer_order = input('Thank you for choosing the pizza restaurant! What size pizza do you want? (s/m/l/xl): ')

if customer_order == 's':
  total = 6
  print(f'Ok, one small pizza! That will be ${total}')
if customer_order == 'm':
  total = 8
  print(f'Ok, one small pizza! That will be ${total}')
if customer_order == 'l':
  total = 10
  print(f'Ok, one small pizza! That will be ${total}')
if customer_order == 'xl':
  total = 12
  print(f'Ok, one small pizza! That will be ${total}')