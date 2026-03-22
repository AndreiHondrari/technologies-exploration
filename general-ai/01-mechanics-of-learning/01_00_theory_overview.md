# 01-mechanics-of-learning: The Mechanics of Learning

## Core Concept: "Code is your Math"

When we approach Artificial Intelligence from a software engineering perspective, the underlying math simply becomes data structures and loops.

### 1. The Dot Product

In math notation, you might see $A \cdot B$. 
In code, this is simply taking two arrays of the same size, multiplying their items index-by-index, and adding up all the results.

```python
# $A \cdot B$
A = [1, 2, 3]
B = [4, 5, 6]

result = sum(a * b for a, b in zip(A, B)) # 1*4 + 2*5 + 3*6 = 32
```
This is the core intuition of AI: It doesn't "think"—it measures distances and relationships between arrays of numbers.

### 2. Cost Functions (MSE)

A Model is just a function (e.g. `predict(x)`). A **Cost Function** is a function that calculates exactly how *wrong* the model is.
**Mean Squared Error (MSE)** is a common cost function: it loops over all predictions, subtracts the actual correct answers, squares the errors (to make them positive and penalize large errors heavily), and takes the average.

### 3. Gradient Descent (The "Blame Game")

If you have a prediction that involves some weights (like `m` and `b` in $y = mx + b$), you want to figure out which direction to tweak `m` and `b` to make the Cost Function go down. 

Instead of guessing randomly, you use **Derivatives** ($\partial$). A derivative is just a tiny tweak. 
"If I increase the weight `m` by `0.001`, does my error go up or down? If it goes down, keep going that way."

The loop of repeatedly measuring the error, tweaking the weights based on the derivative, and repeating is called **Gradient Descent**.
