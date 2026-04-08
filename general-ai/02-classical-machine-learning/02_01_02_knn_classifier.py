"""
02_01_02_knn_classifier.py

Supervised Machine Learning: K-Nearest Neighbors (KNN)

In K-Means, the algorithm had NO IDEA what the groups were. 
Here in KNN, we DO provide the answers (This is "Supervised Learning").

The magical part about KNN is that it actually does zero "learning". It doesn't 
train an equation or run gradients. It just plots the known data into space. 

When asked to classify a new unknown item, it simply measures the physical distance 
to all the known dots, and isolates the `K` closest neighbors. 
It then holds a democratic vote: If 4 out of my 5 closest neighbors are "Cats", 
I must realistically be a "Cat"!
"""
import math
from collections import Counter

# ==========================================
# 1. HELPER MATH (The core engine of Classical ML)
# ==========================================
def euclidean_distance(point1, point2):
    # This mathematically measures the physical distance between two points on the grid.
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# ==========================================
# 2. GENERATE A LABELED DATASET (Supervised)
# ==========================================
# Format: ([x_coord, y_coord], "Label")
labeled_data = [
    # Cats generally hang out geographically around the bottom-left
    ([2.0, 2.0], "Cat"),
    ([1.5, 2.5], "Cat"),
    ([2.5, 1.5], "Cat"),
    ([1.0, 1.0], "Cat"),
    
    # Dogs generally hang out geographically around the top-right
    ([8.0, 8.0], "Dog"),
    ([7.5, 8.5], "Dog"),
    ([8.5, 7.5], "Dog"),
    ([9.0, 9.0], "Dog"),
]

# ==========================================
# 3. KNN ALGORITHM IMPLEMENTATION
# ==========================================
def predict_knn(k_neighbors, unknown_point, dataset):
    distances = []
    
    # Step A: Measure the exact distance from the unknown point to EVERY point in our database
    for known_point, label in dataset:
        dist = euclidean_distance(unknown_point, known_point)
        # We store the physical distance, along with the answer label of that dot
        distances.append((dist, label))
        
    # Step B: Sort the list so the shortest distances (closest neighbors) bubble to the top!
    distances.sort(key=lambda x: x[0])
    
    # Step C: Isolate only the top `K` closest neighbors
    closest_neighbors_labels = [label for dist, label in distances[:k_neighbors]]
    
    # Step D: Hold a democratic voting process! Which label appeared the most?
    vote_counter = Counter(closest_neighbors_labels)
    winning_label, votes = vote_counter.most_common(1)[0]
    
    print(f"\n--- KNN Prediction for Coordinates {unknown_point} (K={k_neighbors}) ---")
    print(f"Holding a democratic vote amongst the {k_neighbors} closest neighbors...")
    
    for dist, label in distances[:k_neighbors]:
        print(f"  -> Found a {label} roughly {dist:.2f} units of distance away.")
        
    print(f"Result: '{winning_label}' wins with {votes}/{k_neighbors} votes! Prediction finalized.")
    return winning_label

if __name__ == "__main__":
    print("=== SUPERVISED KNN CLASSIFIER ===")
    print(f"We have {len(labeled_data)} labeled items mapped into our geometric database.")
    
    # Test 1: A point dropped very close to the bottom left (Should vote Cat)
    test_point_1 = [3.0, 2.5]
    predict_knn(k_neighbors=3, unknown_point=test_point_1, dataset=labeled_data)
    
    # Test 2: A point dropped very close to the top right (Should vote Dog)
    test_point_2 = [7.0, 6.5]
    predict_knn(k_neighbors=3, unknown_point=test_point_2, dataset=labeled_data)
    
    # Test 3: The Danger of Geometrics! A point dropped directly in the middle no-mans-land.
    # By expanding K to 5, we grab a wider radius of opinions to break ties safely.
    test_point_3 = [4.5, 5.0]
    predict_knn(k_neighbors=5, unknown_point=test_point_3, dataset=labeled_data)
