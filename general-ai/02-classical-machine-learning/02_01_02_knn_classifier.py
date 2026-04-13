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
# 0. VISUALIZATION ENGINE (Optional UI logic)
# ==========================================
def visualize_knn_animation(dataset, test_results):
    try:
        import matplotlib.pyplot as plt
        from matplotlib.widgets import Button
        from matplotlib.animation import FuncAnimation
    except ImportError:
        print("\n[!] Matplotlib is not installed. To see the graphical plot, run:")
        print("    pip install matplotlib")
        return
        
    print("\nLaunching Interactive Matplotlib Animation...")
    plt.style.use('dark_background')
    
    fig, ax = plt.subplots(figsize=(9, 9))
    fig.canvas.manager.set_window_title("KNN Classification Animator")
    plt.subplots_adjust(bottom=0.2)
    
    frames_data = []
    frames_data.append({"state": "init"}) # Frame 0: Show empty map with known data
    
    for i, (point, k_val, pred_label, distances) in enumerate(test_results):
        frames_data.append({"state": "dropping", "point": point, "k": k_val, "test_idx": i+1})
        frames_data.append({"state": "classifying", "point": point, "k": k_val, "pred_label": pred_label, "distances": distances, "test_idx": i+1})

    cat_coords = [d[0] for d in dataset if d[1] == "Cat"]
    dog_coords = [d[0] for d in dataset if d[1] == "Dog"]
    
    x_c, y_c = zip(*cat_coords) if cat_coords else ([], [])
    x_d, y_d = zip(*dog_coords) if dog_coords else ([], [])

    class AnimationController:
        def __init__(self):
            self.frame = 0
            self.is_playing = False # Start paused for manual step control!
            
        def draw_state(self):
            ax.clear()
            ax.set_title("KNN Classification (Voting geometrically without Neurons!)", fontsize=14, pad=15)
            ax.grid(True, linestyle='--', alpha=0.4)
            ax.set_xlim(0, 10)
            ax.set_ylim(0, 10)
            
            # 1. Paint background database
            ax.scatter(x_c, y_c, c='#4B4BFF', label='Database: Cats', alpha=0.5, s=150, marker='o')
            ax.scatter(x_d, y_d, c='#FF4B4B', label='Database: Dogs', alpha=0.5, s=150, marker='o')

            # 2. Re-render all completed tests
            for f in range(self.frame):
                if frames_data[f]["state"] == "classifying":
                    p = frames_data[f]["point"]
                    color = '#4B4BFF' if frames_data[f]["pred_label"] == "Cat" else '#FF4B4B'
                    ax.scatter(p[0], p[1], c=color, marker='*', s=450, edgecolor='white', linewidth=1.5)
                    ax.annotate(f"Predicted:\n{frames_data[f]['pred_label']}", (p[0], p[1]), textcoords="offset points", xytext=(0,20), ha='center', fontweight='bold')

            # 3. Render current frame focus
            frame_info = frames_data[self.frame]
            if frame_info["state"] == "dropping":
                p = frame_info["point"]
                ax.scatter(p[0], p[1], c='gray', marker='*', s=450, edgecolor='white', linewidth=1.5, label='Unknown Point Dropped')
                ax.annotate("Scanning Neighbors...", (p[0], p[1]), textcoords="offset points", xytext=(0,20), ha='center', color='yellow')
                
            elif frame_info["state"] == "classifying":
                p = frame_info["point"]
                k_val = frame_info["k"]
                pred_label = frame_info["pred_label"]
                distances = frame_info["distances"]
                color = '#4B4BFF' if pred_label == "Cat" else '#FF4B4B'
                
                # Draw snap lines natively
                for dist, label, known_pt in distances[:k_val]:
                    ax.plot([p[0], known_pt[0]], [p[1], known_pt[1]], color='white', linestyle=':', alpha=0.7)
                    
                ax.scatter(p[0], p[1], c=color, marker='*', s=450, edgecolor='white', linewidth=1.5, label=f'Voted {pred_label} (K={k_val})')
                ax.annotate(f"Predicted:\n{pred_label}", (p[0], p[1]), textcoords="offset points", xytext=(0,20), ha='center', fontweight='bold', color=color)

            ax.legend(loc='upper left')
            fig.canvas.draw_idle()
            
        def next_step(self, event):
            self.is_playing = False
            btn_play.label.set_text('Play')
            if self.frame < len(frames_data) - 1:
                self.frame += 1
                self.draw_state()
                
        def prev_step(self, event):
            self.is_playing = False
            btn_play.label.set_text('Play')
            if self.frame > 0:
                self.frame -= 1
                self.draw_state()
                
        def toggle_play(self, event):
            self.is_playing = not self.is_playing
            btn_play.label.set_text('Pause' if self.is_playing else 'Play')
            
        def timer_tick(self, f):
            if self.is_playing:
                if self.frame < len(frames_data) - 1:
                    self.frame += 1
                    self.draw_state()
                else:
                    self.is_playing = False
                    btn_play.label.set_text('Play')
                    
    controller = AnimationController()
    
    # Render UI Buttons
    ax_prev = plt.axes([0.3, 0.05, 0.1, 0.075])
    ax_play = plt.axes([0.45, 0.05, 0.1, 0.075])
    ax_next = plt.axes([0.6, 0.05, 0.1, 0.075])
    
    btn_prev = Button(ax_prev, 'Prev', color='#333333', hovercolor='#555555')
    btn_play = Button(ax_play, 'Play', color='#333333', hovercolor='#555555')
    btn_next = Button(ax_next, 'Next', color='#333333', hovercolor='#555555')
    
    btn_prev.on_clicked(controller.prev_step)
    btn_play.on_clicked(controller.toggle_play)
    btn_next.on_clicked(controller.next_step)
    
    controller.draw_state()
    anim = FuncAnimation(fig, controller.timer_tick, interval=1500, cache_frame_data=False)
    plt.show()

