"""
01_04_linear_regression.py

Project: Build a linear regression engine (y = mx + b) from scratch using a custom Gradient Descent loop.
"""

import random

def predict(x, m, b):
    """The Model: y = mx + b"""
    return m * x + b

def mean_squared_error(x_data, y_data, m, b):
    """The Cost Function: measures how wrong the model is."""
    total_error = 0.0
    for x, y in zip(x_data, y_data):
        total_error += (y - predict(x, m, b))**2
    return total_error / len(x_data)

def train(x_data, y_data, learning_rate=0.01, epochs=1000):
    """
    Gradient Descent loop.
    Iteratively tweaks `m` and `b` to minimize the MSE.
    """
    # Initialize random weights
    m = random.uniform(-1, 1)
    b = random.uniform(-1, 1)
    
    n = len(x_data)
    
    for epoch in range(epochs):
        # 1. Calculate derivatives (gradients) for m and b
        m_gradient = 0
        b_gradient = 0
        
        for x, y in zip(x_data, y_data):
            # Error = (Predicted - Actual)
            error = predict(x, m, b) - y
            # Derivative of MSE with respect to m is 2x(error)
            m_gradient += (2/n) * x * error
            # Derivative of MSE with respect to b is 2(error)
            b_gradient += (2/n) * error
            
        # 2. Update weights (move in the opposite direction of the gradient)
        m -= learning_rate * m_gradient
        b -= learning_rate * b_gradient
        
        # 3. Print progress every 100 epochs
        if epoch % 100 == 0:
            loss = mean_squared_error(x_data, y_data, m, b)
            print(f"Epoch {epoch}: m={m:.4f}, b={b:.4f}, Loss={loss:.4f}")
            
    return m, b

if __name__ == "__main__":
    # Ground truth: y = 2x + 1
    # We want the script to discover that m=2 and b=1 by itself
    x_train = [1.0, 2.0, 3.0, 4.0, 5.0]
    y_train = [3.0, 5.0, 7.0, 9.0, 11.0]
    
    print("Starting Training...")
    print("Target equation: y = 2x + 1")
    print("-" * 30)
    
    # Train the model
    final_m, final_b = train(x_train, y_train, learning_rate=0.05, epochs=500)
    
    print("-" * 30)
    print("Training Complete!")
    print(f"Resulting model: y = {final_m:.2f}x + {final_b:.2f}")
    
    # Test it
    test_x = 10.0
    print(f"\nTesting with x={test_x}:")
    print(f"Predicted y: {predict(test_x, final_m, final_b):.2f} (Expected: 21.00)")
