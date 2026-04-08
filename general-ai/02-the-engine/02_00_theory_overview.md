# 02-the-engine: Deep Learning & Transformers

If a single linear regression function wrapped in a sigmoid is a "Neuron", what happens when you chain them together? You get Deep Learning.

### 1. Neural Networks as Pipelines
A Neural Network is essentially just a giant, sequential software pipeline. 
- You pass numbers (inputs) into the first layer of functions.
- The functions multiply them by weights, add biases, and "clamp" or squash the output (using activation functions like Sigmoid or ReLU).
- The clamped output is passed sequentially to the *next* layer as its input.
- Ultimately, out comes a final prediction.

**The Golden Rule of Activation Functions:**
* **ReLU (Rectified Linear Unit):** Almost exclusively used in **Hidden Layers**. It is computationally extremely fast because it simply lets positive math pass through unchanged and clamps any negative numbers to `0.0`. This also helps prevent math errors (vanishing gradients) when chaining deep layers together.
* **Sigmoid:** Usually placed strictly at the **Final Output Layer** for binary classification tasks. Because it mathematically "squashes" any number (no matter how giant or negative) into a clean percentage/probability between `0.0` and `1.0`.

Because all the layers are just mathematical functions plugged into each other, the entire network is fully differentiable—meaning we can use Calculus on it.

### 2. Backpropagation
In Part 1, we used "Gradient Descent" to figure out who to blame (which weight to adjust) for a bad prediction on a single function.
But in a Deep pipeline of 50 chained layers, how do you know *which specific function* in the middle caused the bad output? 

**Backpropagation** is the process of walking backwards through the pipeline. Using the Chain Rule of Calculus, it starts at the final error, and meticulously multiplies its way backward, asking every single weight "how much of this error is your fault?".

#### The Core Formulas (The Math of "Blame")
To calculate the gradient (how much to adjust the weights), the network relies on derivatives (rate of change) at every step:

1. **Error Derivative (MSE):** How far off was the ultimate target?
   `d_error = 2 * (prediction - target)`
2. **Sigmoid Derivative:** How sensitive is the output "gate"? (Mathematically elegant because it only requires its own output to calculate its derivative).
   `d_sigmoid = output * (1.0 - output)`
3. **ReLU Derivative:** The hidden gate sensitivity. (Binary: On or Off).
   `d_relu = 1.0 if x > 0 else 0.0`

By continuously multiplying these backward along the chain (The Chain Rule), we calculate the exact **Delta ($\Delta$)** (total accumulated blame) for any specific neuron. We then use that Delta to actually adjust the weight using Gradient Descent:
`new_weight = old_weight - (learning_rate * Delta * input_value)`

### 3. Tokenization & Embeddings
Before we can run Neural Networks on text, we must convert words into numbers. 
* **Tokenization:** This is essentially a giant `Enum` mapping. Every common word or chunk of a word gets assigned to a hardcoded integer (e.g. `Bank = 5024`, `The = 23`). 
* The problem: These are just arbitrary index numbers. `5024` has no mathematical relationship to the word "Money".
* **Embeddings:** We feed the integer into a giant lookup list that spits out an array of floats (e.g. `[0.45, -0.12, 0.88...]`). This array mathematically represents the "meaning" of the word!

### 4. The Transformer (Self-Attention)
Before 2017, AIs read text sequentially (like a `while` loop). The **Transformer** changed this using "Self-Attention"—which acts like a fully parallel, context-aware "Fuzzy Dictionary Lookup".

When looking at the word `Bank`, the engine creates:
1. **Query (Q):** What I am looking for? (e.g., "I am 'Bank', I need financial context or river context")
2. **Key (K):** What do I have? (Other words shout: "I am 'Money'", "I am 'River'")
3. **Value (V):** The actual underlying content/meaning of the word.

The Engine calculates a Dot Product between the "Bank" Query and all the other Keys in the sentence. If "Bank" dot-products with "Money" and scores extremely high, it blends the "Money" Value into its own mathematical meaning. Therefore, "Bank" becomes a dynamically weighted concept shaped by the words surrounding it!
