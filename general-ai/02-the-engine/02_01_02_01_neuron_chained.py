"""
Practice: Chain two single neurons together sequentially (Hidden -> Output).

ACTIVATION FUNCTIONS CHEAT SHEET:
---------------------------------
1. ReLU (Rectified Linear Unit):
   - When to use: Almost always used in HIDDEN layers.
   - Why: It's computationally very fast. It simply lets positive numbers pass 
     through unchanged and kills negative numbers (clamps to 0.0).

2. Sigmoid:
   - When to use: Usually placed at the final OUTPUT layer for binary classification.
   - Why: It mathematically "squashes" any number (no matter how giant or negative) 
     into a clean percentage/probability strictly between 0.0 and 1.0.
"""
import math

def relu_activation(x):
    """Rectified Linear Unit (ReLU) clamps negative numbers to 0."""
    return max(0.0, x)

def sigmoid_activation(x):
    """Sigmoid function squashes any number into a probability between 0.0 and 1.0."""
    return 1 / (1 + math.exp(-x))

class SimpleNeuron:
    def __init__(self, weights, bias, activation_name="relu"):
        self.weights = weights
        self.bias = bias
        self.activation_name = activation_name
        
    def forward(self, inputs):
        # 1. Dot Product
        dot_product = sum(i * w for i, w in zip(inputs, self.weights))
        
        # 2. Add Bias
        z = dot_product + self.bias
        
        # 3. Activation
        if self.activation_name == "relu":
            return relu_activation(z)
        elif self.activation_name == "sigmoid":
            return sigmoid_activation(z)
        else:
            return z

if __name__ == "__main__":
    # --- The Data ---
    # We pass in two features (e.g. House Size, Num Bedrooms)
    data_input = [2.0, 1.5]
    
    # Target value (e.g., 1.0 means "Yes, we want to buy it")
    target_output = 1.0
    
    # --- The Network (Chaining 2 Neurons) ---
    # Neuron 1 (Hidden Layer)
    # It takes 2 inputs (our two features), so it MUST have 2 weights.
    hidden_neuron = SimpleNeuron(weights=[0.5, -0.6], bias=0.1, activation_name="relu")
    
    # Neuron 2 (Output Layer)
    # It takes 1 input (the output from the hidden_neuron), so it MUST have 1 weight!
    output_neuron = SimpleNeuron(weights=[1.2], bias=-0.5, activation_name="sigmoid")
    
    print("--- Network Parameters ---")
    print(f"Hidden Neuron: weights={hidden_neuron.weights}, bias={hidden_neuron.bias}")
    print(f"Output Neuron: weights={output_neuron.weights}, bias={output_neuron.bias}")
    print("--------------------------\n")
    
    # --- The Forward Pass ---
    print(f"Initial Input Data: {data_input}")
    
    # Step 1: Pass data through the first neuron
    hidden_output = hidden_neuron.forward(data_input)
    print(f"Hidden Neuron Output (ReLU): {hidden_output:.4f}")
    
    # Step 2: Pass that output directly into the second neuron
    # (We wrap it in a list [hidden_output] because our forward() function expects a list of inputs)
    final_prediction = output_neuron.forward([hidden_output])
    print(f"Final Prediction (Sigmoid): {final_prediction:.4f}")
    
    # --- Error Calculation ---
    error = (target_output - final_prediction) ** 2
    
    print("-" * 30)
    print(f"Target: {target_output}")
    print(f"Cost/Error (MSE): {error:.4f}")
