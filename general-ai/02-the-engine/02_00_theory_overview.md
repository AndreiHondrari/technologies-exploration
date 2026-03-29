# 02-the-engine: Deep Learning & Transformers

If a single linear regression function wrapped in a sigmoid is a "Neuron", what happens when you chain them together? You get Deep Learning.

### 1. Neural Networks as Pipelines
A Neural Network is essentially just a giant, sequential software pipeline. 
- You pass numbers (inputs) into the first layer of functions.
- The functions multiply them by weights, add biases, and "clamp" or squash the output (using activation functions like Sigmoid or ReLU).
- The clamped output is passed sequentially to the *next* layer as its input.
- Ultimately, out comes a final prediction.

Because all the layers are just mathematical functions plugged into each other, the entire network is fully differentiable—meaning we can use Calculus on it.

### 2. Backpropagation
In Part 1, we used "Gradient Descent" to figure out who to blame (which weight to adjust) for a bad prediction on a single function.
But in a Deep pipeline of 50 chained layers, how do you know *which specific function* in the middle caused the bad output? 

**Backpropagation** is the process of walking backwards through the pipeline. Using the Chain Rule of Calculus, it starts at the final error, and meticulously multiplies its way backward, asking every single weight "how much of this error is your fault?" so it can apply Gradient Descent to all of them at once.

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
