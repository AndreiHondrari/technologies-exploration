# 02-classical-machine-learning

Before we chained neurons together to fold non-linear shapes (Deep Learning), the field of Artificial Intelligence was dominated by **Classical Machine Learning**.

The grand secret of Classical ML is that **learning patterns does not mathematically require "neurons" or "backpropagation".** You can build incredibly accurate, blazingly fast predictive models using nothing but basic geometry and logic algorithms. 

---

## 1. K-Means Clustering [Unsupervised]
**Goal:** Discover hidden groups in unlabeled data.
**Example:** *Segmenting 4 Data Points into 2 Groups.*

### The Math in Action:
*   **Raw Data:** `points = [[1, 1], [2, 2], [8, 8], [9, 9]]`
*   **Starting Centroids:** `c1 = [0, 0], c2 = [10, 10]`
*   **Step 1:** `[1, 1]` is closer to `c1`. `[9, 9]` is closer to `c2`.
*   **Step 2 (The Average):** 
    `c1` moves to the average of `[1, 1]` and `[2, 2]` → `[1.5, 1.5]`
    `c2` moves to the average of `[8, 8]` and `[9, 9]` → `[8.5, 8.5]`
*   **Result:** The "Groups" are now mathematically defined as the areas around `1.5` and `8.5`.

### Gotchas & Engineer's Notes
1. **How do you pick K?** In our script, we manually hard-coded $K=3$. But in the real world, you don't know how many clusters exist! Engineers use a visual trick called the **Elbow Method**. They run K-Means with $K=1, 2, 3...$ and chart the "total error". They pick the $K$ value exactly where the graph violently bends (like a human elbow), which represents the point of diminishing mathematical returns.
2. **The "Local Minima" Trap:** You likely noticed that if the initial random centroids spawn right next to each other, they steal each other's points and stabilize beautifully on completely wrong data! Because K-Means is logically blind, it relies heavily on its initial drop coordinates. To solve this, real-world systems either run the algorithm 10 separate times and average the results, or use an upgrade called **K-Means++** which physically forces the initial random centroids to spawn as far away from each other as geometrically possible.

---

## 2. K-Nearest Neighbors (KNN) [Supervised]
**Goal:** Classify an unknown item by looking at its neighbors.
**Example:** *Predicting if [3, 3] is a Cat or a Dog.*

### The Math in Action:
*   **Database:** `[([1, 1], "Cat"), ([2, 2], "Cat"), ([9, 9], "Dog")]`
*   **New Point:** `[3, 3]`
*   **Calculation (Euclidean Distance):**
    1. Distance to first Cat: $\sqrt{(3-1)^2 + (3-1)^2} = 2.82$
    2. Distance to second Cat: $\sqrt{(3-2)^2 + (3-2)^2} = 1.41$
    3. Distance to Dog: $\sqrt{(3-9)^2 + (3-9)^2} = 8.48$
*   **Classification:** If $K=2$, we pick the two closest neighbors (both Cats). **Result: It's a Cat.**

### Gotchas & Engineer's Notes
1. **How do you pick K?** You should strictly pick an **odd number** for $K$ (like 3, 5, or 7) to mathematically prevent a 50/50 hung jury during the democratic vote! Furthermore, a larger $K$ forces the algorithm to poll the broader general "neighborhood" rather than just the specific closest neighbor, which safely prevents the AI from being tricked by random chaotic outliers.

---

## 3. Decision Trees [Supervised]
**Goal:** Build an autonomous flowchart of `if/else` statements.
**Example:** *Determining if we "Play Tennis" based on Weather.*

### The Math in Action:
*   **Dataset:** `[["Sunny", "No"], ["Sunny", "No"], ["Overcast", "Yes"], ["Overcast", "Yes"]]`
*   **Initial Chaos (Gini):** `0.5` (perfect 50/50 split of Yes/No).
*   **Testing Question:** `"Is Weather == Overcast?"`
    *   **True Branch:** `[["Yes"], ["Yes"]]` → Gini: `0.0` (Perfectly Pure!)
    *   **False Branch:** `[["No"], ["No"]]` → Gini: `0.0` (Perfectly Pure!)
*   **Information Gain:** `0.5 - (0.5 * 0 + 0.5 * 0) = 0.5` (A massive improvement).
*   **Winner:** The AI locks in `If Weather == Overcast` as its first logic gate.

---

## 4. Random Forests [Ensemble Supervised]
**Goal:** Use a "Forest" of trees to prevent errors.
**Example:** *Predicting Fraud from 3 Voting Trees.*

### The Math in Action:
*   **Scenario:** A suspicious credit card transaction.
*   **Tree 1 (Trained on subset 1):** Predicts "Fraud".
*   **Tree 2 (Trained on subset 2):** Predicts "Fraud".
*   **Tree 3 (Trained on subset 3):** Predicts "Legitimate" (Overfit on an outlier).
*   **Final Consensus:** `["Fraud", "Fraud", "Legit"]`.
*   **Result:** The forest outputs "Fraud" (2 vs 1). The error of Tree 3 is cancelled out by the majority.

---

## 5. A* Pathfinding [GOFAI / Search]
**Goal:** Find the optimal path through a grid.
**Example:** *Moving from [0,0] to [2,2] through a wall.*

### The Math in Action:
*   **Current Tile:** `[0, 1]` 
*   **Cost (G):** We have walked `1` step so far.
*   **Guess (H):** Manhattan distance to `[2, 2]` is $|2-0| + |2-1| = 3$.
*   **Total Score (F):** `1 + 3 = 4`.
*   **Decision:** If a different tile `[1, 0]` has an F-score of `3.5`, the AI will **abandon** its current path and follow that one instead!

---

### Why "Data Transformation" Matters
Everything we build is just a pipe that turns numbers into decisions!
*   KNN transforms **Coordinates → Sorted Distances → Labels.**
*   Decision Trees transform **Categories → Impurity Scores → Logic Gates.**
*   K-Means transforms **Scattered Noise → Mathematical Means → Clusters.**

Classical AI is not "thinking"—it is **calculating equilibrium.**
