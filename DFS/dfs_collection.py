GRAPH = {
    'A': ['B', 'C'],  
    'B': ['C', 'E'],  
    'C': ['B', 'E'],  
    'E': []          
}

start_node = 'A'
goal_node = 'E'

def dfs_search(start, goal, graph):
    """Depth-First Search - explores deepest node first (LIFO Stack)"""
    stack = [[start]]
    visited = set()
    
    while stack:
        path = stack.pop()  # LIFO - gets last element (DFS)
        node = path[-1]
        
        if node in visited:
            continue
            
        if node == goal:
            return path  # Return the solution path
        
        visited.add(node)

        # Add neighbors to stack in reverse order to maintain DFS order
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                new_path = path + [neighbor]
                stack.append(new_path)
    
    return []  # No path found

print("DFS (Depth-First Search)")
dfs_path = dfs_search(start_node, goal_node, GRAPH)
print(f"Path: {' -> '.join(dfs_path)}")