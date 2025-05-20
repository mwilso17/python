import matplotlib.pyplot as plt

input = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(input, squares)

ax.set_title("Square value table")
ax.set_xlabel("Inputs")
ax.set_ylabel("Squares")

plt.show()