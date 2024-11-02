import matplotlib.pyplot as plt

# Coordinates of the two points
x_values = [209, 452, 15]
y_values = [25, 36, 51]

# Plotting the line between the two points
plt.plot(x_values, y_values, marker='o', color='blue', linestyle='-')
# plt.scatter(x, y, s=100, c='blue')
# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Between Two Points')

# Displaying the plot
plt.show()
