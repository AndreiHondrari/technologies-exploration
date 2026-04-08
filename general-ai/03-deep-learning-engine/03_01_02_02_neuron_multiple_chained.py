"""
Practice: Chain three single neurons together (Hidden -> Output).
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
    
    # --- The Network (2 Hidden -> 1 Output) ---
    # Hidden Layer: 2 Neurons
    # They both take 2 inputs (our two incoming features), so they MUST have 2 weights each.
    hidden_neuron_1 = SimpleNeuron(weights=[0.5, -0.6], bias=0.1, activation_name="relu")
    hidden_neuron_2 = SimpleNeuron(weights=[0.1,  0.8], bias=-0.2, activation_name="relu")
    
    # Output Layer: 1 Final Neuron
    # It takes 2 inputs (the outputs from the two hidden neurons), so it MUST have 2 weights!
    output_neuron = SimpleNeuron(weights=[1.2, -0.5], bias=0.3, activation_name="sigmoid")
    
    print("--- Network Parameters ---")
    print(f"Hidden Neuron 1: weights={hidden_neuron_1.weights}, bias={hidden_neuron_1.bias}")
    print(f"Hidden Neuron 2: weights={hidden_neuron_2.weights}, bias={hidden_neuron_2.bias}")
    print(f"Output Neuron: weights={output_neuron.weights}, bias={output_neuron.bias}")
    print("--------------------------\n")
    
    # --- The Forward Pass ---
    print(f"Initial Input Data: {data_input}")
    
    # Step 1: Pass initial data through BOTH neurons in the first layer
    h1_output = hidden_neuron_1.forward(data_input)
    h2_output = hidden_neuron_2.forward(data_input)
    print(f"Hidden Neuron 1 Output (ReLU): {h1_output:.4f}")
    print(f"Hidden Neuron 2 Output (ReLU): {h2_output:.4f}")
    
    # Step 2: Gather those outputs and pass them as an array into the final neuron
    layer_1_results = [h1_output, h2_output]
    final_prediction = output_neuron.forward(layer_1_results)
    
    print(f"Output Neuron receives from Hidden Layer: {layer_1_results}")
    print(f"Final Prediction (Sigmoid): {final_prediction:.4f}")
    
    # --- Error Calculation ---
    error = (target_output - final_prediction) ** 2
    
    print("-" * 30)
    print(f"Target: {target_output}")
    print(f"Cost/Error (MSE): {error:.4f}")
