letter = ['A', 'B', 'C', 'D']

def get_moves(node):
    moves = []
    current_index = letter.index(node)

    if current_index + 1 < len(letter):
        moves.append(letter[current_index + 1])
    if current_index + 2 < len(letter):
        moves.append(letter[current_index + 2])
    
    return moves

def bfs(frontier, goal):
    first = frontier[0]
    current_letter = first[-1]

    if current_letter == goal:
        return first
    
    moves = get_moves(current_letter)
    new_paths = [first + [m] for m in moves]
    return bfs(frontier[1:] + new_paths, goal)

start, goal = 'A', 'D'
print("BFS path: ", bfs([[start]], goal))