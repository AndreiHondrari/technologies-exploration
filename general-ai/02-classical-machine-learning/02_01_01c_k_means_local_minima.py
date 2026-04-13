"""
02_01_01c_k_means_local_minima.py

Unsupervised Machine Learning: K-Means Clustering
EXPERIMENT 3: The "Local Minima" Gotcha

We intentionally spawn all 3 centroids in the exact same bottom corner.
Watch how they get stuck (Local Minima) and fail to cluster correctly!
"""
import math
import random
import sys

try:
    from utils.visualisation.kmeans import visualize_kmeans_animation
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
def run_kmeans(data_points, K, max_iterations=20, manual_centroids=None):
    # 1. INITIALIZATION: Spawn the forced (bad) Centroids
    centroids = [list(c) for c in manual_centroids]
        
    # To fulfill the animation request, we create a chronological timeline of its state!
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
            
        # Take snapshot for the UI Animator!
        history.append(( [list(c) for c in centroids], [[list(p) for p in c] for c in clusters] ))
        
        # Step C: Check for Convergence. If they stopped moving, we found the groups!
        total_movement = sum(euclidean_distance(prev, new) for prev, new in zip(previous_centroids, centroids))
        if total_movement < 0.001: break
            
    total_inertia = calculate_inertia(clusters, centroids)
    return history, centroids, clusters, total_inertia


if __name__ == "__main__":
    raw_data = []
    # To guarantee the Local Minimum trap locks permanently, we generate perfectly 
    # symmetrical fixed lattice points instead of floating randomization, preventing drift!
    # Cluster 1 (Bottom Left)
    for x in [1, 2, 3]: 
        for y in [1, 2, 3]: raw_data.append([x, y]) 
    # Cluster 2 (Top Left)
    for x in [1, 2, 3]: 
        for y in [7, 8, 9]: raw_data.append([x, y]) 
    # Cluster 3 (Bottom Right)
    for x in [7, 8, 9]: 
        for y in [1, 2, 3]: raw_data.append([x, y])

    print("=== EXPERIMENT 3: LOCAL MINIMA FAILURE ===")
    
    if not CAN_VISUALIZE:
        print("\n[!] Please run 'pip install matplotlib' for the visual experiments to work!")
        sys.exit(1)

    print("Spawning centroids into an inescapable symmetrical trap...")
    bad_spawns = [[8.0, 1.9], [8.0, 2.1], [2.0, 5.0]]
    
    history_bad, _, _, _ = run_kmeans(raw_data, K=3, manual_centroids=bad_spawns)
    visualize_kmeans_animation(history_bad, raw_data, title="Experiment 3: Catastrophic Local Minima Trap")
