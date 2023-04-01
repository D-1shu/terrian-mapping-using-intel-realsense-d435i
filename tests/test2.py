import matplotlib.pyplot as plt

# Heights and weights data
heights = [63, 64, 66, 69, 69, 71, 71, 72, 73, 75]
weights = [127, 121, 142, 157, 162, 156, 169, 165, 181, 208]

# Create the scatter plot
plt.scatter(heights, weights)

# Add labels and title
plt.xlabel('Height (inches)')
plt.ylabel('Weight (pounds)')
plt.title('Scatter Plot of Heights and Weights')

# Show the plot
plt.show()