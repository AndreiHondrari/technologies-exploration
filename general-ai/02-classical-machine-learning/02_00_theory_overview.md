# 02-classical-machine-learning

Before we chained neurons together to fold non-linear shapes (Deep Learning), the field of Artificial Intelligence was dominated by **Classical Machine Learning**.

The grand secret of Classical ML is that **learning patterns does not mathematically require "neurons" or "backpropagation".** You can build incredibly accurate, blazingly fast predictive models using nothing but basic geometry and logic algorithms. 

In the modern world, Classical ML is still heavily used for structured tabular data (spreadsheets), fraud detection, and recommendation systems because it is computationally cheap and completely transparent (unlike the "black box" of Deep Learning).

### 1. Supervised vs. Unsupervised Learning

In Part 1, you learned **Supervised Learning**. We explicitly fed the network the `inputs` and the `targets`. The network learned to map the inputs to the correct pre-labeled answers. 

But what if you have 10,000 data points and have *no idea* what the labels are? This is called **Unsupervised Learning**. The AI's job is to organically find structure in the chaos without you telling it what to look for.

### 2. Geometry & Distance (KNN and K-Means)

Instead of using gradients and Calculus to find patterns, many Classical ML algorithms use pure **Geometry** (Euclidean Distance / The Pythagorean Theorem).

* **K-Nearest Neighbors (KNN):** [Supervised]
  If I drop a new point on a graph and I don't know what it is, I simply look at the $K$ closest dots to it. If 4 of the 5 closest dots are "Cats", my new dot is probably a "Cat". Making a prediction involves zero training; it just measures raw distances!

* **K-Means Clustering:** [Unsupervised]
  I have a giant cloud of unlabeled data. I want the AI to find 3 distinct groups. 
  1. I randomly drop 3 "Centers" (Centroids) onto the graph.
  2. Every data point aligns with whichever Center is closest to it.
  3. Then, I move the Center directly to the average middle of its newly claimed group.
  4. Repeat until the Centers stop moving! The AI has autonomously discovered the natural clusters.

### 3. Entropy & Logic (Decision Trees)

What if the data isn't easily mapped on a geometric grid? What if it's mixed with categories like `Weather = Sunny`? 

* **Decision Trees:** [Supervised]
  The algorithm mathematically explores the data looking for a rule that splits the data perfectly in half. For example, *"Is Age > 30?"*. If that cleanly separates the people who bought a car from people who didn't, it locks that split in as an `if/else` block. 
  It repeats this recursively, autonomously writing a massive flow chart of `if/else` statements until it perfectly categorizes the entire dataset.

  *Why is this popular?* Because you can literal print the tree and read the `if` statements. You know *exactly* why the AI made a decision!

### The Practical Mission

In this chapter, we are going to write a **K-Means Clustering** engine from scratch. It will visualize scattered, unlabelled data points, autonomously find the geographical centers of mass, and group the data correctly without ever using a gradient, a derivative, or a neuron!
