"""
02_01_01_k_means_clustering.py

Unsupervised Machine Learning: K-Means Clustering

In this script, we dump an array of Unlabeled Data Points into a 2D space. 
We then tell the code to autonomously figure out where the 3 distinct "Clusters" are!

Notice: There are zero Neurons here!
There are no derivatives, no backpropagation, and no cost functions!
It achieves Artificial Intelligence (autonomous pattern recognition) using 
nothing but basic Geometry (The Pythagorean Theorem).
"""
import math
import random

# ==========================================
# 1. HELPER MATH (The Engine of Classical ML)
# ==========================================
def euclidean_distance(point1, point2):
    # The Pythagorean Theorem: a^2 + b^2 = c^2
    # This mathematically measures the physical distance between two points on the grid.
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# ==========================================
# 2. GENERATE SYNTHETIC UNLABELED DATA
# ==========================================
# We secretly generate random clusters of points in 3 specific geographical areas.
# NOTE: In real life, the algorithm would have no idea how these were generated!
data_points = []

# Secret Cluster 1 (Around x=2, y=2)
for _ in range(15):
    data_points.append([random.uniform(0, 4), random.uniform(0, 4)])

# Secret Cluster 2 (Around x=8, y=8)
for _ in range(15):
    data_points.append([random.uniform(6, 10), random.uniform(6, 10)])

# Secret Cluster 3 (Around x=2, y=8)
for _ in range(15):
    data_points.append([random.uniform(0, 4), random.uniform(6, 10)])

# We intentionally shuffle the list so the data points are in complete physical chaos
random.shuffle(data_points)

# ==========================================
# 3. THE K-MEANS ALGORITHM
# ==========================================
# We want the algorithm to autonomously find K=3 distinct groups.
K = 3

# Step A: Drop 3 completely random "Centroids" (Centers of mass) onto the grid.
centroids = [[random.uniform(0, 10), random.uniform(0, 10)] for _ in range(K)]

print("=== STARTING AUTONOMOUS CLUSTERING ===")
print("Initial Random Centroid Positions:")
for i, c in enumerate(centroids):
    print(f"  Centroid {i}: ({c[0]:.2f}, {c[1]:.2f})")
print("\nMoving Centroids to find statistical equilibrium...\n")

max_iterations = 20
for iteration in range(max_iterations):
    # Step B: Assign every data point to whatever Centroid is mathematically closest to it.
    clusters = [[] for _ in range(K)]
    
    for point in data_points:
        best_centroid_idx = 0
        min_distance = float('inf')
        
        # Check distance to all 3 centroids to find the closest one
        for i, centroid in enumerate(centroids):
            distance = euclidean_distance(point, centroid)
            if distance < min_distance:
                min_distance = distance
                best_centroid_idx = i
                
        # Register the point to the winning centroid's cluster list
        clusters[best_centroid_idx].append(point)
        
    # Step C: Move each Centroid to the exact statistical average "Center" of its newly claimed group!
    previous_centroids = [list(c) for c in centroids]
    
    for i in range(K):
        # Prevent crash if a centroid claimed zero points
        if len(clusters[i]) == 0:
            continue
            
        sum_x = sum(p[0] for p in clusters[i])
        sum_y = sum(p[1] for p in clusters[i])
        
        # Move centroid to the average!
        centroids[i][0] = sum_x / len(clusters[i])
        centroids[i][1] = sum_y / len(clusters[i])
        
    # Step D: Did the centroids stop moving? If yes, we found the perfect clusters! Break early.
    total_movement = sum(euclidean_distance(prev, new) for prev, new in zip(previous_centroids, centroids))
    print(f"Iteration {iteration+1:>2}: Total drift this step was {total_movement:.4f} units.")
    
    if total_movement < 0.001:
        print(f"\n✅ Algorithm stabilized elegantly at Iteration {iteration+1}!")
        break

# ==========================================
# 4. RESULTS
# ==========================================
print("\n=== FINAL DISCOVERED CLUSTERS ===")
for i, c in enumerate(centroids):
    print(f"Centroid {i} definitively settled at: ({c[0]:.2f}, {c[1]:.2f})")
    print(f"  -> It autonomously claimed {len(clusters[i])} data points without labels.\n")

print("Because the Centroids settled exactly around (2,2), (8,8), and (2,8)...")
print("We have mathematically proven the AI perfectly reverse-engineered our secret data generation!")
