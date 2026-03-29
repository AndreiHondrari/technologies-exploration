"""
02_01_neuron_pipeline.py
Practice: Build a simple forward-pass neuron pipeline and calculate errors.
"""
import math

def relu_activation(x):
    """Rectified Linear Unit (ReLU) clamps negative numbers to 0."""
    return max(0.0, x)

class SimpleNeuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
        
    def forward(self, inputs):
        # 1. Dot Product (multiply inputs by weights and sum them up)
        dot_product = sum(i * w for i, w in zip(inputs, self.weights))
        
        # 2. Add Bias
        z = dot_product + self.bias
        
        # 3. Activation (squash or clamp the result so it can pass to the next layer)
        output = relu_activation(z)
        
        return output

class MockPipeline:
    def __init__(self):
        # Hidden Layer: 2 Neurons
        self.neuron1 = SimpleNeuron(weights=[0.5, -0.6], bias=0.1)
        self.neuron2 = SimpleNeuron(weights=[0.1, 0.8], bias=-0.2)
        
        # Output Layer: 1 Neuron
        self.output_neuron = SimpleNeuron(weights=[1.5, -1.0], bias=0.5)
        
    def forward_pass(self, inputs):
        print(f"Input Data: {inputs}")
        
        # Pass data through hidden layer
        h1 = self.neuron1.forward(inputs)
        h2 = self.neuron2.forward(inputs)
        print(f"Hidden Layer Activations: [{h1:.4f}, {h2:.4f}]")
        
        # Pass hidden layer results to output layer
        final_prediction = self.output_neuron.forward([h1, h2])
        print(f"Final Prediction: {final_prediction:.4f}")
        
        return final_prediction

if __name__ == "__main__":
    network = MockPipeline()
    
    # We pass in two features (e.g. House Size, Num Bedrooms)
    data_input = [2.0, 1.5]
    target_output = 3.0
    
    prediction = network.forward_pass(data_input)
    
    # Calculate Error (MSE)
    error = (target_output - prediction) ** 2
    print("-" * 30)
    print(f"Target: {target_output}")
    print(f"Cost/Error (MSE): {error:.4f}")
    
    print("\n[!] In a real neural network, 'Backpropagation' would now theoretically walk backwards")
    print("from that Cost to figure out exactly how much to adjust the weights of the")
    print("Output Neuron, and then pass the blame further back to the Hidden Neurons.")
