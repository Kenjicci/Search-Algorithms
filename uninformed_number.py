# Function that gives the possible moves from a number
def get_moves(number):
    return [number + 1, number + 2]  # From a number, we can go +1 or +2


# ---------------- DFS (Depth First Search) ----------------
def dfs(number, goal, path):
    if number == goal:               # If we reach the goal, return the path
        return path

    moves = get_moves(number)        # Get the possible next numbers

    # First, go deep on the first move
    result = dfs(moves[0], goal, path + [moves[0]])  
    if result:                       # If a solution was found, return it
        return result

    # If the first move did not reach the goal, try the second move
    return dfs(moves[1], goal, path + [moves[1]])


# ---------------- BFS (Breadth First Search) ----------------
def bfs(frontier, goal):
    first = frontier[0]              # Take the first path from the frontier
    number = first[-1]               # Look at the last number in the path

    if number == goal:               # If this path ends at the goal, return it
        return first

    moves = get_moves(number)        # Get possible next numbers
    new_paths = [first + [m] for m in moves]  # Create new paths with moves

    # Add new paths to the end of the frontier and continue
    return bfs(frontier[1:] + new_paths, goal)


# ---------------- UCS (Uniform Cost Search) ----------------
def ucs(frontier, goal):
    # Sort the frontier by total path cost
    frontier = sorted(frontier, key=lambda path: sum(
        [1 if (path[i+1]-path[i])==1 else 2 for i in range(len(path)-1)]
    ))

    path = frontier[0]               # Take the path with the lowest cost
    number = path[-1]                # Look at the last number in this path

    if number == goal:               # If it reaches the goal, return path + cost
        cost = sum([1 if (path[i+1]-path[i])==1 else 2 for i in range(len(path)-1)])
        return path, cost

    moves = get_moves(number)        # Get possible next numbers
    new_paths = [path + [m] for m in moves]  # Create new extended paths

    # Continue searching with updated frontier
    return ucs(frontier[1:] + new_paths, goal)


# ---------------- MAIN PROGRAM ----------------
start, goal = 0, 4

# Run Depth-First Search
print("DFS Path:", dfs(start, goal, [start]))  # Shows the deep-first path

# Run Breadth-First Search
print("BFS Path:", bfs([[start]], goal))       # Shows the shortest path in steps

# Run Uniform Cost Search
ucs_path, ucs_cost = ucs([[start]], goal)
print("UCS Path:", ucs_path, "Cost:", ucs_cost)  # Shows cheapest path and its cost