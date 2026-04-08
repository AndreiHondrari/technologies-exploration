"""
02_01_05_neuron_net.py

The Linear "OR" Gate Logic Problem

A single perceptron is essentially a mathematical line-drawer. Because the "OR" logic
gate is a "Linear Problem", we can easily teach a SINGLE neuron to perfectly separate 
the True values from the False values using just one straight boundary line!

The OR Rule: Output 1 if AT LEAST ONE input is 1.
[0,0] -> 0
[1,0] -> 1
[0,1] -> 1
[1,1] -> 1
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
    def __init__(self, num_inputs, activation_name="sigmoid"):
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
    # 1. THE DATASET: The pure OR Gate (4 samples total!)
    training_data = [
        ([0.0, 0.0], 0.0),
        ([1.0, 0.0], 1.0),
        ([0.0, 1.0], 1.0),
        ([1.0, 1.0], 1.0),
    ]

    # 2. INITIALIZE THE NEURAL NETWORK (1 Single Neuron!)
    # Because the "OR" gate is simple and linear, ONE single neuron can find
    # a clean 50% boundary line between the 0s and 1s! No hidden layers needed.
    single_neuron = TrainableNeuron(num_inputs=2, activation_name="sigmoid")
    
    learning_rate = 0.1
    epochs = 1000
    
    print("=== BEGIN STOCHASTIC GRADIENT DESCENT (OR Logic Gate) ===")
    for epoch in range(epochs):
        total_error = 0.0
        random.shuffle(training_data)
        
        for inputs, target in training_data:
            # --- FORWARD PASS ---
            prediction = single_neuron.forward(inputs)
            
            error = (target - prediction) ** 2
            total_error += error
            
            # --- BACKPROPAGATION ---
            # Output Neuron Blame
            d_err_pred = 2 * (prediction - target)
            delta = d_err_pred * sigmoid_derivative(prediction)
            
            grad_w0 = delta * inputs[0]
            grad_w1 = delta * inputs[1]
            grad_b  = delta
            
            # --- UPDATE WEIGHTS ---
            single_neuron.weights[0] -= learning_rate * grad_w0
            single_neuron.weights[1] -= learning_rate * grad_w1
            single_neuron.bias -= learning_rate * grad_b
            
        avg_error = total_error / len(training_data)
        if (epoch + 1) % 200 == 0:
            print(f"Epoch {epoch + 1:>4} | Avg Error: {avg_error:.4f}")
            
    # 3. TEST THE NETWORK
    print("\n=== FINAL PREDICTIONS ===")
    test_data = [([0.0, 0.0], 0.0), ([1.0, 0.0], 1.0), ([0.0, 1.0], 1.0), ([1.0, 1.0], 1.0)]
    for inputs, target in test_data:
        prediction = single_neuron.forward(inputs)
        print(f"Input: {inputs} | Target: {target} | Prediction: {prediction:.4f}")
