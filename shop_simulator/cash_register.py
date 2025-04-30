# This program records a sale and stores in in sales.txt for future use.
import datetime

sales_file = open("shop_simulator\sales.txt", "a")

def get_timestamp():
  timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  try:
    with sales_file as file: 
      file.write(timestamp + " , " + "\n")
    print("Timestamp recorded")
  except Exception as e:
    print(f"An error occurred: {e}")