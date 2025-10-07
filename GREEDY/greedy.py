
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
   
print("\n--- Greedy Search ---")
greedy_path = greedy_search("Home", "Library")
print("Greedy Path:", greedy_path)