from dice import Die

die = Die()

results = []
for roll_num in range(10):
  result = die.roll()
  results.append(result)

print(results)