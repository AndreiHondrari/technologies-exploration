"""
02_01_06_neuron_net_nonlinear.py

The Historic XOR Problem (1969 "AI Winter")

A single perceptron can easily learn logic gates like OR and AND because you
can draw a single straight line to separate the True/False answers on a graph.

However, the XOR (Exclusive OR) gate is famously NON-LINEAR:
[0,0] -> 0
[1,0] -> 1
[0,1] -> 1
[1,1] -> 0

You mathematically cannot draw a single straight line to separate these! A single neuron fails.
To solve it, we chain 2 hidden neurons (using ReLU to fold the math) and map 
them to 1 output neuron. This structure is what officially creates a "Deep" Neural Network.
"""
import math
import random

def relu_activation(x):
    return max(0.0, x)

def relu_derivative(x):
    return 1.0 if x > 0 else 0.0

def sigmoid_activation(x):
    x = max(min(x, 100), -100)
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(output):
    return output * (1.0 - output)

class TrainableNeuron:
    def __init__(self, num_inputs, activation_name="relu"):
        self.weights = [random.uniform(-1.0, 1.0) for _ in range(num_inputs)]
        self.bias = random.uniform(-1.0, 1.0)
        self.activation_name = activation_name
        self.last_input = None
        self.last_z = None
        self.last_output = None
        
    def forward(self, inputs):
        self.last_input = inputs
        dot_product = sum(i * w for i, w in zip(inputs, self.weights))
        self.last_z = dot_product + self.bias
        
        if self.activation_name == "relu":
            self.last_output = relu_activation(self.last_z)
        elif self.activation_name == "sigmoid":
            self.last_output = sigmoid_activation(self.last_z)
        else:
            self.last_output = self.last_z
            
        return self.last_output


if __name__ == "__main__":
    # 1. THE DATASET: The pure XOR Gate (Only 4 samples total!)
    training_data = [
        ([0.0, 0.0], 0.0),
        ([1.0, 0.0], 1.0),
        ([0.0, 1.0], 1.0),
        ([1.0, 1.0], 0.0),
    ]

    # 2. INITIALIZE THE DEEP NEURAL NETWORK (2 Hidden -> 1 Output)
    # The 2 Hidden Neurons draw the 2 lines we need to box in the XOR results
    h1 = TrainableNeuron(num_inputs=2, activation_name="relu")
    h2 = TrainableNeuron(num_inputs=2, activation_name="relu")
    
    out_neuron = TrainableNeuron(num_inputs=2, activation_name="sigmoid")
    
    learning_rate = 0.1
    epochs = 4000  # Non-linear folding takes much longer to settle!
    
    print("=== BEGIN STOCHASTIC GRADIENT DESCENT (XOR Problem) ===")
    for epoch in range(epochs):
        total_error = 0.0
        random.shuffle(training_data)
        
        for inputs, target in training_data:
            # --- FORWARD PASS ---
            h1_out = h1.forward(inputs)
            h2_out = h2.forward(inputs)
            
            prediction = out_neuron.forward([h1_out, h2_out])
            
            error = (target - prediction) ** 2
            total_error += error
            
            # --- BACKPROPAGATION ---
            # Output Neuron Blame
            d_err_pred = 2 * (prediction - target)
            delta_out = d_err_pred * sigmoid_derivative(prediction)
            
            grad_w_out = [delta_out * h1_out, delta_out * h2_out]
            grad_b_out = delta_out
            
            # Hidden Neurons Blame (Applying ReLU derivative hinge!)
            delta_h1 = (delta_out * out_neuron.weights[0]) * relu_derivative(h1.last_z)
            delta_h2 = (delta_out * out_neuron.weights[1]) * relu_derivative(h2.last_z)
            
            grad_w_h1 = [delta_h1 * inputs[0], delta_h1 * inputs[1]]
            grad_b_h1 = delta_h1
            
            grad_w_h2 = [delta_h2 * inputs[0], delta_h2 * inputs[1]]
            grad_b_h2 = delta_h2
            
            # --- UPDATE WEIGHTS ---
            out_neuron.weights[0] -= learning_rate * grad_w_out[0]
            out_neuron.weights[1] -= learning_rate * grad_w_out[1]
            out_neuron.bias -= learning_rate * grad_b_out
            
            h1.weights[0] -= learning_rate * grad_w_h1[0]
            h1.weights[1] -= learning_rate * grad_w_h1[1]
            h1.bias -= learning_rate * grad_b_h1
            
            h2.weights[0] -= learning_rate * grad_w_h2[0]
            h2.weights[1] -= learning_rate * grad_w_h2[1]
            h2.bias -= learning_rate * grad_b_h2
            
        avg_error = total_error / len(training_data)
        if (epoch + 1) % 500 == 0:
            print(f"Epoch {epoch + 1:>4} | Avg Error: {avg_error:.4f}")
            
    # 3. TEST THE NETWORK
    print("\n=== FINAL PREDICTIONS ===")
    # Notice we test it sequentially (un-shuffled) so it's easy to read!
    test_data = [([0.0, 0.0], 0.0), ([1.0, 0.0], 1.0), ([0.0, 1.0], 1.0), ([1.0, 1.0], 0.0)]
    for inputs, target in test_data:
        h1_out = h1.forward(inputs)
        h2_out = h2.forward(inputs)
        prediction = out_neuron.forward([h1_out, h2_out])
        
        print(f"Input: {inputs} | Target: {target} | Prediction: {prediction:.4f}")
