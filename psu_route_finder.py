import collections

# DEFINE THE THREE DICTIONARIES BELOW
GRAPH = {
    'A': ['B', 'C'],  # City Proper
    'B': ['C', 'E'],  # Junction 1 (Traffic)
    'C': ['B', 'E'],  # Abanico Jct. (Detour)
    'E': []           # PSU Main Campus
}

COSTS = {
    ('A', 'B'): 5,
    ('A', 'C'): 10,
    ('B', 'C'): 5,
    ('B', 'E'): 20,
    ('C', 'B'): 5,
    ('C', 'E'): 10
}

HEURISTIC = {
    'A': 30,
    'B': 15,
    'C': 5,
    'E': 0
}

start_node = 'A'
goal_node = 'E'

# --- Helper Function ---
def calculate_path_cost(path, costs_dict):
    """Calculates the total time (cost g) for a given path in minutes."""
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += costs_dict.get((path[i], path[i+1]), 0)
    return total_cost


# --- Algorithm Implementations ---

def bfs_search(start, goal, graph):
    """Breadth-First Search - explores fewest edges first (FIFO Queue)"""
    queue = collections.deque([[start]])
    visited = set()
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node in visited:
            continue
        visited.add(node)
        
        if node == goal:
            cost = calculate_path_cost(path, COSTS)
            return (path, cost)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                queue.append(new_path)
    
    return ([], 0)


def dfs_search(start, goal, graph):
    """Depth-First Search - explores deepest node first (LIFO Stack)"""
    stack = [[start]]
    visited = set()
    
    while stack:
        path = stack.pop()
        node = path[-1]
        
        if node in visited:
            continue
        visited.add(node)
        
        if node == goal:
            cost = calculate_path_cost(path, COSTS)
            return (path, cost)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                stack.append(new_path)
    
    return ([], 0)


def ucs_search(start, goal, graph, costs_dict):
    """Uniform Cost Search - explores lowest cost g(n) first"""
    frontier = [(0, [start])]
    visited = set()
    
    while frontier:
        frontier.sort(key=lambda x: x[0])
        cost, path = frontier.pop(0)
        node = path[-1]
        
        if node in visited:
            continue
        visited.add(node)
        
        if node == goal:
            return (path, cost)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                new_cost = calculate_path_cost(new_path, costs_dict)
                frontier.append((new_cost, new_path))
    
    return ([], 0)


def greedy_search(start, goal, graph, heuristic_dict):
    """Greedy Best-First Search - explores lowest heuristic h(n) first"""
    frontier = [(heuristic_dict[start], [start])]
    visited = set()
    
    while frontier:
        frontier.sort(key=lambda x: x[0])
        h_value, path = frontier.pop(0)
        node = path[-1]
        
        if node in visited:
            continue
        visited.add(node)
        
        if node == goal:
            cost = calculate_path_cost(path, COSTS)
            return (path, cost)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                frontier.append((heuristic_dict[neighbor], new_path))
    
    return ([], 0)


def a_star_search(start, goal, graph, costs_dict, heuristic_dict):
    """A* Search - explores lowest f(n) = g(n) + h(n) first"""
    frontier = [(heuristic_dict[start], 0, [start])]
    visited = set()
    
    while frontier:
        frontier.sort(key=lambda x: x[0])
        f_value, g_value, path = frontier.pop(0)
        node = path[-1]
        
        if node in visited:
            continue
        visited.add(node)
        
        if node == goal:
            return (path, g_value)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                new_g = calculate_path_cost(new_path, costs_dict)
                new_f = new_g + heuristic_dict[neighbor]
                frontier.append((new_f, new_g, new_path))
    
    return ([], 0)


# --- MAIN PROGRAM ---
if __name__ == "__main__":
    
    print("BFS (Breadth-First Search)")
    bfs_path, bfs_cost = bfs_search(start_node, goal_node, GRAPH)
    print(f"Path: {' -> '.join(bfs_path)}")
    print(f"Cost: {bfs_cost} minutes")
    
    print("DFS (Depth-First Search)")
    dfs_path, dfs_cost = dfs_search(start_node, goal_node, GRAPH)
    print(f"Path: {' -> '.join(dfs_path)}")
    print(f"Cost: {dfs_cost} minutes")
    
    print("UCS (Uniform Cost Search)")
    ucs_path, ucs_cost = ucs_search(start_node, goal_node, GRAPH, COSTS)
    print(f"Path: {' -> '.join(ucs_path)}")
    print(f"Cost: {ucs_cost} minutes")
    
    print("Greedy Best-First Search")
    greedy_path, greedy_cost = greedy_search(start_node, goal_node, GRAPH, HEURISTIC)
    print(f"Path: {' -> '.join(greedy_path)}")
    print(f"Cost: {greedy_cost} minutes")
    
    print("A* Search")
    astar_path, astar_cost = a_star_search(start_node, goal_node, GRAPH, COSTS, HEURISTIC)
    print(f"Path: {' -> '.join(astar_path)}")
    print(f"Cost: {astar_cost} minutes")
