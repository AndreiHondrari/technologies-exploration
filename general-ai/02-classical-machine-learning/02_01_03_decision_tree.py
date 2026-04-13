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
def find_best_split(data, depth):
    best_gain = 0
    best_question = None
    best_true_split = None
    best_false_split = None
    current_uncertainty = gini_impurity(data)
    
    indent = "  " * depth
    num_features = len(data[0]) - 1 
    
    print(f"\n{indent}📂 Evaluation for {len(data)} rows:")
    for row in data: print(f"{indent}   {row}")
    print(f"{indent}   (Current chaos/Gini: {current_uncertainty:.3f})")

    # Try literally every unique value in every column as a potential `if` statement!
    for col in range(num_features):
        unique_values = set([row[col] for row in data])
        for val in unique_values:
            # Physically separate the data assuming this was the if statement
            true_rows, false_rows = split_dataset(data, col, val)
            
            # Skip if it doesn't divide anything
            if not true_rows or not false_rows:
                continue 
                
            # --- THE CALCULATION STEP ---
            g_true = gini_impurity(true_rows)
            g_false = gini_impurity(false_rows)
            
            # Weighted average of the new impurity
            p = len(true_rows) / len(data)
            weighted_avg_gini = (p * g_true) + ((1 - p) * g_false)
            
            # Gain is simply: How much did chaos drop?
            gain = current_uncertainty - weighted_avg_gini
            
            print(f"{indent}   ❓ Test: {feature_names[col]} == '{val}'?")
            print(f"{indent}      -> True: {len(true_rows)} rows (Gini: {g_true:.3f})")
            print(f"{indent}      -> False: {len(false_rows)} rows (Gini: {g_false:.3f})")
            print(f"{indent}      => Improvement (Gain): {gain:.3f}")

            if gain > best_gain:
                best_gain = gain
                best_question = (col, val)
                best_true_split = true_rows
                best_false_split = false_rows
                
    if best_question:
        col, val = best_question
        print(f"\n{indent}🏆 WINNING SPLIT: '{feature_names[col]} == {val}'")
        print(f"{indent}   This reduced chaos by {best_gain:.3f}")
    
    return best_question, best_true_split, best_false_split, best_gain

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

def build_tree(data, depth=0):
    indent = "  " * depth
    # 1. Ask the engine to find the mathematically perfect split
    question, true_split, false_split, gain = find_best_split(data, depth)
    
    # 2. If no gain can be made, we've reached a pure Leaf!
    if gain <= 0 or question is None:
        labels = dict(collections.Counter([row[-1] for row in data]))
        print(f"{indent}🍃 PURE LOGIC REACHED: {labels}")
        return Leaf(data)
        
    # 3. Recursively build the next branches deeper and deeper
    print(f"\n{indent}🌿 RECURSION: Moving into TRUE branch ('{feature_names[question[0]]} == {question[1]}')")
    true_branch = build_tree(true_split, depth + 1)
    
    print(f"\n{indent}🌿 RECURSION: Moving into FALSE branch ('{feature_names[question[0]]} != {question[1]}')")
    false_branch = build_tree(false_split, depth + 1)
    
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

def classify(row, node):
    """
    Traverses the tree recursively to categorize a new unseen row of data.
    """
    # 1. Base Case: If we are at a Leaf, return the answer!
    if isinstance(node, Leaf):
        return node.predictions

    # 2. Decision Logic: Ask the question stored at this node
    col, val = node.question
    if row[col] == val:
        # It's a match! Follow the 'True' path deeper.
        return classify(row, node.true_branch)
    else:
        # Not a match. Follow the 'False' path deeper.
        return classify(row, node.false_branch)

if __name__ == "__main__":
    print("=== AUTONOMOUS DECISION TREE BUILDER ===")
    print("Calculating system entropies and dynamically assembling if/else flowchart blocks...\n")
    
    # Pass the raw training data to build the "Brain"
    my_tree = build_tree(dataset)
    
    print("\n=== FINAL VISUALIZED TREE ===")
    print_tree(my_tree)

    print("\n=== MAKING A PREDICTION ===")
    # Let's test it on a brand new day: Sunny, Cool, and Strong wind.
    new_day = ["Sunny", "Cool", "Strong"]
    prediction = classify(new_day, my_tree)
    
    print(f"Scenario: {new_day}")
    print(f"AI Decision: {prediction}")
