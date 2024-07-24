import matplotlib.pyplot as plt

# chart values
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
x_values = list(range(1, 51))
y_values = [x**2 for x in x_values]

# chart type basic color and RGB
# # color 'c' is default 'blue'. Can also use RGB (0, 0, 0.8) with values between and including 0 and 1
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolors='none', s=40)

# chart type colormaps
# https://matplotlib.org/stable/tutorials/colors/colormaps.html
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.viridis_r, edgecolors='none', s=40)
# viridis is a sequential color gradient. 'viridis_r' reverses the color gradient or use .reversed()

# emphasize the first and last points
plt.scatter(x_values[0], y_values[0], c='green', edgecolor='none', s=100)
plt.scatter(x_values[-1], y_values[-1], c='orange', edgecolor='none', s=100)

# set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# hide the axes
# plt.gca().get_xaxis().set_visible(False)
# plt.gca().get_yaxis().set_visible(False)

# set the range for each axis
plt.axis([0, 60, 0, 3000])  # min and max values for x-axis and y-axis

# set size of tick labels
plt.tick_params(axis="both", which="major", labelsize=12)

# # alter the size to fill the screen ---- DOES NOT WORK
# plt.figure(figsize=[10, 6])

# save plots automatically
# plt.savefig("squares_plot.png", bbox_inches="tight")

# show plot
plt.show()
