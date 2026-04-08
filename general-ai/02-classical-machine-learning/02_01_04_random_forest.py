"""
02_01_04_random_forest.py

Supervised Machine Learning: Random Forests (Ensemble Learning)

A single Decision Tree is great, but it is notoriously prone to "overfitting" 
(memorizing the exact training data directly, while performing poorly on brand new data). 
To fix this, we build a "Random Forest".

The algorithm randomly samples chunks of the data and dynamically builds an entire forest 
of slightly mutated trees. When asked to classify a new scenario, it drops the data 
through EVERY single tree and holds a massive democratic vote across the forest.
"""
import random
import collections
import importlib

# We can flawlessly reuse the pure-logic engine we built in the previous script!
dt = importlib.import_module("02_01_03_decision_tree")

def bootstrap_dataset(dataset, sample_size):
    # Randomly samples rows from the dataset (with replacement)
    # This purposefully ensures every Tree we build is trained on slightly different data!
    return [random.choice(dataset) for _ in range(sample_size)]

def predict_single_tree(node, row):
    # Traverses a single decision tree recursively to make a prediction
    if isinstance(node, dt.Leaf):
        # Return the highest counted prediction in this Leaf's bucket
        return max(node.predictions.items(), key=lambda k: k[1])[0]
        
    col, val = node.question
    
    if row[col] == val:
        return predict_single_tree(node.true_branch, row)
    else:
        return predict_single_tree(node.false_branch, row)

def random_forest_predict(forest, row):
    # Drop the data through all trees and collect their independent votes!
    votes = []
    for tree in forest:
        prediction = predict_single_tree(tree, row)
        votes.append(prediction)
        
    print(f"  -> Raw Forest Votes: {votes}")
    
    # Hold a democratic assembly vote!
    vote_counter = collections.Counter(votes)
    winner = vote_counter.most_common(1)[0][0]
    return winner

if __name__ == "__main__":
    print("=== AUTONOMOUS RANDOM FOREST BUILDER ===")
    
    # Use the same exact Tennis dataset
    full_dataset = dt.dataset
    
    NUM_TREES = 7
    my_forest = []
    
    print(f"Processing Bootstrapped samples. Growing {NUM_TREES} unique Decision Trees...\n")
    for i in range(NUM_TREES):
        # 1. Grab a random mutated sample of the dataset
        subset = bootstrap_dataset(full_dataset, len(full_dataset))
        
        # 2. Build a tree using that subset
        tree = dt.build_tree(subset)
        my_forest.append(tree)
        print(f"Tree {i+1} successfully grown!")
        
    print("\n=== ENSEMBLE PREDICTION ===")
    
    # Let's test a couple of brand new, unseen weather scenarios
    test_1 = ["Sunny", "Cool", "Weak"]
    print(f"Scenario 1: {test_1}\nPredicting...")
    result_1 = random_forest_predict(my_forest, test_1)
    print(f"✅ Final Consensus: {result_1}\n")
    
    test_2 = ["Rain", "Hot", "Strong"]
    print(f"Scenario 2: {test_2}\nPredicting...")
    result_2 = random_forest_predict(my_forest, test_2)
    print(f"✅ Final Consensus: {result_2}\n")
