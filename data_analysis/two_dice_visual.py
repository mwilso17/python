from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Die

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
  result = die_1.roll() + die_2.roll()
  results.append(result)

# print(results)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
  frequency = results.count(value)
  frequencies.append(frequency)

# print(frequencies)

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title" : "Result", "dtick" : 1}
y_axis_config = {"title" : "Frequency of Results"}
layout = Layout(title='Results of rolling two D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data" : data, "layout": layout})