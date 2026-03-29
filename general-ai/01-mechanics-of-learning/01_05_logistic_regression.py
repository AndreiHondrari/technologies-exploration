"""
01_05_logistic_regression.py

Project: Upgrade our Linear Regression engine (y=mx+b) by wrapping it in a Sigmoid function.
This converts it into a Logistic Regression classifier that outputs a probability (0.0 to 1.0).
"""

import random
import math

def sigmoid(x):
    """Squashes any infinite number to be strictly between 0.0 and 1.0."""
    # math.exp(-x) is e^(-x). We clamp x to prevent giant math overflows.
    x = max(min(x, 100), -100) 
    return 1 / (1 + math.exp(-x))

def predict_linear(x, m, b):
    """Step 1: The standard linear equation (can be any giant number)."""
    return m * x + b

def predict_probability(x, m, b):
    """Step 2: Take the linear output and squash it into a % probability."""
    linear_output = predict_linear(x, m, b)
    return sigmoid(linear_output)

def binary_cross_entropy_loss(x_data, y_data, m, b):
    """
    Cost Function for Classification (Log Loss).
    MSE is great for straight lines, but for probabilities (0 or 1), 
    Log Loss heavily punishes being highly confident about the WRONG answer!
    """
    total_error = 0.0
    for x, y in zip(x_data, y_data):
        prob = predict_probability(x, m, b)
        # Prevent math.log(0) crash by clipping prob slightly
        prob = max(min(prob, 0.9999), 0.0001)
        
        # If true answer is 1: punish for making prob closer to 0
        if y == 1:
            total_error -= math.log(prob)
        # If true answer is 0: punish for making prob closer to 1
        else:
            total_error -= math.log(1 - prob)
            
    return total_error / len(x_data)

def train(x_data, y_data, learning_rate=0.1, epochs=2000):
    m = random.uniform(-1, 1)
    b = random.uniform(-1, 1)
    n = len(x_data)
    
    for epoch in range(epochs):
        m_gradient = 0
        b_gradient = 0
        
        for x, y in zip(x_data, y_data):
            # Error = (Predicted Probability - Actual Answer)
            error = predict_probability(x, m, b) - y
            
            # The calculus derivative for Logistic Regression simplifies beautifully to:
            m_gradient += (1/n) * x * error
            b_gradient += (1/n) * error
            
        m -= learning_rate * m_gradient
        b -= learning_rate * b_gradient
        
        if epoch % 500 == 0:
            loss = binary_cross_entropy_loss(x_data, y_data, m, b)
            print(f"Epoch {epoch}: m={m:.4f}, b={b:.4f}, LogLoss={loss:.4f}")
            
    return m, b

if __name__ == "__main__":
    # Let's say we are classifying if a student "Passes" (1) or "Fails" (0) based on hours studied (x)
    hours_studied = [1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0]
    passed_exam =   [0,   0,   0,   0,   1,   1,   1] # Notice it jumps abruptly from 0 to 1 at 4 hours
    
    print("Training Logistic Regression Model (Classifier)...")
    final_m, final_b = train(hours_studied, passed_exam, learning_rate=0.5, epochs=3000)
    
    print("-" * 40)
    print(f"Final Model: y = sigmoid({final_m:.2f}x + {final_b:.2f})")
    
    # Let's test it on unseen data
    test_hours = [2.5, 3.5, 4.5]
    print("\nTesting new students:")
    for h in test_hours:
        prob = predict_probability(h, final_m, final_b)
        chance = prob * 100
        decision = "PASS" if prob >= 0.5 else "FAIL"
        print(f"Studied {h} hrs --> {chance:.1f}% chance of passing => {decision}")
