
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
    'Mall': 2,
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
