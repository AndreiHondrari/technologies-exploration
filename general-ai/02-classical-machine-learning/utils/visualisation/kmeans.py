import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.animation import FuncAnimation

# ==========================================
# 0. BASE ANIMATION CONTROLLER (DRY)
# ==========================================
class BaseKMeansController:
    """
    Common logic for handling Iteration Frame state, 
    Playback toggling, and UI button callbacks.
    """
    def __init__(self, max_frames):
        self.frame = 0
        self.is_playing = False
        self.max_frames = max_frames
        self.btn_play = None # To be linked by the UI builder
        self.draw_callback = None # To be linked by the specific visualizer

    def next_step(self, event=None):
        self.pause()
        if self.frame < self.max_frames - 1:
            self.frame += 1
            self.draw_callback()
            
    def prev_step(self, event=None):
        self.pause()
        if self.frame > 0:
            self.frame -= 1
            self.draw_callback()
            
    def reset_step(self, event=None):
        self.pause()
        self.frame = 0
        self.draw_callback()
        
    def toggle_play(self, event=None):
        self.is_playing = not self.is_playing
        if self.btn_play:
            self.btn_play.label.set_text('Pause' if self.is_playing else 'Play')
            
    def pause(self):
        self.is_playing = False
        if self.btn_play:
            self.btn_play.label.set_text('Play')

    def timer_tick(self, f):
        if self.is_playing:
            if self.frame < self.max_frames - 1:
                self.frame += 1
                self.draw_callback()
            else:
                self.pause()

def setup_standard_buttons(controller, axes_rects):
    """
    Utility to spawn the Reset/Prev/Play/Next button row.
    """
    # rects: [reset, prev, play, next]
    ax_res = plt.axes(axes_rects[0])
    ax_pre = plt.axes(axes_rects[1])
    ax_pla = plt.axes(axes_rects[2])
    ax_nex = plt.axes(axes_rects[3])
    
    btn_res = Button(ax_res, 'Reset', color='#333333', hovercolor='#555555')
    btn_pre = Button(ax_pre, 'Prev', color='#333333', hovercolor='#555555')
    btn_pla = Button(ax_pla, 'Play', color='#333333', hovercolor='#555555')
    btn_nex = Button(ax_nex, 'Next', color='#333333', hovercolor='#555555')
    
    btn_res.on_clicked(controller.reset_step)
    btn_pre.on_clicked(controller.prev_step)
    btn_pla.on_clicked(controller.toggle_play)
    btn_nex.on_clicked(controller.next_step)
    
    controller.btn_play = btn_pla
    return [btn_res, btn_pre, btn_pla, btn_nex] # Return to prevent GC

# ==========================================
# 1. VISUALIZATION ENGINE 
# ==========================================
def visualize_kmeans_animation(history, data_points, title="Autonomous K-Means Clustering"):
    """
    Renders the iterative step-by-step history of K-Means.
    """
    plt.style.use('dark_background')
    colors = ['#FF4B4B', '#4B4BFF', '#22C55E', '#FACC15', '#A855F7', '#38BDF8', '#F472B6'] 
    
    fig, ax = plt.subplots(figsize=(8, 8))
    fig.canvas.manager.set_window_title(f"K-Means Animator: {title}")
    plt.subplots_adjust(bottom=0.2)
    
    controller = BaseKMeansController(max_frames=len(history))
    
    def draw_state():
        ax.clear()
        centroids, clusters = history[controller.frame]
        
        ax.set_title(f"{title}\nIteration {controller.frame}", fontsize=14, pad=15)
        ax.grid(True, linestyle='--', alpha=0.4)
        ax.set_xlim(-1, 11)
        ax.set_ylim(-1, 11)
        
        # 1. Paint data points
        if not clusters or all(len(c) == 0 for c in clusters):
            x_pts = [p[0] for p in data_points]
            y_pts = [p[1] for p in data_points]
            ax.scatter(x_pts, y_pts, c='#aaaaaa', label='Unassigned Points', alpha=0.7, s=50)
        else:
            for i, cluster in enumerate(clusters):
                if not cluster: continue
                x_vals = [p[0] for p in cluster]
                y_vals = [p[1] for p in cluster]
                ax.scatter(x_vals, y_vals, c=colors[i % len(colors)], label=f'Cluster {i}', alpha=0.7, s=50)
                
        # 2. Paint Centroids
        if centroids:
            c_x = [c[0] for c in centroids]
            c_y = [c[1] for c in centroids]
            ax.scatter(c_x, c_y, c='white', marker='X', s=300, label='Centroids', edgecolors='black', linewidths=1.5)
        
        ax.legend(loc='upper right')
        fig.canvas.draw_idle()

    controller.draw_callback = draw_state
    
    # Layout the buttons
    btns = setup_standard_buttons(controller, [
        [0.25, 0.05, 0.1, 0.075], # Reset
        [0.4, 0.05, 0.1, 0.075],  # Prev
        [0.55, 0.05, 0.1, 0.075], # Play
        [0.7, 0.05, 0.1, 0.075]   # Next
    ])
    
    draw_state()
    anim = FuncAnimation(fig, controller.timer_tick, interval=1500, cache_frame_data=False)
    plt.show()