# ==========================================
# 1. HELPER MATH (The core engine of Classical ML)
# ==========================================
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# ==========================================
# 2. GENERATE A LABELED DATASET (Supervised)
# ==========================================
labeled_data = [
    ([2.0, 2.0], "Cat"), ([1.5, 2.5], "Cat"), ([2.5, 1.5], "Cat"), ([1.0, 1.0], "Cat"),
    ([8.0, 8.0], "Dog"), ([7.5, 8.5], "Dog"), ([8.5, 7.5], "Dog"), ([9.0, 9.0], "Dog"),
]

# ==========================================
# 3. KNN ALGORITHM IMPLEMENTATION
# ==========================================
def predict_knn(k_neighbors, unknown_point, dataset):
    distances = []
    for known_point, label in dataset:
        dist = euclidean_distance(unknown_point, known_point)
        distances.append((dist, label, known_point))
        
    distances.sort(key=lambda x: x[0])
    closest_neighbors_labels = [label for dist, label, pt in distances[:k_neighbors]]
    
    vote_counter = Counter(closest_neighbors_labels)
    winning_label, votes = vote_counter.most_common(1)[0]
    
    print(f"\n--- KNN Prediction for Coordinates {unknown_point} (K={k_neighbors}) ---")
    for dist, label, pt in distances[:k_neighbors]:
        print(f"  -> Found a {label} roughly {dist:.2f} units of distance away.")
    print(f"Result: '{winning_label}' wins with {votes}/{k_neighbors} votes!")
    
    return winning_label, distances

if __name__ == "__main__":
    print("=== SUPERVISED KNN CLASSIFIER ===")
    
    test_results_to_plot = []
    
    t1_pt = [3.0, 2.5]
    t1_k = 3
    t1_pred, t1_dist = predict_knn(k_neighbors=t1_k, unknown_point=t1_pt, dataset=labeled_data)
    test_results_to_plot.append((t1_pt, t1_k, t1_pred, t1_dist))
    
    t2_pt = [7.0, 6.5]
    t2_k = 3
    t2_pred, t2_dist = predict_knn(k_neighbors=t2_k, unknown_point=t2_pt, dataset=labeled_data)
    test_results_to_plot.append((t2_pt, t2_k, t2_pred, t2_dist))
    
    t3_pt = [4.5, 5.0]
    t3_k = 5
    t3_pred, t3_dist = predict_knn(k_neighbors=t3_k, unknown_point=t3_pt, dataset=labeled_data)
    test_results_to_plot.append((t3_pt, t3_k, t3_pred, t3_dist))

    visualize_knn_animation(labeled_data, test_results_to_plot)
