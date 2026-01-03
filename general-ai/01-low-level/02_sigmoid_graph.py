import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    """Calculates the sigmoid function."""
    return 1 / (1 + np.exp(-x))


# Sample data
x_values = np.linspace(-10, 10, 100)  # Create 100 evenly spaced numbers from -10 to 10
y_values = sigmoid(x_values)

# Data for specific examples
specific_x = [-5, -2, 0, 2, 5]
specific_y = sigmoid(np.array(specific_x))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Sigmoid Function')
plt.scatter(specific_x, specific_y, color='red', label='Specific Points')

# Annotating specific points
for i in range(len(specific_x)):
    plt.annotate(f'({specific_x[i]}, {specific_y[i]:.2f})',
                 (specific_x[i], specific_y[i]),
                 textcoords="offset points",
                 xytext=(0, 10),
                 ha='center')

plt.xlabel('Input (x)')
plt.ylabel('Sigmoid Output (σ(x))')
plt.title('Sigmoid Function Visualization')
plt.grid(True)
plt.legend()
plt.show()

print("Specific x values and their sigmoid outputs:")
for x, y in zip(specific_x, specific_y):
    print(f"x = {x}, sigmoid(x) = {y:.4f}")
