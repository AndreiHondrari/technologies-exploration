"""
02_01_05_neuron_net.py
Practice: Training a Neural Network to memorize a 6x6 Image.
This demonstrates coordinate-based machine learning. Instead of memorizing
a static array, the network learns a mathematical function that predicts
the color (0.0 or 1.0) based solely on the (x, y) coordinates of the pixel!
"""
import math
import random

def relu_activation(x):
    return max(0.0, x)

def relu_derivative(x):
    return 1.0 if x > 0 else 0.0

def sigmoid_activation(x):
    # Clamping x to prevent overflow errors in math.exp
    x = max(min(x, 100), -100)
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(output):
    return output * (1.0 - output)

class TrainableNeuron:
    def __init__(self, num_inputs, activation_name="relu"):
        # We start with random small weights so the network can break symmetry
        self.weights = [random.uniform(-0.5, 0.5) for _ in range(num_inputs)]
        self.bias = random.uniform(-0.5, 0.5)
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
    # 1. GENERATE THE TRAINING DATASET (6x6 Image)
    # x goes from 0 to 5 (Left to Right), y goes from 0 to 5 (Top to Bottom)
    # Target: x < 3 is Black (0.0), x >= 3 is White (1.0)
    training_data = []
    
    print("=== TARGET IMAGE (6x6) ===")
    num_matrix_target = []
    
    for y in range(6):
        row_num = ""
        for x in range(6):
            # The rule: Target is a real value continuous gradient from left (0.0) to right (1.0).
            target = float(x) / 5.0
            
            # Save the training pair: ( [x, y], target )
            training_data.append(([float(x), float(y)], target))
            row_num += f"{target:5.2f} "
            
        num_matrix_target.append(row_num)
        
    for row in num_matrix_target:
        print(row)
        
    print("==========================\n")

    # 2. INITIALIZE THE NEURAL NETWORK (2 Hidden -> 1 Output)
    # Hidden Layer: 2 Neurons (each takes 2 inputs: the x and y coordinates)
    h1 = TrainableNeuron(num_inputs=2, activation_name="relu")
    h2 = TrainableNeuron(num_inputs=2, activation_name="relu")
    
    # Output Layer: 1 Neuron (takes 2 inputs from the hidden layer h1 & h2)
    out = TrainableNeuron(num_inputs=2, activation_name="sigmoid")
    
    # Hyperparameters
    learning_rate = 0.1
    epochs = 500
    
    print("=== BEGIN STOCHASTIC GRADIENT DESCENT ===")
    for epoch in range(epochs):
        total_error = 0.0
        
        # Shuffle data each epoch so it learns the general pattern, not the sequence
        random.shuffle(training_data)
        
        # Train on every pixel one by one
        for inputs, target in training_data:
            # --- FORWARD PASS ---
            h1_out = h1.forward(inputs)
            h2_out = h2.forward(inputs)
            
            prediction = out.forward([h1_out, h2_out])
            
            error = (target - prediction) ** 2
            total_error += error
            
            # --- BACKPROPAGATION ---
            # Output Neuron Blame
            d_err_pred = 2 * (prediction - target)
            delta_out = d_err_pred * sigmoid_derivative(prediction)
            
            grad_w_out = [delta_out * h1_out, delta_out * h2_out]
            grad_b_out = delta_out
            
            # Hidden Neurons Blame
            delta_h1 = (delta_out * out.weights[0]) * relu_derivative(h1.last_z)
            delta_h2 = (delta_out * out.weights[1]) * relu_derivative(h2.last_z)
            
            grad_w_h1 = [delta_h1 * inputs[0], delta_h1 * inputs[1]]
            grad_b_h1 = delta_h1
            
            grad_w_h2 = [delta_h2 * inputs[0], delta_h2 * inputs[1]]
            grad_b_h2 = delta_h2
            
            # --- UPDATE WEIGHTS ---
            out.weights[0] -= learning_rate * grad_w_out[0]
            out.weights[1] -= learning_rate * grad_w_out[1]
            out.bias -= learning_rate * grad_b_out
            
            h1.weights[0] -= learning_rate * grad_w_h1[0]
            h1.weights[1] -= learning_rate * grad_w_h1[1]
            h1.bias -= learning_rate * grad_b_h1
            
            h2.weights[0] -= learning_rate * grad_w_h2[0]
            h2.weights[1] -= learning_rate * grad_w_h2[1]
            h2.bias -= learning_rate * grad_b_h2
            
        avg_error = total_error / len(training_data)
        if (epoch + 1) % 100 == 0:
            print(f"Epoch {epoch + 1:>4} | Avg Pixel Error: {avg_error:.4f}")
            
    # 3. TEST THE NETWORK
    print("\n=== NETWORK'S PREDICTED IMAGE ===")
    print("If successful, the net recreates the real values directly via its learned math!")
    
    number_matrix = []
    
    for y in range(6):
        number_row = ""
        for x in range(6):
            # Forward pass test parameters through the now fully trained network
            h1_out = h1.forward([float(x), float(y)])
            h2_out = h2.forward([float(x), float(y)])
            prediction = out.forward([h1_out, h2_out])
            
            # Format number nicely aligned to 2 decimal places
            number_row += f"{prediction:5.2f} "
            
        number_matrix.append(number_row)
        
    for row in number_matrix:
        print(row)
