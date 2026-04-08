"""
02_01_05_astar_pathfinding.py

Good Old-Fashioned AI (GOFAI): A* Pathfinding Graph Search

Before Machine Learning dominated, "AI" meant solving complex intelligence puzzles 
using graph theory. The A* (A-Star) algorithm is the undisputed king of GOFAI.

It intelligently navigates a physical maze by mathematically scoring every step:
1. G-Score: The actual distance physically walked from the Start.
2. H-Score (Heuristic): An estimated 'straight-line' distance to the Target.
Final Score (F) = G + H

By constantly picking the tile with the lowest F-score, it physically avoids wasting 
time exploring dead ends, organically prioritizing tiles that head directly toward the target!
"""
import heapq

# 0 = Empty Space, 1 = Wall
MAZE = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
]

def heuristic_distance(current, target):
    # Manhattan distance (straight line distance completely ignoring walls)
    # This is the "H-Score" guess.
    return abs(current[0] - target[0]) + abs(current[1] - target[1])

def get_neighbors(node, maze):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # Right, Down, Left, Up
    
    for dx, dy in directions:
        nx, ny = node[0] + dx, node[1] + dy
        
        # Check map bounds and ensure it isn't a wall
        if 0 <= ny < len(maze) and 0 <= nx < len(maze[0]):
            if maze[ny][nx] == 0:
                neighbors.append((nx, ny))
    return neighbors

def astar_search(maze, start, target):
    # Priority Queue format: (F_Score, (x, y))
    frontier = []
    heapq.heappush(frontier, (0, start))
    
    # Track the cheapest path practically taken to reach a node (The G-Score mapping)
    came_from = {start: None}
    g_score = {start: 0}
    
    explored_nodes = 0
    
    while frontier:
        # 1. Pop the tile with the lowest F-Score (The mathematically most promising tile!)
        current_f, current_node = heapq.heappop(frontier)
        explored_nodes += 1
        
        # 2. Did we reach the target?
        if current_node == target:
            # Reconstruct the successful path backwards using our breadcrumbs
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            return path, explored_nodes
            
        # 3. Mathematically evaluate surrounding neighbors
        for next_node in get_neighbors(current_node, maze):
            # Calculate new G-Score (physical distance from start to here)
            new_g = g_score[current_node] + 1
            
            # If we've never seen this tile, or if we found a CHEAPER way to get here
            if next_node not in g_score or new_g < g_score[next_node]:
                g_score[next_node] = new_g
                f_score = new_g + heuristic_distance(next_node, target)
                
                # Push back onto the priority queue!
                heapq.heappush(frontier, (f_score, next_node))
                came_from[next_node] = current_node
                
    # Impossible to reach
    return None, explored_nodes

if __name__ == "__main__":
    # Target is trapped deep inside the maze!
    start_pos = (0, 0)
    target_pos = (2, 2) 
    
    print("=== A* PATHFINDING AI ===")
    print("Navigating maze utilizing Heuristic priority queues...\n")
    
    path, nodes_searched = astar_search(MAZE, start_pos, target_pos)
    
    # 4. VISUALIZE THE AI'S DISCOVERED ROUTE
    for y in range(len(MAZE)):
        row_str = ""
        for x in range(len(MAZE[0])):
            if (x, y) == start_pos:
                row_str += "S "
            elif (x, y) == target_pos:
                row_str += "T "
            elif path and (x, y) in path:
                row_str += "* "
            elif MAZE[y][x] == 1:
                row_str += "█ "
            else:
                row_str += ". "
        print(row_str)
        
    print(f"\n✅ Optimal Path found! Route length: {len(path)-1} moves.")
    print(f"The GOFAI algorithm aggressively ignored bad loops, safely exploring only {nodes_searched} total tiles.")
