letter = ['A', 'B', 'C', 'D']

def get_moves(node):
    moves = []
    current_letter = letter.index(node)

    if current_letter + 1 < len(letter):
        moves.append(letter[current_letter + 1])
    if current_letter + 2 < len(letter):
        moves.append(letter[current_letter + 2])

    return moves

def ucs(frontier, goal):
    frontier = sorted(frontier, key=lambda path: sum(
        [1 if (letter.index(path[i+1]) - letter.index(path[i])) == 1 else 2 for i in range(len(path)-1)]
    ))

    path = frontier[0]
    current_letter = path[-1]

    if current_letter == goal:
        cost = sum([1 if (letter.index(path[i+1]) - letter.index(path[i])) == 1 else 2 for i in range(len(path)-1)])
        return path, cost
    moves = get_moves(current_letter)
    new_paths = [path + [m] for m in moves]


    return ucs(frontier[1:] + new_paths, goal)

start, goal = 'A', 'D'
print(ucs([[start]], goal))  # Output: (['A', 'C', 'D'], 4)