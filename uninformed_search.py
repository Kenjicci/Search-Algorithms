letter = ["A", "B", "C", "D"]

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


# ---------------- MAIN PROGRAM ----------------
start, goal = letter[0], letter[3]  # A to D

# Run Depth-First Search
print("DFS Path:", dfs(start, goal, [start]))

# Run Breadth-First Search
print("BFS Path:", bfs([[start]], goal))    

# Run Uniform Cost Search
ucs_path, ucs_cost = ucs([[start]], goal)
print("UCS Path:", ucs_path, "Cost:", ucs_cost)