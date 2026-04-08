"""
Practice: Full Training Loop (Gradient Descent) on a chained network.
We run the Forward Pass & Backpropagation multiple times until the network "learns" the right weights.
"""
import math

def relu_activation(x):
    """Rectified Linear Unit (ReLU)"""
    return max(0.0, x)

def relu_derivative(x):
    """Derivative of ReLU"""
    return 1.0 if x > 0 else 0.0

def sigmoid_activation(x):
    """Sigmoid function"""
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(output):
    """Derivative of Sigmoid using its output value"""
    return output * (1.0 - output)

class TrainableNeuron:
    def __init__(self, weights, bias, activation_name="relu"):
        self.weights = weights.copy()
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
    
    # We increase the learning rate slightly so it learns faster in fewer loops
    learning_rate = 0.5 
    epochs = 200 # The number of times we will repeat the cycle
    
    # --- The Network ---
    hidden_neuron = TrainableNeuron(weights=[0.5, -0.6], bias=0.1, activation_name="relu")
    output_neuron = TrainableNeuron(weights=[1.2], bias=-0.5, activation_name="sigmoid")
    
    print("=== INITIAL STATE ===")
    h_out_init = hidden_neuron.forward(data_input)
    prediction_init = output_neuron.forward([h_out_init])
    print(f"Prediction: {prediction_init:.4f}")
    print(f"Error: {(target_output - prediction_init) ** 2:.4f}\n")
    
    print("=== BEGIN TRAINING LOOP ===")
    
    # This loop is Gradient Descent!
    for epoch in range(epochs):
        # 1. Forward Pass
        h_out = hidden_neuron.forward(data_input)
        prediction = output_neuron.forward([h_out])
        
        # 2. Calculate Error (MSE)
        error = (target_output - prediction) ** 2
        
        if (epoch + 1) % 20 == 0 or epoch == 0:
            print(f"Epoch {(epoch + 1):>3} | Prediction: {prediction:.4f} | Error: {error:.4f}")
            
        # 3. Backpropagation (Calculate Blame)
        
        # --- Output Neuron Blame ---
        d_error_pred = 2 * (prediction - target_output)
        d_pred_zout = sigmoid_derivative(prediction)
        delta_output = d_error_pred * d_pred_zout
        
        grad_w_out = delta_output * h_out
        grad_b_out = delta_output
        
        # --- Hidden Neuron Blame (Chain Rule) ---
        d_error_hout = delta_output * output_neuron.weights[0]
        d_hout_zhid = relu_derivative(hidden_neuron.last_z)
        delta_hidden = d_error_hout * d_hout_zhid
        
        grad_w_hid = [delta_hidden * i for i in data_input]
        grad_b_hid = delta_hidden
        
        # 4. Update Weights (Take a step down the gradient)
        output_neuron.weights[0] -= learning_rate * grad_w_out
        output_neuron.bias -= learning_rate * grad_b_out
        
        hidden_neuron.weights = [w - learning_rate * g for w, g in zip(hidden_neuron.weights, grad_w_hid)]
        hidden_neuron.bias -= learning_rate * grad_b_hid
        
            
    print("\n=== FINAL STATE AFTER TRAINING ===")
    print(f"Hidden Neuron: weights={[round(w, 4) for w in hidden_neuron.weights]}, bias={hidden_neuron.bias:.4f}")
    print(f"Output Neuron: weights={[round(w, 4) for w in output_neuron.weights]}, bias={output_neuron.bias:.4f}")
    
    final_h_out = hidden_neuron.forward(data_input)
    final_prediction = output_neuron.forward([final_h_out])
    
    print(f"\nFinal Prediction: {final_prediction:.4f}")
    print(f"Final Error     : {(target_output - final_prediction) ** 2:.6f}")
    
    if final_prediction > 0.95:
        print("\nSUCCESS! Through repetition, the network learned to adjust its weights perfectly.")
