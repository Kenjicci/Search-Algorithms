def get_moves(number):
    return [number + 1, number+ 2]

def dfs(number, goal, path):
    if number == goal:
        return path
    
    moves = get_moves(number)

    result = dfs(moves[0], goal, path + [moves[0]])
    if result:
        return result
    
    return dfs(moves[1], goal, path + [moves[1]])

start, goal = 1, 6
print("Depth First Search (DFS):", dfs(start, goal, [start]))
