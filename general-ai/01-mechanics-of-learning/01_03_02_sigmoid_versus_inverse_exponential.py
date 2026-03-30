import numpy as np
import matplotlib.pyplot as plt

# Enable dark mode for the plot
plt.style.use('dark_background')


def sigmoid(x):
    """Calculates the sigmoid function."""
    return 1 / (1 + np.exp(-x))

def exponential(x):
    """Calculates the exponential function."""
    return np.exp(x)

def inverse_exponential(x):
    """Calculates 1 divided by exponential function."""
    return 1 / np.exp(x)  # Same as np.exp(-x)

def inverse_sigmoid(x):
    """Calculates 1 divided by (1 + exponential of positive x)."""
    return 1 / (1 + np.exp(x))

# Sample data
x_values = np.linspace(-5, 5, 100)  # Create 100 evenly spaced numbers from -5 to 5
y_sigmoid = sigmoid(x_values)
y_exp = exponential(x_values)
y_inv_exp = inverse_exponential(x_values)
y_inv_sigmoid = inverse_sigmoid(x_values)

# Data for specific examples
specific_x = [-3, -1, 0, 1, 3]
specific_sigmoid = sigmoid(np.array(specific_x))
specific_exp = exponential(np.array(specific_x))
specific_inv_exp = inverse_exponential(np.array(specific_x))
specific_inv_sigmoid = inverse_sigmoid(np.array(specific_x))

# Special overlay figure: y_inv_exp, y_sigmoid, and y_inv_one_plus_x
fig = plt.figure(figsize=(12, 8))
fig.canvas.manager.set_window_title('Function Overlay Comparison')
fig.suptitle('Overlay: 1/Exponential vs Sigmoid', fontsize=16, color='white')
plt.plot(x_values, y_inv_exp, label='1/Exponential (e^-x)', color='magenta', linewidth=2)
plt.plot(x_values, y_sigmoid, label='Sigmoid (1/(1+e^-x))', color='yellow', linewidth=2)

# Plot specific points for overlay functions
plt.scatter(specific_x, specific_inv_exp, color='magenta', s=50, zorder=5)
plt.scatter(specific_x, specific_sigmoid, color='yellow', s=50, zorder=5)

plt.xlabel('Input (x)')
plt.ylabel('Function Output')
plt.title('Overlay: 1/Exponential vs Sigmoid')
plt.grid(True, alpha=0.3)
plt.legend()
plt.ylim(-2, 5)  # Adjusted limits for better visualization of these three functions

# Display both figures simultaneously
plt.show()

print("Comparison of functions at specific x values:")
print(f"{'x':>4} {'Exponential':>12} {'1/Exponential':>14} {'Sigmoid':>10}")
print("-" * 80)
for x, exp_val, inv_exp_val, sig_val in zip(specific_x, specific_exp, specific_inv_exp, specific_sigmoid):
    print(f"{x:>4} {exp_val:>12.4f} {inv_exp_val:>14.4f} {sig_val:>10.4f}")

