"""
02_01_01b_k_means_elbow.py

Unsupervised Machine Learning: K-Means Clustering
EXPERIMENT 2: The Elbow Method (Finding K blind)

In the real world, we don't know how many groups exist!
Here we run K-Means independently for K=1 through K=7, 
measuring the 'Total Error' (Inertia) to find the mathematical Elbow!
"""
import math
import random
import sys

try:
    from utils.visualisation.kmeans import visualize_elbow_multipanel_animation
    CAN_VISUALIZE = True
except ImportError:
    CAN_VISUALIZE = False

# ==========================================
# 1. HELPER MATH (The Engine of Classical ML)
# ==========================================
def euclidean_distance(point1, point2):
    # The Pythagorean Theorem: a^2 + b^2 = c^2
    # This mathematically measures the physical distance between two points on the grid.
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def calculate_inertia(clusters, centroids):
    # Calculates how 'tight' the clusters are (Sum of squared distances from centroids)
    total_error = 0
    for i, cluster in enumerate(clusters):
        if i >= len(centroids): continue
        c = centroids[i]
        for p in cluster:
            total_error += (p[0] - c[0])**2 + (p[1] - c[1])**2
    return total_error

# ==========================================
# 2. CORE ALGORITHM LOGIC
# ==========================================
def run_kmeans(data_points, K, max_iterations=20):
    # 1. INITIALIZATION: Spawn the random Centroids
    centroids = [[random.uniform(0, 10), random.uniform(0, 10)] for _ in range(K)]
    
    history = []
    history.append(( [list(c) for c in centroids], [] ))
    clusters = []
    
    # 2. THE MAIN LOOP: Finding Statistical Equilibrium
    for iteration in range(max_iterations):
        clusters = [[] for _ in range(K)]
        
        # Step A: Associate each point with its nearest centroid using Pythagorean math
        for point in data_points:
            best_centroid_idx = 0
            min_distance = float('inf')
            for i, centroid in enumerate(centroids):
                distance = euclidean_distance(point, centroid)
                if distance < min_distance:
                    min_distance = distance
                    best_centroid_idx = i
            clusters[best_centroid_idx].append(point)
            
        previous_centroids = [list(c) for c in centroids]
        
        # Step B: Physically relocate the centroids to the new "Center of Mass"
        for i in range(K):
            # Dead centroid guard (If a centroid claims no points, leave it)
            if len(clusters[i]) == 0: continue 
            sum_x = sum(p[0] for p in clusters[i])
            sum_y = sum(p[1] for p in clusters[i])
            centroids[i][0] = sum_x / len(clusters[i])
            centroids[i][1] = sum_y / len(clusters[i])
            
        history.append(( [list(c) for c in centroids], [[list(p) for p in c] for c in clusters] ))
            
        # Step C: Check for Convergence. If they stopped moving, we found the groups!
        total_movement = sum(euclidean_distance(prev, new) for prev, new in zip(previous_centroids, centroids))
        if total_movement < 0.001: break
            
    total_inertia = calculate_inertia(clusters, centroids)
    return history, total_inertia


if __name__ == "__main__":
    raw_data = []
    for _ in range(15): raw_data.append([random.uniform(0, 4), random.uniform(0, 4)]) # Cluster 1
    for _ in range(15): raw_data.append([random.uniform(6, 10), random.uniform(6, 10)]) # Cluster 2
    for _ in range(15): raw_data.append([random.uniform(0, 4), random.uniform(6, 10)]) # Cluster 3
    random.shuffle(raw_data)

    print("=== EXPERIMENT 2: THE ELBOW METHOD ===")
    
    if not CAN_VISUALIZE:
        print("\n[!] Please run 'pip install matplotlib' for the visual experiments to work!")
        sys.exit(1)

    k_experiments = range(1, 8)
    all_errors = []
    all_histories = []
    
    for k_test in k_experiments:
        history, inertia = run_kmeans(raw_data, K=k_test)
        all_histories.append(history)
        all_errors.append(inertia)
        print(f"   Tested K={k_test} -> Total Error Distance: {inertia:.1f}")
        
    visualize_elbow_multipanel_animation(k_experiments, all_histories, all_errors, raw_data)
