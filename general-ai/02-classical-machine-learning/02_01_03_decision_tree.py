"""
02_01_03_decision_tree.py

Supervised Machine Learning: The Decision Tree

If KNN categorizes data by Geometry, the Decision Tree groups data by pure Logic.
It mathematically autonomously writes a massive `if/else` logic flow chart!

How does it code itself? By measuring "Gini Impurity" (how messy the answers are). 
It mathematically tests EVERY possible `if` statement, and permanently locks in 
whichever question perfectly sorts the data into the cleanest "True/False" buckets. 
It repeats this recursively until the buckets are 100% pure!
"""
import collections

# ==========================================
# 1. GENERATE A LABELED DATASET
# ==========================================
# Format: [Weather, Temp, Wind, "Play_Tennis?"]
dataset = [
    ["Sunny", "Hot", "Weak", "No"],
    ["Sunny", "Hot", "Strong", "No"],
    ["Overcast", "Hot", "Weak", "Yes"],
    ["Rain", "Mild", "Weak", "Yes"],
    ["Rain", "Cool", "Weak", "Yes"],
    ["Rain", "Cool", "Strong", "No"],
    ["Overcast", "Cool", "Strong", "Yes"],
    ["Sunny", "Mild", "Weak", "No"],
]
feature_names = ["Weather", "Temp", "Wind"]

# ==========================================
# 2. HELPER MATH (Gini Impurity)
# ==========================================
def gini_impurity(data):
    # Perfect purity = 0.0. Maximum messy mix = 0.5
    if not data:
        return 0.0
    counter = collections.Counter([row[-1] for row in data])
    impurity = 1.0
    for label in counter:
        probability = counter[label] / len(data)
        impurity -= probability ** 2
    return impurity

def split_dataset(data, column_idx, value):
    true_split = [row for row in data if row[column_idx] == value]
    false_split = [row for row in data if row[column_idx] != value]
    return true_split, false_split

# ==========================================
# 3. THE SPLITTING ENGINE
# ==========================================
def find_best_split(data):
    best_gini = 1.0 # Worst case scenario
    best_question = None
    best_true_split = None
    best_false_split = None
    
    num_features = len(data[0]) - 1 # Exclude the final answer label
    
    # Try literally every unique value in every column as a potential `if` statement!
    for col in range(num_features):
        unique_values = set([row[col] for row in data])
        for val in unique_values:
            # Physically separate the data assuming this was the if statement
            true_split, false_split = split_dataset(data, col, val)
            if not true_split or not false_split:
                continue # Skip if it doesn't divide anything
                
            # Calculate the weighted average Gini of the newly separated branches
            p_true = len(true_split) / len(data)
            p_false = len(false_split) / len(data)
            weighted_gini = (p_true * gini_impurity(true_split)) + (p_false * gini_impurity(false_split))
            
            # If this resulted in a cleaner bucket than we've found so far, lock it in!
            if weighted_gini < best_gini:
                best_gini = weighted_gini
                best_question = (col, val)
                best_true_split = true_split
                best_false_split = false_split
                
    return best_question, best_true_split, best_false_split

# ==========================================
# 4. RECURSIVE TREE GENERATION
# ==========================================
class Leaf:
    def __init__(self, data):
        self.predictions = dict(collections.Counter([row[-1] for row in data]))

class DecisionNode:
    def __init__(self, question, true_branch, false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch

def build_tree(data):
    # 1. Ask the engine to find the mathematically perfect split
    question, true_split, false_split = find_best_split(data)
    
    # 2. If it can't find a way to split the data any cleaner, we've reached a pure Leaf!
    if question is None:
        return Leaf(data)
        
    # 3. Recursively build the next branches deeper and deeper
    true_branch = build_tree(true_split)
    false_branch = build_tree(false_split)
    
    return DecisionNode(question, true_branch, false_branch)

def print_tree(node, spacing=""):
    if isinstance(node, Leaf):
        print(spacing + f"Predict Category: {node.predictions}")
        return
        
    col, val = node.question
    print(spacing + f"Is {feature_names[col]} == '{val}'?")
    
    print(spacing + "--> True:")
    print_tree(node.true_branch, spacing + "  ")
    
    print(spacing + "--> False:")
    print_tree(node.false_branch, spacing + "  ")

if __name__ == "__main__":
    print("=== AUTONOMOUS DECISION TREE BUILDER ===")
    print("Calculating system entropies and dynamically assembling if/else flowchart blocks...\n")
    
    # We pass the raw data, and the code writes the flowchart for us!
    my_tree = build_tree(dataset)
    print_tree(my_tree)
