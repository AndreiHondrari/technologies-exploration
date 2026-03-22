def predict(x, m, b):
    """
    Calculate y = mx + b for a single input x.
    In AI, 'm' is the Weight and 'b' is the Bias.
    """
    return m * x + b

def mean_squared_error(x_train, y_train, m, b):
    """
    Calculate the average of (prediction - actual)^2 for all points.
    This is our 'Cost Function' or 'Loss Function'.
    """
    total_error = 0.0
    n = len(x_train)

    for i in range(n):
        prediction = predict(x_train[i], m, b)
        actual = y_train[i]
        error = (prediction - actual) ** 2
        total_error += error
    
    return total_error / n


# --- Execution ---

# 1. The Data (Ground Truth)
# We want the model to learn the pattern: y = 2x
x_data = [1.0, 2.0, 3.0, 4.0]
y_data = [2.0, 4.0, 6.0, 8.0]

# 2. The "Dumb" Model
# Initial random guesses for weight (m) and bias (b)
m = 0.5
b = 0.0

print(f"Model: y = {m}x + {b}")

# 3. Evaluate
error = mean_squared_error(x_data, y_data, m, b)

print(f"Mean Squared Error: {error:.4f}")
# Goal: We want this error to be 0.0.
# Currently, for x=4, model predicts 0.5*4 = 2.0. Real is 8.0. Error is huge!