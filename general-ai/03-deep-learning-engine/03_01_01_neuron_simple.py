"""
Practice: Build a simple forward-pass neuron pipeline and calculate errors.
"""
import math

def sigmoid_activation(x):
    """Sigmoid function squashes any number into a probability between 0.0 and 1.0."""
    return 1 / (1 + math.exp(-x))

class SimpleNeuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
        
    def forward(self, inputs):
        # 1. Dot Product (multiply inputs by weights and sum them up)
        dot_product = sum(i * w for i, w in zip(inputs, self.weights))
        
        # 2. Add Bias
        z = dot_product + self.bias
        
        # 3. Activation: Sigmoid
        # This will squash our dot_product result into a clean 0.0 to 1.0 Probability.
        output = sigmoid_activation(z)
        
        return output

if __name__ == "__main__":
    # Our simplified "Network" is now just a single active neuron.
    # It has 2 weights strictly because our input data has 2 features.
    neuron = SimpleNeuron(weights=[0.5, -0.6], bias=0.1)
    
    # We pass in two features (e.g. House Size, Num Bedrooms)
    data_input = [2.0, 1.5]
    
    # Target MUST be between 0.0 and 1.0 because we are using Sigmoid!
    # e.g., 1.0 means "Yes, this is definitely a house we want to buy"
    target_output = 1.0
    
    print("--- Network Parameters ---")
    print(f"Single Neuron: weights={neuron.weights}, bias={neuron.bias}")
    print("--------------------------\n")

    print(f"Input Data: {data_input}")
    
    # The "Forward Pass" is now just passing data through this single neuron
    prediction = neuron.forward(data_input)
    print(f"Final Prediction: {prediction:.4f}")
    
    # Calculate Error (Mean Squared Error)
    error = (target_output - prediction) ** 2
    
    print("-" * 30)
    print(f"Target: {target_output}")
    print(f"Cost/Error (MSE): {error:.4f}")