def visualize_elbow_multipanel_animation(k_values, all_histories, errors, data_points):
    """
    Renders an 8-panel multiplexed animation showing K-Means evolution side-by-side.
    """
    plt.style.use('dark_background')
    colors = ['#FF4B4B', '#4B4BFF', '#22C55E', '#FACC15', '#A855F7', '#38BDF8', '#F472B6'] 
    
    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    fig.canvas.manager.set_window_title("Experiment 2: The Elbow Method (Multiplexed)")
    plt.subplots_adjust(bottom=0.15, hspace=0.4, wspace=0.3)
    
    axes_flat = axes.flatten()
    max_frames = max(len(h) for h in all_histories)
    
    controller = BaseKMeansController(max_frames=max_frames)
    
    def draw_state():
        fig.suptitle(f"The Elbow Method Multiplexer — Iteration {controller.frame}", fontsize=16, color='white')
        
        # Panel 1-7: The Iterative Animations
        for i in range(len(k_values)):
            ax = axes_flat[i]
            ax.clear()
            
            history = all_histories[i]
            frame_idx = min(controller.frame, len(history) - 1)
            centroids, clusters = history[frame_idx]
            
            ax.set_title(f"K={k_values[i]}", fontsize=12)
            ax.grid(True, linestyle='--', alpha=0.3)
            ax.set_xlim(-1, 11); ax.set_ylim(-1, 11)
            ax.set_xticks([]); ax.set_yticks([])
            
            if not clusters or all(len(c) == 0 for c in clusters):
                x_pts, y_pts = [p[0] for p in data_points], [p[1] for p in data_points]
                ax.scatter(x_pts, y_pts, c='#aaaaaa', alpha=0.5, s=10)
            else:
                for c_idx, cluster in enumerate(clusters):
                    if not cluster: continue
                    x_v, y_v = [p[0] for p in cluster], [p[1] for p in cluster]
                    ax.scatter(x_v, y_v, c=colors[c_idx % len(colors)], alpha=0.5, s=10)
                    
            if centroids:
                c_x, c_y = [c[0] for c in centroids], [c[1] for c in centroids]
                ax.scatter(c_x, c_y, c='white', marker='X', s=50, edgecolors='black')
        
        # Panel 8: The Analytical Elbow Curve
        ax_elbow = axes_flat[7]
        ax_elbow.clear()
        ax_elbow.set_title("The Final Elbow Curve", color='yellow', fontsize=12)
        ax_elbow.set_xlabel("K"); ax_elbow.set_ylabel("Inertia")
        ax_elbow.plot(k_values, errors, color='#38BDF8', marker='o', linewidth=2, markersize=5)
        ax_elbow.set_xticks(k_values) # Explicitly show all integer K values
        ax_elbow.grid(True, linestyle='--', alpha=0.3)
        
        elbow_k = 3 
        if elbow_k in k_values:
            idx = list(k_values).index(elbow_k)
            ax_elbow.scatter([elbow_k], [errors[idx]], color='yellow', s=100, zorder=5)
            
        fig.canvas.draw_idle()

    controller.draw_callback = draw_state
    
    # Layout buttons
    btns = setup_standard_buttons(controller, [
        [0.38, 0.02, 0.05, 0.05], # Reset
        [0.44, 0.02, 0.05, 0.05], # Prev
        [0.50, 0.02, 0.05, 0.05], # Play
        [0.56, 0.02, 0.05, 0.05]  # Next
    ])
    
    draw_state()
    anim = FuncAnimation(fig, controller.timer_tick, interval=1000, cache_frame_data=False)
    plt.show()
