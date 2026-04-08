"""
Practice: Chain two single neurons together sequentially (Hidden -> Output) and implement Backpropagation.
"""
import math

def relu_activation(x):
    """Rectified Linear Unit (ReLU) clamps negative numbers to 0."""
    return max(0.0, x)

def relu_derivative(x):
    """Derivative of ReLU: 1 if x > 0 else 0."""
    return 1.0 if x > 0 else 0.0

def sigmoid_activation(x):
    """Sigmoid function squashes any number into a probability between 0.0 and 1.0."""
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(output):
    """Derivative of Sigmoid using its output value: output * (1 - output)."""
    return output * (1.0 - output)

class TrainableNeuron:
    def __init__(self, weights, bias, activation_name="relu"):
        self.weights = weights
        self.bias = bias
        self.activation_name = activation_name
        self.last_input = None
        self.last_z = None
        self.last_output = None
        
    def forward(self, inputs):
        self.last_input = inputs
        # 1. Dot Product
        dot_product = sum(i * w for i, w in zip(inputs, self.weights))
        
        # 2. Add Bias
        self.last_z = dot_product + self.bias
        
        # 3. Activation
        if self.activation_name == "relu":
            self.last_output = relu_activation(self.last_z)
        elif self.activation_name == "sigmoid":
            self.last_output = sigmoid_activation(self.last_z)
        else:
            self.last_output = self.last_z
            
        return self.last_output

if __name__ == "__main__":
    # --- The Data ---
    data_input = [2.0, 1.5]
    target_output = 1.0
    learning_rate = 0.1
    
    # --- The Network ---
    hidden_neuron = TrainableNeuron(weights=[0.5, -0.6], bias=0.1, activation_name="relu")
    output_neuron = TrainableNeuron(weights=[1.2], bias=-0.5, activation_name="sigmoid")
    
    print("=== INITIAL STATE ===")
    print(f"Inputs: {data_input}")
    print(f"Target: {target_output}")
    print(f"Hidden Neuron: weights={hidden_neuron.weights}, bias={hidden_neuron.bias}")
    print(f"Output Neuron: weights={output_neuron.weights}, bias={output_neuron.bias}\n")

    print("--- Initial Forward Pass ---")
    h_out = hidden_neuron.forward(data_input)
    prediction = output_neuron.forward([h_out])
    error = (target_output - prediction) ** 2
    
    print(f"Hidden Output: {h_out:.4f}")
    print(f"Final Prediction: {prediction:.4f}")
    print(f"Current Error: {error:.4f}\n")

    # --- Backpropagation (The "Blame" Game) ---
    print("--- Backpropagation Steps ---")
    
    # 1. Output Neuron Blame
    d_error_pred = 2 * (prediction - target_output)
    d_pred_zout = sigmoid_derivative(prediction)
    delta_output = d_error_pred * d_pred_zout
    
    # Gradients for Output Neuron
    grad_w_out = delta_output * h_out
    grad_b_out = delta_output
    
    print(f"Output Delta: {delta_output:.4f} (Blame for being off by {prediction - target_output:.4f})")

    # 2. Hidden Neuron Blame (Chain Rule)
    d_error_hout = delta_output * output_neuron.weights[0]
    d_hout_zhid = relu_derivative(hidden_neuron.last_z)
    delta_hidden = d_error_hout * d_hout_zhid
    
    # Gradients for Hidden Neuron
    grad_w_hid = [delta_hidden * i for i in data_input]
    grad_b_hid = delta_hidden
    
    print(f"Hidden Delta: {delta_hidden:.4f}")
    print(f"Hidden Weights Gradients: {grad_w_hid}\n")

    # --- Update Weights (Gradient Descent) ---
    print("--- Updating Weights (Learning) ---")
    output_neuron.weights[0] -= learning_rate * grad_w_out
    output_neuron.bias -= learning_rate * grad_b_out
    
    hidden_neuron.weights = [w - learning_rate * g for w, g in zip(hidden_neuron.weights, grad_w_hid)]
    hidden_neuron.bias -= learning_rate * grad_b_hid
    
    print(f"New Hidden: weights={hidden_neuron.weights}, bias={hidden_neuron.bias:.4f}")
    print(f"New Output: weights={output_neuron.weights}, bias={output_neuron.bias:.4f}\n")

    # --- New Forward Pass ---
    print("--- Post-Training Forward Pass ---")
    h_out_new = hidden_neuron.forward(data_input)
    prediction_new = output_neuron.forward([h_out_new])
    error_new = (target_output - prediction_new) ** 2
    
    print(f"New Prediction: {prediction_new:.4f}, New Error: {error_new:.4f}")
    print(f"Improvement: {error - error_new:.4f}")
