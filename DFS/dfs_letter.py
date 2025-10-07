letter = ["A", "B", "C", "D"]

def get_moves(node):
    letter_index = letter.index(node)
    moves = []
    if letter_index +1 < len(letter):
        moves.append(letter[letter_index + 1])
    
    if letter_index + 2 < len(letter):
        moves.append(letter[letter_index + 2])

    return moves

def dfs(current, goal, path):
    if current == goal:
        return path
    
    moves = get_moves(current)

    if not moves:
        return None

    for move in moves:
        if move not in path:
            result = dfs(move, goal, path + [move])
            if result:
                return result
    
    return None

start, goal = letter[0], letter[3]
print("Depth First Search (DFS):", dfs(start, goal, [start]))