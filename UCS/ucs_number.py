def get_moves(number):
    return [number+1, number +2]

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

start, goal = 0, 4
print(ucs([[start]], goal))  # Output: ([0, 2, 4], 4)