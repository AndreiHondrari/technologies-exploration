# AI & Machine Learning Algorithms Taxonomy

This document categorizes the core mathematical engines, structures, and filters that power Artificial Intelligence. 

## 1. Traditional Supervised Learning (Classical ML)
Algorithms that learn from labeled data (e.g., "Here is a picture of a cat, it is labeled 'Cat'").

| Algorithm | Category | Primary Purpose | How It Works (The "Code" Intuition) |
| :--- | :--- | :--- | :--- |
| **Linear Regression** | Regression | Predicting continuous numbers (Price, Temp) | Draws a straight mathematical line ($y=mx+b$) through data points to minimize total error distances. |
| **Logistic Regression** | Classification | Binary Yes/No (Pass/Fail, Spam) | Uses a Sigmoid function to squash a Linear Regression output into a 0% to 100% boundary. |
| **Decision Trees** | Both | Interpretability & Logic Rules | Automatically writes a giant nested `if/else` statement by splitting data based on the most informative features. |
| **Random Forest** | Both | Robustness & Accuracy | Creates 1,000 different Decision Trees and makes them "vote" on the final answer to prevent overfitting. |
| **K-Nearest Neighbors (KNN)** | Classification | Grouping by similarity | Plots data on a grid. To classify a new point, it looks at its $K$ closest neighbors using geometric distance math (Pythagorean Theorem) and copies them. |
| **Support Vector Machines (SVM)** | Classification | Distinct separation boundaries | Draws the widest, fattest possible barrier (hyperplane) perfectly between two different clusters of data. |
| **Naive Bayes** | Classification | Text & Spam filtering | Uses pure probability math (Bayes' Theorem) counting how often certain words appear in "Spam" vs "Not Spam". Fast but assumes words are independent. |

## 2. Unsupervised Learning
Algorithms that find patterns in raw, unlabeled data without knowing what they are looking for.

| Algorithm | Category | Primary Purpose | How It Works (The "Code" Intuition) |
| :--- | :--- | :--- | :--- |
| **K-Means Clustering** | Clustering | Finding unknown groups (Market segments) | Drops $K$ random center-points onto a graph. Points gravitate to the closest center. The centers repeatedly jump to the middle of their group until stable. |
| **Principal Component Analysis (PCA)** | Dimensionality Reduction | Compression | Squashes a 100-dimension array into a 3-dimension array by finding the mathematically most "important" angles, throwing away useless noise. |

## 3. Deep Learning Architectures
Algorithms constructed from vast pipelines of individual Neurons (Logistic/Linear math).

| Architecture | Category | Primary Purpose | How It Works (The "Code" Intuition) |
| :--- | :--- | :--- | :--- |
| **Multilayer Perceptron (MLP)** | Vanilla NN | Basic Deep Learning | Just standard Neurons chained in sequential hidden layers. The output of one layer is the `[inputs]` for the next. |
| **Convolutional Neural Networks (CNN)** | Computer Vision | Image recognition | Passes a tiny $3\times3$ mathematical magnifying glass (filter) over a giant 2D grid of pixels, multiplying them to detect edges, then shapes, then objects. |
| **Recurrent Neural Networks (RNN)** | Sequence / Time | Forecasting, old NLP | A `while` loop that takes the output of the current step, saves it in a `hidden_state` variable, and feeds it backward into the *next* step of the loop. |
| **Transformers** | Advanced Sequence | LLMs (ChatGPT) | Uses an attention dictionary (Query, Key, Value mappings) to process all words entirely in parallel instead of a sequential loop, dynamically linking context. |

## 4. Optimization Engines (The "Gradient" Solvers)
The algorithms responsible for updating the weights (`m` and `b`) during training.

| Optimizer | Primary Purpose | How It Works (The "Code" Intuition) |
| :--- | :--- | :--- |
| **Gradient Descent (GD)** | Base Optimization | Calculates the exact derivative (slope) of the error and takes one tiny, uniform step totally downhill. |
| **Stochastic Gradient Descent (SGD)** | Speed | Instead of checking the error of *all* 10,000 data points before taking a step, it picks 1 random point, calculates error, and steps instantly. Fast but chaotic. |
| **Adam (Adaptive Moment Estimation)** | Modern Default | It gives Gradient Descent "momentum". If it has been rolling downhill in the same direction for 50 steps, it speeds up. If the hill gets bumpy, it taps the brakes dynamically. |

## 5. Activation "Filters" (Non-Linear Functions)
Mathematical gates placed at the end of a Neuron to squash or clamp the output before passing it entirely to the next network layer.

| Filter | Math Output Range | Primary Purpose | Why It Matters |
| :--- | :--- | :--- | :--- |
| **Sigmoid** | `0.0` to `1.0` | Probabilities | Converts giant continuous numbers strictly into percentages. Used in output layers for binary classification. |
| **ReLU (Rectified)** | `0.0` to infinity | Deep Network Speed | `max(0, x)`. If the number is negative, it dies (`0.0`). If positive, it passes through perfectly. Incredibly fast for GPUs to calculate. |
| **Tanh** | `-1.0` to `1.0` | Zero-centered features | Same curve as Sigmoid, but centers data around `0` instead of `0.5`. Helps gradients flow more smoothly in hidden layers. |
| **Softmax** | `0.0` to `1.0` (Sums to 1) | Multi-category Choice | If a model outputs raw scores like `[Dog: 50, Cat: 20]`, Softmax converts them so they add to 100% (e.g. `[Dog: 71%, Cat: 29%]`). |
