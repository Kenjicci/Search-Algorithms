def get_moves(number):
    return [number + 1, number + 2]

def bfs(frontier, goal):
    first = frontier[0]
    number = first[-1]

    if number == goal:
        return first
    
    moves = get_moves(number)
    new_paths = [first + [m] for m in moves]

    return bfs(frontier[1:] + new_paths, goal)

start, goal = 0, 3
print("BFS path: ", bfs([[start]], goal))