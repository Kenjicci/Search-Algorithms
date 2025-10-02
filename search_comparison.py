letter = ["a", "b", "c", "d"]

def get_moves(node):
    letter_index = letter.index(node)
    moves = []
    
    # Check if we can move +1 position
    if letter_index + 1 < len(letter):
        moves.append(letter[letter_index + 1])
    
    # Check if we can move +2 positions
    if letter_index + 2 < len(letter):
        moves.append(letter[letter_index + 2])
    
    return moves


# ---------------- DFS (Depth First Search) ----------------
def dfs(current, goal, path):
    if current == goal:               # If we reach the goal, return the path
        return path

    moves = get_moves(current)        # Get the possible next letters
    
    # If no moves are possible, return None (dead end)
    if not moves:
        return None

    # Try each possible move
    for move in moves:
        # Avoid revisiting letters already in our current path (prevent cycles)
        if move not in path:
            result = dfs(move, goal, path + [move])
            if result:                # If a solution was found, return it
                return result
    
    return None  # No solution found from this path
    
def bfs(frontier, goal):
    first = frontier[0]              # Take the first path from the frontier
    letter = first[-1]               # Look at the last number in the path

    if letter == goal:               # If this path ends at the goal, return it
        return first

    moves = get_moves(letter)        # Get possible next numbers
    new_paths = [first + [m] for m in moves]  # Create new paths with moves

    # Add new paths to the end of the frontier and continue
    return bfs(frontier[1:] + new_paths, goal)
    
def ucs(frontier, goal):
    # Sort the frontier by total path cost
    frontier = sorted(frontier, key=lambda path: sum(
        [2 if (letter.index(path[i+1])-letter.index(path[i]))==1 else 5 for i in range(len(path)-1)]
    ))

    path = frontier[0]               # Take the path with the lowest cost
    current_letter = path[-1]                # Look at the last number in this path

    if current_letter == goal:               # If it reaches the goal, return path 
        cost = sum([2 if (letter.index(path[i+1])-letter.index(path[i]))==1 else 5 for i in range(len(path)-1)])
        return path, cost

    moves = get_moves(current_letter)        # Get possible next numbers
    new_paths = [path + [m] for m in moves]  # Create new extended paths

    # Continue searching with updated frontier
    return ucs(frontier[1:] + new_paths, goal)



# ---------------- Informed Search Algorithms ----------------


# Graph connections (roads between places)
graph = {
    'Home': ['School', 'Mall'],
    'School': ['Library', 'Park'],
    'Mall': ['Library'],
    'Park': ['Library'],
    'Library': []
}

# Heuristic (straight-line guess distance to Library)
heuristic = {
    'Home': 7,
    'School': 6,
    'Mall': 8,
    'Park': 1,
    'Library': 0
}

# Road distances (for A* search g(n))
road_costs = {
    ('Home', 'School'): 2,
    ('Home', 'Mall'): 5,
    ('School', 'Library'): 4,
    ('School', 'Park'): 2,
    ('Mall', 'Library'): 1,
    ('Park', 'Library'): 2
}

# 1. Greedy Best-First Search
def get_best_neighbor_greedy(neighbors):
    best = None
    for node in neighbors:
        if best is None or heuristic[node] < heuristic[best]:
            best = node
    return best

def greedy_search(current, goal, visited=None):
    if visited is None:
        visited = []
    print("Visiting:", current)
    visited.append(current)

    if current == goal:
        print("Reached goal:", goal)
        return visited

    neighbors = [n for n in graph[current] if n not in visited]
    if neighbors:
        next_node = get_best_neighbor_greedy(neighbors)
        return greedy_search(next_node, goal, visited)

    return visited


# 2. A* Search
def get_best_neighbor_a_star(current, neighbors, cost_so_far):
    best = None
    best_f = None

    for node in neighbors:
        g_value = cost_so_far + road_costs.get((current, node), 0)
        f_value = g_value + heuristic[node]

        if best is None or f_value < best_f:
            best = node
            best_f = f_value
    return best

def a_star_search(current, goal, cost_so_far=0, visited=None):
    if visited is None:
        visited = []
    print("Visiting:", current, "with cost so far:", cost_so_far)
    visited.append((current, cost_so_far))

    if current == goal:
        print("Reached goal:", goal, "with total cost:", cost_so_far)
        return visited

    neighbors = [n for n in graph[current] if n not in [v[0] for v in visited]]
    if neighbors:
        next_node = get_best_neighbor_a_star(current, neighbors, cost_so_far)
        new_cost = cost_so_far + road_costs.get((current, next_node), 0)
        return a_star_search(next_node, goal, new_cost, visited)

    return visited



# 3. Graph Search
def graph_search(current, goal, visited=None):
    if visited is None:
        visited = []
    print("Visiting:", current)
    visited.append(current)

    if current == goal:
        print("Reached goal:", goal)
        return visited

    for neighbor in graph[current]:
        if neighbor not in visited:
            result = graph_search(neighbor, goal, visited)
            if result:
                return result
    return None

# ---------------- MAIN PROGRAM ----------------
start, goal = letter[0], letter[3]  # A to D

# Run Depth-First Search
print("DFS Path:", dfs(start, goal, [start]))

# Run Breadth-First Search
print("BFS Path:", bfs([[start]], goal))    

# Run Uniform Cost Search
ucs_path, ucs_cost = ucs([[start]], goal)
print("UCS Path:", ucs_path, "Cost:", ucs_cost)

# Running the searches
print("\n--- Greedy Search ---")
greedy_path = greedy_search("Home", "Library")
print("Greedy Path:", greedy_path)

print("\n--- A* Search ---")
a_star_path = a_star_search("Home", "Library")
print("A* Path with costs:", a_star_path)

print("\n--- Graph Search ---")
graph_path = graph_search("Home", "Library")
print("Graph Search Path:", graph_path)
