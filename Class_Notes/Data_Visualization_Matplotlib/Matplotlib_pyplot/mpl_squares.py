import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt

# chart values
x_values = [1, 2, 3, 4, 5]
y_values_squared = [1, 4, 9, 16, 25]

# chart type
plt.plot(x_values, y_values_squared, linewidth=5)

# set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# set size of tick labels
plt.tick_params(axis="both", labelsize=14)

plt.show()
